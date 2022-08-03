from html.entities import name2codepoint
from django.shortcuts import render

# Create your views here.



def load_add_page(request):
    return render(request,'add.html')

def index(request):
    return render(request,'index.html')


def add_num(request):
    n1=int(request.GET['num1'])
    n2=int(request.GET['num2'])                                                                                                                                                                                                                                                                                                                                                                                                                        
    sum= n1+n2
    return render(request,'result.html',{'result':sum})


def cal(request):
    return render(request,'cal.html')    

def calc(request):
    c=''

    if request.method=='POST':
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        opr=request.POST.get('opr')

        if opr=="+":
            c=n1+n2
        elif opr=="-":
            c=n1-n2
        elif opr=="*":
            c=n1*n2
        elif opr=="/":
            c=n1/n2
    print(c)
    return render(request,"cal.html",{'result':c})                    

        