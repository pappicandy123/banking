from django.db import models
from django.contrib.auth.models import User

# Create your models here.  



class Checking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_acc_holder = models.CharField(max_length=250)
    c_bank = models.CharField(max_length=250, blank=True, null=True)
    c_acc_name = models.CharField(max_length=250, blank=True, null=True)
    c_acc_num = models.IntegerField(blank=True, null=True)
    c_purpose = models.TextField(blank=True, null=True)
    checkings_account = models.BooleanField()
    c_credit = models.IntegerField(blank=True, null=True)
    c_debit = models.IntegerField(blank=True, null=True)
    c_balance = models.IntegerField(blank=True, null=True)
    c_success = models.BooleanField(default=False)
    c_debit_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username



class Saving(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    s_acc_holder = models.CharField(max_length=250)
    s_bank = models.CharField(max_length=250, blank=True, null=True)
    s_acc_name = models.CharField(max_length=250, blank=True, null=True)
    s_acc_num = models.IntegerField(blank=True, null=True)
    s_purpose = models.TextField(blank=True, null=True)
    savings_account = models.BooleanField()
    s_credit = models.IntegerField(blank=True, null=True)
    s_debit = models.IntegerField(blank=True, null=True)
    s_balance = models.IntegerField(blank=True, null=True)
    s_success = models.BooleanField(default=False)
    s_debit_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username
        



    

