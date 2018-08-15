from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.forms import ModelForm

from blog.models import MyUser, Employee, GREForm, TOEFLForm, IELTSForm


class NameForm(forms.ModelForm):
    error_css_class = "error"
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "ایمیل"
        self.fields['name'].label = "نام و نام خانوادگی"
        self.fields['password'].label = "رمز عبور"
        self.fields['acc_num'].label = "شماره حساب"
        self.fields['email'].required = True
    class Meta:
        model =MyUser
        fields = ['name', 'email', 'password', 'acc_num']
        error_messages = {
            'email': {
                'unique': ('این ایمیل قبلا استفاده شده است.'),
                'required': ('وارد کردن ایمیل ضروری است'),
            }
        }
        widgets = {'password': forms.TextInput(
                     attrs={'type': 'password', 'required': True}
            ),
        }


class NameForm2(forms.ModelForm):

    class Meta:
        model =MyUser
        fields = ['name', 'email',  'acc_num' ]
        labels ={
            'email': "ایمیل",
            'name': "نام و نام خانوادگی",
            'acc_num': 'شماره حساب',

        }

class ChangePassWordForm(forms.Form):
    old_pass = forms.CharField(max_length=80, widget=forms.PasswordInput(), label=u"رمز عبور")
    new_pass = forms.CharField(max_length=80, widget=forms.PasswordInput(), label=u"رمز عبور جديد")
    repeat_pass = forms.CharField(max_length=80, widget=forms.PasswordInput(), label=u"تکرار رمز عبور جدید")


class add_employee2(forms.ModelForm):
    class Meta:
        model =Employee
        fields = ['name', 'email',  'acc_num' , 'salary' ]
        labels ={
            'email': "ایمیل",
            'name': "نام و نام خانوادگی",
            'acc_num': 'شماره حساب',
            'salary': "حقوق",
        }

class ChangeSalary(forms.Form):
    new_salary = forms.CharField(max_length=80, widget=forms.NumberInput(), label=u"حقوق جدید")


class Nform():
    class Meta:
        pass

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class ContactForm(forms.Form):

    name = forms.CharField(max_length=200, label=u"نام")
    email = forms.EmailField(max_length=200, label=u"ایمیل")
    message = forms.CharField(widget=forms.Textarea, label=u"پیام")

class GREForm(forms.ModelForm):
    class Meta:
        model =GREForm
        fields = ['name', 'password',  'city' , 'country', 'center', 'placecode', 'education', 'citizen', 'major', 'majorcode', 'explanation', 'date', ]
        labels ={
            'name' : "نام کاربری",
            'password': "رمز عبور",
            'city': 'شهر',
            'country': "کشور",
            'center': "مرکز محل آزمون",
            'placecode': "کد محل آزمون",
            'education': "وضعیت تحصیلی",
            'citizen': "وضعیت شهروندی",
            'major': "نام رشته",
            'majorcode': "کد رشته",
            'explanation': "توضیحات",
            'date': "تاریخ آزمون",
        }

class TOEFLForm(forms.ModelForm):
    class Meta:
        model =TOEFLForm
        fields = ['name', 'password', 'kind', 'number',  'city' , 'country', 'center', 'placecode', 'education', 'citizen', 'major', 'majorcode', 'explanation', 'date', 'reason', 'destination' ]
        labels ={
            'name': "نام کاربری",
            'password': "رمز عبور",
            'kind':"نوع هویت",
            'number':"شماره ی هویت",
            'city': 'شهر',
            'country': "کشور",
            'center': "مرکز محل آزمون",
            'placecode': "کد محل آزمون",
            'education': "وضعیت تحصیلی",
            'citizen': "وضعیت شهروندی",
            'major': "نام رشته",
            'majorcode': "کد رشته",
            'explanation': "توضیحات",
            'date': "تاریخ آزمون",
            'reason':"دلیل شرکت در آزمون",
            'destination':"کشور مقصد تحصیل",
        }
    
class IELTSForm(forms.ModelForm):
    class Meta:
        model =IELTSForm
        fields = ['name', 'password',  'arzi' , 'kind', 'site']
        labels ={
            'name': "نام کاربری",
            'password': "رمز عبور",
            'arzi': 'مبلغ ارزی',
            'kind': "نوع ارز",
            'site': "لینک سایت ثبت نام",
        }  
