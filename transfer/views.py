from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login

# Create your views here.


def index(request):
     if request.method =="POST":
        name = request.POST['username']
        passw = request.POST['password']
        user = authenticate(username = name, password = passw)
        if user:
            login(request, user)
            messages.success(request, 'signin successful')
            return redirect('main')
        else:
            messages.warning(request, 'username/password incorrect')
            return redirect('index')    
     return render(request, 'index.html')

    
def main(request):
    incoming_debit = Checking.objects.filter(user__username = request.user.username).last()
    new_balance = incoming_debit.c_balance

    incoming_credit = Checking.objects.filter(user__username = request.user.username).last()
    credit_balance = incoming_credit.c_balance

    incoming_deb = Saving.objects.filter(user__username = request.user.username).last()
    save_balance = incoming_deb.s_balance

    incoming_sav = Saving.objects.filter(user__username = request.user.username).last()
    sav_balance = incoming_sav.s_balance

    incoming_tra = Saving.objects.filter(user__username = request.user.username).last()
    incoming_money = incoming_tra.s_balance

    incoming_tran = Checking.objects.filter(user__username = request.user.username).last()
    outgoing =  incoming_tran.c_balance



    history = Checking.objects.filter(user__username = request.user.username, c_success = True, checkings_account = True).order_by('-id')
    saving_history = Saving.objects.filter(user__username = request.user.username, s_success = True, savings_account = True).order_by('-id')


    return render(request, 'main.html',{'new_balance':new_balance,
    'history':history,'credit_balance':credit_balance,'save_balance':save_balance,'saving_history':saving_history,' sav_balance': sav_balance,'incoming_money':incoming_money,'outgoing':outgoing
    })

def signup(request):
    return render(request, 'signup.html')

def transferbank(request):
    bot = User.objects.get(username = request.user.username)

    new_checkings = Checking.objects.filter(user__username = request.user.username).last()
    new_c =  new_checkings.c_balance

    moving = Checking.objects.filter(user__username = bot).last()
    creditbalance = moving.c_balance

    if request.method == 'POST':
        owo = int(request.POST['owo'])
        num = request.POST['num']
        name = request.POST['name']
        purp = request.POST['purp']
        bankn = request.POST['bankn']
        person_name = request.POST['person_name']

        


        new_checkings = Checking.objects.filter(user__username = request.user.username).last()
        chec =  new_checkings.c_balance
        new_c = int(chec)


        pick = Checking()
        pick.user = request.user
        pick.c_bank = bankn
        pick.c_acc_name = name
        pick.c_acc_num = num
        pick.c_purpose = purp
        pick.checkings_account = True
        pick.c_debit = owo
        pick.c_balance = int(chec) - int(owo)
        pick.c_success = True
        pick.save()


        bot = User.objects.get(username = person_name)
        moving = Checking.objects.filter(user__username = bot).last()
        newcredit = moving.c_balance
        creditbalance = int(newcredit)

        goal = Checking()
        goal.user = bot
        goal.c_bank = bankn
        goal.c_acc_name = name
        goal.c_acc_num = num
        goal.c_purpose = purp
        goal.checkings_account = True
        goal.c_credit = owo
        goal.c_balance = int(newcredit) + int(owo)
        goal.c_success = True
        goal.save()
        messages.success(request, 'transaction successful')
        return redirect('sucesspage')
    
    context = {
        'creditbalance':creditbalance,
        'new_c': new_c 

    }
    
       


    return render(request, 'transferbank.html', context)

def transfer(request):
    who = User.objects.get(username = request.user.username)
    incoming_tra = Saving.objects.filter(user__username = request.user.username).last()
    incoming_money = incoming_tra.s_balance

    incoming_tran = Checking.objects.filter(user__username = request.user.username).last()
    outgoing =  incoming_tran.c_balance
    if request.method == 'POST':
        m = int(request.POST['m'])
        a = request.POST['a']
        b = request.POST['b']
        p = request.POST['p']
        ba = request.POST['ba']
        
        incoming_tra = Saving.objects.filter(user__username = request.user.username).last()
        incoming_save = incoming_tra.s_balance
        incoming_money = int(incoming_save )
        save_bank = Saving()
        save_bank.user = who
        save_bank.s_acc_holder = f'{who.first_name} {who.last_name}'
        save_bank.s_bank = ba
        save_bank.s_acc_name = a
        save_bank.s_acc_num = b
        save_bank.s_purpose = p
        save_bank.savings_account = True
        save_bank.s_credit = m
        save_bank.s_balance = int(incoming_save) + int(m)
        save_bank.s_success = True
        save_bank.save()


        incoming_tran = Checking.objects.filter(user__username = request.user.username).last()
        check_bal =  incoming_tran.c_balance
        outgoing = int(check_bal)
        box = Checking()
        box.user = who
        box.c_acc_holder = f'{who.first_name} {who.last_name}'
        box.c_bank = ba
        box.c_acc_name = a
        box.c_acc_num = b
        box.c_purpose = p
        box.checkings_account = True
        box.c_debit = m
        box.c_balance = int(check_bal) - int(m)
        box.c_success = True
        box.save()
        messages.success(request, 'transaction successful')
        return redirect('sucesspage')
    context = {
         
         'outgoing':outgoing,
         'incoming_money':incoming_money 
         
    } 

    return render(request, 'transfer.html',context)


