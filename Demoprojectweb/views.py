from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
'''def loginvalidate(request):
   a=request.POST.get("txt1")
    b=request.POST.get("pass1")
    print(a)
    print(b)
    if a=='user' and b=='userpw' :
        return render(request,'userhome.html')
    elif a=='anu' and b=='123' :
        return render(request,'userhome.html')
    else:
        return render(request,'login.html',{'errormsg':'invalid entry'})'''
import mysql.connector
def loginvalidate(request):
    a=request.GET.get("txt1")
    b=request.GET.get("pass1")
    #print(a)
   # print(b)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="textdb")
    mycursor=mydb.cursor()
    q="select * from demoweb where userid='"+a+"' and password='"+b+"';"
    #print(q)
    mycursor.execute(q)
    result=mycursor.fetchone()
    #print(result)
    mydb.close()
    if  result=="":
     return render(request,'login.html',{'errormsg':'invalid entry'})
    else:
        return render(request,'userhome.html')
        
     


