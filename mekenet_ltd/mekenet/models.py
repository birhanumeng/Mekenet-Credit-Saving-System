from django.db import models
#import UUID


class CustomerInfo(models.Model):
    """ All cusomer information in the company """
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    sex = models.CharField(max_length=50)
    shares = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    membership = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    
    def __str__(self):
        """ print customer information """
        return f"{self.name}: {self.membership}"
    
    def generateId():
        """ generating customer id """


class CustomerSaving(models.Model):
    """ Creating customers iniformation data relating to their saving """
    name = models.CharField(max_length=200)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    undue = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    compulsary = models.IntegerField()
    voluntary = models.IntegerField()
    vocher = models.CharField(max_length=200)
    maker = models.CharField(max_length=200, null=True, blank=True)
    authorizer = models.CharField(max_length=200, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    interest = models.IntegerField(null=True, blank=True)
    balance = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """ print the saving name """
        return self.name


class CustomerLoan(models.Model):
    """ Creating customers iniformation data relating to their loan """
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(null=True, blank=True)
    catagory = models.CharField(max_length=50)
    repayment = models.IntegerField()
    collateral = models.CharField(max_length=200)
    loan_term = models.CharField(max_length=200)
    return_date = models.DateTimeField(auto_now_add=True)
    maker = models.CharField(max_length=200)
    authorizer = models.CharField(max_length=200)
    interest = models.IntegerField()
    balance = models.IntegerField()

    def __str__(self):
        """ print the loan taker name """
        return self.name
