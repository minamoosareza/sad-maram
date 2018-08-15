from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail, mail_admins
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#import requests
from django.shortcuts import render
import datetime
from django.utils import timezone
# Create your views here.
from django.contrib.auth.models import User

from blog.forms import NameForm, NameForm2, Nform, ChangePassWordForm, add_employee2, ChangeSalary, ContactForm, GREForm, TOEFLForm, IELTSForm
# from blog.models import MyUser
from blog.models import MyUser, Employee, Transaction, Message, MyUserManager
from django.shortcuts import redirect
from django.db.models import Q


def profile(request):
    f=NameForm()
    return render (request , 'register.html' , {'form':f})

@login_required(redirect_field_name='login')
def edit(request):
    f=NameForm2(instance=request.user)
    return render (request , 'profile_edit_user.html' , {'form':f , 'user': request.user})
@login_required(redirect_field_name='login')
def bala_pass(request):
    f=ChangePassWordForm(request.POST)
    return render (request , 'change_password.html' , {'form':f})

@login_required(redirect_field_name='login')
def bala_add_employee(request):
    f=add_employee2(instance=request.user)
    return render (request , 'add_employee.html' , {'form':f , 'user': request.user})

def upload_file(request):
    form = NameForm(request.POST, request.FILES)
    if request.method == 'POST' :
        if form.is_valid():
                user = form.save();
                user.set_password(form.data['password'])
                # user = MyUser.objects.create_user(name=form.data['name'], email=form.data['email'],  acc_num=form.data['acc_num'])
                messages.success(request, 'ثبت نام با موفقیت انجام شد')
                user.save();
                return render(request, 'register.html', { 'user':user
                })
    return render(request, 'register.html', {'form':form})

@login_required(redirect_field_name='login')
def edit_user_profile(request):
    form = NameForm2(request.POST)

    if request.method == 'POST' :
        if form.is_valid():
            user =  MyUser.objects.get(pk = request.user.pk)
            user.name = form.cleaned_data['name']
            user.acc_num = form.cleaned_data['acc_num']
            try:
                user.email = form.cleaned_data['email']
            except:
                pass
            messages.success(request, 'ویرایش با موفقیت انجام شد')
            user.save()
            return render(request, 'profile_edit_user.html', {})
        else:
            user =  MyUser.objects.get(pk = request.user.pk)
            user.name = form.cleaned_data['name']
            user.acc_num = form.cleaned_data['acc_num']
            messages.success(request, 'ویرایش با موفقیت انجام شد')
            user.save()
            return render(request, 'profile_edit_user.html', {})
    return render(request, 'profile_edit_user.html', {'form':form})


@login_required(redirect_field_name='login')
def change_pass(request):
    form = ChangePassWordForm(request.POST)
    if request.method == 'POST' :
        if form.is_valid():
            u = MyUser.objects.get(pk=request.user.pk)
            if u.password == form.cleaned_data['old_pass'] and form.cleaned_data['new_pass'] == form.cleaned_data['repeat_pass']  :
                u.set_password(form.cleaned_data['new_pass'])
                u.save()
                messages.success(request, 'تغییر رمز با موفقیت انجام شد')
                u.save()
                return render(request, 'change_password.html', {})
            else:
                messages.success(request, 'ورودی های خود را چک کنید')
    return render(request, 'change_password.html', {'form':form})

