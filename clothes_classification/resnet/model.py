from __future__ import print_function, division
import torch.utils.data
from PIL import Image
from torch.autograd import Variable
from torchvision import transforms
import torch.nn.functional as f

class Classify:
    def __init__(self, mod):
        self.mod = mod

    def predict(self, img, crop, x=0):            # x=1 -> use crop (inner)      
        model = torch.load(self.mod, map_location=torch.device('cpu'))
        model.eval()

        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

        input_image = Image.open(img)
        if x==1:
            input_image = input_image.crop((crop["x1"], crop["y1"], crop["x2"], crop["y2"]))
        
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        image_tensor = preprocess(input_image).float()
        image_tensor = image_tensor.unsqueeze_(0)
        input = Variable(image_tensor)
        input = input.to(device)
        output = model(input)
        index = output.data.cpu().numpy().argmax()
        softval = f.softmax(output, dim=1).cpu().detach().numpy()[0][index]
        if softval >= 0.1:
            return index
        else:
            return None
