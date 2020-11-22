from django.db import models
from restApi.models import Account

class Mcasual(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Mcasuallike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Mcampus(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Mcampuslike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Mminimal(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Mminimallike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Mstreet(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Mstreetlike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Mtravel(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Mtravellike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Msports(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Msportslike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Mformal(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Mformallike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Mdandy(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Mdandylike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Munique(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Muniquelike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Mworkwear(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Mworkwearlike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


# Woman coordination
class Wcampus(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wcampuslike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wsports(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wsportslike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wcasual(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wcasuallike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wformal(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wformallike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wromantic(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wromanticlike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wgirlish(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wgirlishlike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wstreet(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wstreetlike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wfeminine(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wfemininelike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wtravel(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wtravellike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wunique(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wuniquelike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wworkwear(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wworkwearlike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wminimal(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wminimallike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()


class Wdandy(models.Model):                 #place to preserve coordinates image
    outer = models.CharField(max_length=30, blank=True)
    outercol = models.CharField(max_length=30, blank=True)
    top = models.CharField(max_length=30, blank=True)
    topcol = models.CharField(max_length=30, blank=True)
    bottom = models.CharField(max_length=30, blank=True)
    bottomcol = models.CharField(max_length=30, blank=True)
    dress = models.CharField(max_length=30, blank=True)
    dresscol = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=100)

class Wdandylike(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    num = models.IntegerField()