@login_required(redirect_field_name='login')
def add_employee(request):
    form = add_employee2(request.POST)
    if request.method == 'POST':
        print("hhhhhhhhhhhhhhhhhhhhhhhhh")
        if form.is_valid():
            print("yeeeeeeeeeeeeeeeeeeeeeeeees")
            user = form.save()
            user.set_password('123456')
            user.save()
            messages.success(request, 'ثبت کارمند با موفقیت انجام شد')
            return render(request, 'add_employee.html', {'user': user, 'form':form})

        return render(request, 'add_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    print("fffffffffffffffffffffffffffffffff   ")
    print(employees)
    return render(request, 'employee_list.html',{'employees':employees} )

def see_employee_profile(request, pke):
    e = Employee.objects.filter(pk = pke).first()
    return render(request, 'employee_profile.html' , {'e':e})


def bala_change_employee_salary(request,pke):
    form = ChangeSalary(request.POST)

    u = Employee.objects.get(pk=pke)

    return render(request, 'change_employee_salary.html' ,{'form':form , 'e':u} )

def change_salary(request , pke):
    form = ChangeSalary(request.POST)
    if request.method == 'POST' :
        if form.is_valid():
            u = Employee.objects.get(pk=pke)
            u.salary = form.data['new_salary']
            u.save()
            messages.success(request, 'تغییر حقوق با موفقیت انجام شد')
            return render(request, 'change_employee_salary.html', {'form':form , 'e':u})
        else:
                messages.success(request, 'ورودی های خود را چک کنید')
    return render(request, 'change_employee_salary.html', {'form':form })


def ban_employee(request, pke):
    pass #todo

def see_employee_transactions(request, pke):
    e = Employee.objects.filter(pk = pke).first()
    t = Transaction.objects.filter(employee = e)
    return render(request, 'employee_transactions.html', {'transactions': t , 'e':e})

def see_transaction_context(request, pkt):
    t = Transaction.objects.filter(pk = pkt).first()
    return render(request , 'transaction_context.html' , {'t':t})

def contactus(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.data['name']
            email = form.data['email']
            message = form.data['message']
            #man = MyUserManager.objects.all()[0]
            sendmessage = Message.objects.create(author=request.user, reciever = request.user, content=form.data['message'], subject=form.data['name'])
            sendmessage.save()
            if  message and email:
                try:
                    send_mail(name, message, 'm.s.moosareza@gmail.com', ['m.mina1997@yahoo.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            else:
        # In reality we'd use a form class
        # to get proper validation errors.
                return HttpResponse('Make sure all fields are entered and valid.')
            messages.success(request, 'پیام شما با موفقیت ارسال شد')
            return redirect('contactus')
        else:
            messages.success(request, 'مشکلی در ارسال پیام وجود دارد. ورودی های خود را بررسی کنید!')
    else:
        form = ContactForm(request.POST)	
    return render(request, 'contactus.html', {'form': form})

def gre(request):
    if request.method == "POST":
        form = GREForm(request.POST)
        if form.is_valid():
            gre = form.save()
            gre.save()
            u = MyUser.objects.get(pk=request.user.pk)
            e = Employee.objects.all()[0]
            transaction = Transaction.objects.create(type="GRE",employee=e,  user =u, subject = "GRE", GREForm = gre)
            transaction.save()
            sendmessage = Message.objects.create(author=request.user, reciever = request.user, content='تراکنش ثبت نام در آزمون GRE برای شما ثبت شد', subject='آزمون GRE')
            sendmessage.save()
            messages.success(request, 'درخواست شما با موفقیت ثبت گردید')
            return redirect('gre')
        else:
            messages.success(request, 'مشکلی در ارسال پیام وجود دارد. ورودی های خود را بررسی کنید!')
    else:
        form = GREForm(request.POST)	
    return render(request, 'GRE.html', {'form': form})

def toefl(request):
    if request.method == "POST":
        form = TOEFLForm(request.POST)
        if form.is_valid():
            toefl = form.save()
            toefl.save()
            u = MyUser.objects.get(pk=request.user.pk)
            e = Employee.objects.all()[0]
            transaction = Transaction.objects.create(type="TOEFT",employee=e,  user =u, subject = "TOEFL", TOEFLForm = toefl)
            transaction.save()
            sendmessage = Message.objects.create(author=request.user, reciever = request.user, content='تراکنش ثبت نام در آزمون TOEFL برای شما ثبت شد', subject='آزمون TOEFL')
            sendmessage.save()
            messages.success(request, 'درخواست شما با موفقیت ثبت گردید')
            return redirect('toefl')
        else:
            messages.success(request, 'مشکلی در ارسال پیام وجود دارد. ورودی های خود را بررسی کنید!')
    else:
        form = TOEFLForm(request.POST)	
    return render(request, 'TOEFL.html', {'form': form})

def ielts(request):
    if request.method == "POST":
        form = IELTSForm(request.POST)
        if form.is_valid():
            ielts = form.save()
            ielts.save()
            u = MyUser.objects.get(pk=request.user.pk)
            e = Employee.objects.all()[0]
            transaction = Transaction.objects.create(type="IELTS",employee=e,  user =u, subject = "IELTS", IELTSForm = ielts)
            transaction.save()
            sendmessage = Message.objects.create(author=request.user, reciever = request.user, content='تراکنش ثبت نام در آزمون IELTS برای شما ثبت شد', subject='آزمون IELTS')
            sendmessage.save()
            messages.success(request, 'درخواست شما با موفقیت ثبت گردید')
            return redirect('ielts')
        else:
            messages.success(request, 'مشکلی در ارسال پیام وجود دارد. ورودی های خود را بررسی کنید!')
    else:
        form = IELTSForm(request.POST)	
    return render(request, 'IELTS.html', {'form': form})


def managertransactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'managertransactions.html', {'transactions':transactions})

def message(request, pk):
    messages = Message.objects.filter(reciever = request.user)
    return render(request, 'message.html', {'messages':messages})

def transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if transaction.type == "GRE":
        f = transaction.greform
        return render(request, 'gretransaction.html', {'gre':f})
    elif transaction.type == "TOEFL":
        f = transaction.toeflform
        return render(request, 'toefltransaction.html', {'toefl':f})
    elif transaction.type == "IELTS":
        f = transaction.ieltsform
        return render(request, 'ieltstransaction.html', {'ielts':f})
    return render(request, 'employeetransactions.html')

def employeetransactions(request):
    s = "در حال انتظار"
    transactions = Transaction.objects.filter(~Q(status = s), ~Q(status = 'قبول شده'))
    return render(request, 'employeetransactions.html', {'transactions':transactions})

def inform(request, pk):
    if request.method == "POST":
        print("iiiiiiiinnnnnnnn")
        sendmessage = Message.objects.create(author=request.user, reciever = request.user, content='اطلاع حالت غیر عادی برای تراکنش ', subject='حالت غیرعادی', transaction=get_object_or_404(Transaction, pk=pk))
        sendmessage.save()
        
        messages.success(request, 'درخواست شما با موفقیت ثبت گردید')
    print("iiiiiiiinnnnnnnn۲")
    return render(request, 'inform.html')

def yes(request, pk):
    transaction=get_object_or_404(Transaction, pk=pk)
    transaction.status = 'تایید شده'
    transaction.save()
    messages.success(request, 'درخواست شما با موفقیت ثبت گردید')
    return render(request, 'accept.html', {'transaction':transaction})

def accept(request, pk):
    transaction=get_object_or_404(Transaction, pk=pk)
    transaction.status = 'قبول شده'
    transaction.save()
    transaction.employee = Employee.objects.all()[0]
    messages.success(request, 'درخواست شما با موفقیت ثبت گردید')
    return render(request, 'accept.html', {'transaction':transaction})

def no(request, pk):
    transaction=get_object_or_404(Transaction, pk=pk)
    transaction.status = 'رد شده'
    transaction.save()
    messages.success(request, 'درخواست شما با موفقیت ثبت گردید')
    return render(request, 'accept.html', {'transaction':transaction})

def runtransactions(request, pk):
    transactions = Transaction.objects.filter(status = 'قبول شده' , employee = Employee.objects.all()[0])
    return render(request, 'runtransactions.html', {'transactions':transactions})

def waitingtransactions(request):
    s = "در حال انتظار"
    transactions = Transaction.objects.filter(status = s)
    return render(request, 'waitingtransactions.html', {'transactions':transactions})

def usertransactions(request, pk):
    u = MyUser.objects.get(pk=request.user.pk)
    transactions = Transaction.objects.filter(user = u)
    return render(request, 'usertransactions.html', {'transactions':transactions})

def gretransaction(request, pk):
    g = get_object_or_404(Transaction, pk=pk)
    return render(request, 'gretransaction.html', {'transaction': g})

def nerkh_arz(request):
    response = requests.get('https://www.faranevis.com/api/currency/')
    geodata = response.json()
    return render(request, 'nerkh_arz.html', {
        'dollar': geodata['دلار'],
        'euro': geodata['یورو'],
})
