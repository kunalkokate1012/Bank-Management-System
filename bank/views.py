from django.shortcuts import render,redirect
from .models import User,Transiction
from django.db import connection
import datetime
# Create your views here.
def index(request):
    return render(request,'bank/index.html')
def transiction(request):
    user=User.objects.raw('select * from bank_user')
    return render(request,'bank/transiction.html',{'user':user})
def make_transiction(request,id):
    a=User.objects.raw('select * from bank_user where id=%s',[id])
    users = User.objects.raw('select * from bank_user where not id=%s',[id])
    all={'a':a[0],'users':users}
    ammount=request.POST.get('ammount',0)
    total1=a[0].balance-int(ammount)
    to_id=request.POST.get('reciver',1)
    print(ammount)
    print(to_id)
    b=User.objects.raw('select * from bank_user where id=%s',[to_id])
    if len(b) !=0 and ammount!=0:
        total2=b[0].balance+int(ammount)
        if(a[0].balance>=int(ammount)):
            m = User.objects.get(id=id)
            m.balance = total1
            m.save()
            n = User.objects.get(id=to_id)
            n.balance =total2
            n.save()
            date=datetime.date.today()
            with connection.cursor() as cursor:
                cursor.execute("insert into bank_transiction(from_user,to_user,ammount,date) values(%s,%s,%s,%s)",[a[0].name, b[0].name, int(ammount),date])
        else:
            return redirect('/bank/')
    return render(request,'bank/make_transiction.html',all)
def transiction_history(reuest):
    users=User.objects.raw('select * from bank_transiction')
    {'user': users}
    return render(reuest,'bank/transiction_history.html', {'user':users})
def create_user(reuest):
    name=reuest.POST.get('name',"")
    email = reuest.POST.get('email',"")
    balance = reuest.POST.get('amount',0)
    if name !="":
        with connection.cursor() as cursor:
            cursor.execute("insert into bank_user(name,email,balance) values(%s,%s,%s)",[name,email,balance])
    return render(reuest,'bank/create_user.html')
