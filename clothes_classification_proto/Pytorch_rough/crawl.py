# 선언
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

save_root = 'downloads'
if not os.path.exists(save_root): os.makedirs(save_root)


def get_images(query='apple', limit=20):
    save_path = os.path.join(save_root, query)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 한글 검색 자동 변환
    url = baseUrl + quote_plus(query)
    html = urlopen(url)
    soup = bs(html, "html.parser")
    img = soup.find_all(class_='_img', limit=limit)

    n = 1
    for i in img:
        imgUrl = i['data-source']
        with urlopen(imgUrl) as f:
            with open(os.path.join(save_path, str(n) + '.jpg'), 'wb') as h:  # w - write b - binary
                img = f.read()
                h.write(img)
        n += 1
    print('%s download complete' % (query))


queries = ['남성 7부 셔츠']

num_limit = 1100

for query in queries:
    get_images(query=query, limit=num_limit)

print('done!!')
beep = lambda x: os.system("echo -n '\a';sleep 0.3;" * x)
beep(3)