def credit_saving(request):
    person = User.objects.get(username = request.user.username)
    incoming_sav = Saving.objects.filter(user__username = request.user.username).last()
    sav_balance = incoming_sav.s_balance
    if request.method == 'POST':
        money = int(request.POST['money'])
        accountname = request.POST['accountname']
        bankno = request.POST['bankno']
        purposename = request.POST['purposename']
        bankname = request.POST['bankname']
        

        incoming_sav = Saving.objects.filter(user__username = request.user.username).last()
        credit_bal = incoming_sav.s_balance
        sav_balance = int(credit_bal )
        credit_bank = Saving()
        credit_bank.user = person
        credit_bank.s_acc_holder = f'{person.first_name} {person.last_name}'
        credit_bank.s_bank = bankname
        credit_bank.s_acc_name = accountname
        credit_bank.s_acc_num = bankno
        credit_bank.s_purpose = purposename
        credit_bank.savings_account = True
        credit_bank.s_credit = money
        credit_bank.s_balance = int(credit_bal) + int(money)
        credit_bank.s_success = True
        credit_bank.save()
        messages.success(request, 'transaction successful')
        return redirect('sucesspage')
    
    context = {
         'person':person,
         'sav_balance':sav_balance 
         
    } 
    

    return render(request, 'credit_saving.html', context)

def savings(request):
    sender = User.objects.get(username = request.user.username)
    incoming_deb = Saving.objects.filter(user__username = request.user.username).last()
    save_balance = incoming_deb.s_balance
    if request.method == 'POST':
        am = int(request.POST['am'])
        acc = request.POST['acc']
        acn = request.POST['acn']
        pur = request.POST['pur']
        banking = request.POST['banking']
        

        incoming_deb = Saving.objects.filter(user__username = request.user.username).last()
        saving_bal = incoming_deb.s_balance
        save_balance = int(saving_bal)
        savings_bank = Saving()
        savings_bank.user = sender
        savings_bank.s_acc_holder = f'{sender.first_name} {sender.last_name}'
        savings_bank.s_bank = banking
        savings_bank.s_acc_name = acn
        savings_bank.s_acc_num = acc
        savings_bank.s_purpose = pur
        savings_bank.savings_account = True
        savings_bank.s_debit = am
        savings_bank.s_balance = int(saving_bal) - int(am)
        savings_bank.s_success = True
        savings_bank.save()
        messages.success(request, 'transaction successful')
        return redirect('sucesspage')
    
    context = {
         'sender':sender,
         'save_balance':save_balance 
         
    } 
    return render(request, 'savings.html', context)

def credit(request):
    owner = User.objects.get(username = request.user.username)
    incoming_credit = Checking.objects.filter(user__username = request.user.username).last()
    credit_balance = incoming_credit.c_balance
    if request.method == 'POST':
        amo = int(request.POST['amo'])
        accno = request.POST['accno']
        accname = request.POST['accname']
        purpose_main = request.POST['purpose_main']
        bank_name = request.POST['bank_name']

        incoming_credit = Checking.objects.filter(user__username = request.user.username).last()
        new_credit = incoming_credit.c_balance
        credit_balance = int(new_credit)
        increase = Checking()
        increase.user = owner
        increase.c_acc_holder = f'{owner.first_name} {owner.last_name}'
        increase.c_bank = bank_name
        increase.c_acc_name = accname
        increase.c_acc_num = accno
        increase.c_purpose = purpose_main
        increase.checkings_account = True
        increase.c_credit = amo
        increase.c_balance = int(new_credit) + int(amo)
        increase.c_success = True
        increase.save()
        messages.success(request, 'transaction successful')
        return redirect('sucesspage')
    
    context = {
        'owner':owner,
        'credit_balance':credit_balance
    }
    return render(request, 'credit.html', context)

def checkings(request):
    sender = User.objects.get(username = request.user.username)
    incoming_debit = Checking.objects.filter(user__username = request.user.username).last()
    new_balance = incoming_debit.c_balance
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        acc_no = request.POST['acc_no']
        acc_name = request.POST['acc_name']
        purpose = request.POST['purpose']
        bank = request.POST['bank']
        
        if new_balance >= amount:
            incoming_debit = Checking.objects.filter(user__username = request.user.username).last()
            credit_bal = incoming_debit.c_balance
            new_balance = int(credit_bal)
            transact = Checking()
            transact.user = sender
            transact.c_acc_holder = f'{sender.first_name} {sender.last_name}'
            transact.c_bank = bank
            transact.c_acc_name = acc_name
            transact.c_acc_num = acc_no
            transact.c_purpose = purpose
            transact.checkings_account = True
            transact.c_debit = amount
            transact.c_balance = int(credit_bal) - int(amount)
            transact.c_success = True
            transact.save()
            messages.success(request, 'transaction successful')
            return redirect('sucesspage')
        else:
            messages.success(request, 'insuficient fund')
            return redirect('main')
        
        

    
    context = {
         'sender':sender,
         'new_balance':new_balance
         
    } 
    return render(request, 'checkings.html', context)

def sucesspage(request):
    client = User.objects.get(username = request.user.username)
    return render(request, 'sucesspage.html', {'client':client})