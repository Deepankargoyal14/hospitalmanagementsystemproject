# in this file we can create some python functions that makes a web request and returns a web response.
# this response can be a html contents of a webpage, or a redirect or a 404 erroe(not found), or an xml documents or anything else
# each view function takes http request as its first parameter.
#render is the shortcut function to return the given template.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,Group
from hospital.models import Patient,LoginTable
from rest_framework import status
from rest_framework.decorators import api_view

from hospital.hospitalserializer import SignupSerializer,LoginTableSerializer




# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def aboutpage(request):
    return render(request,'about.html')


def createaccountpage(request):
    return render(request,'createaccountpage.html')

def loginpage(request):
    return render(request,'loginpage.html')

# def createuser(request):
#     error = ""
#     user = "none"
#     if request.method == 'POST':
#         Patientname = request.POST['patientname']
#         email = request.POST['email']
#         password = request.POST['psw']
#         repeatpassword = request.POST['psw-repeat']
#         gender = request.POST['gender']
#         phonenumber = request.POST['phoneno']
#         address = request.POST['address']
#         birthdate = request.POST['dob']
#         bloodgroup = request.POST['bg']
#         try:
#             if password == repeatpassword:
#                 Patient.objects.create(name=Patientname, email=email, password=password, gender=gender,
#                                        phonenumber=phonenumber, address=address, birthdate=birthdate,
#                                        bloodgroup=bloodgroup)
#                 user = User.objects.create_user(first_name=Patientname, email=email, password=password, username=email)
#                 pat_group = Group.objects.get(name='Patient')
#                 pat_group.user_set.add(user)
#                 # print(pat_group)
#                 user.save()
#                 return HttpResponse("secsesfully signup")
#                 # print(user)
#                 error = "no"
#             else:
#                 error = "yes"
#         except Exception as e:
#             error = "yes"
#         # print("Error:",e)
#     d = {'error': error}
#     # print(error)
#
#     return render(request, 'createaccountpage.html', d)
#     # return render(request,'createaccountpage.html')



# def createuser(request):
#     data2=request.POST
#     if request.method == 'POST':
#         Patientname = request.POST['patientname']
#         email = request.POST['email']
#         password = request.POST['psw']
#         repeatpassword = request.POST['psw-repeat']
#         gender = request.POST['gender']
#         phonenumber = request.POST['phoneno']
#         address = request.POST['address']
#         birthdate = request.POST['dob']
#         bloodgroup = request.POST['bg']
#     dict2={}
#     for ele in data2:
#         if ele!="csrfmiddlewaretoken":
#             print(ele)
#
#
#     return JsonResponse(data2)

@api_view(['GET','POST'])
def createuser(request):
    if request.POST['password']==request.POST['psw-repeat']:
        data1=SignupSerializer(data=request.data)
        # return HttpResponse('Somthing Went Wrong')
        if data1.is_valid():
            data1.save()
            return HttpResponse("You are Register succesfully ")
            # return render(request, 'loginpage.html')
        else:
            return HttpResponse('Somthing Went Wrong')
        # return JsonResponse(data1.data,status=status.HTTP_201_CREATED)


    else:
        return HttpResponse('Password didnot match')

@api_view(['GET','POST'])
def login(request):
    print(request.data)
    # print(request.GET["session"])
    # data1=LoginSerializer(data=request.data)

    entemail = request.data["email"]
    entpswd = request.data["password"]
    data3=Patient.objects.filter(email=entemail)
    # if Patient.objects.filter(email=entemail):
    if data3:
        # emdt = Patient.objects.get(email=entemail)

        # if emdt.password == entpswd:
        if data3[0].password == entpswd:
            # enter data in LoginTable for help in logut in continue session
            data1 = LoginTableSerializer(data=request.data)
            if data1.is_valid():
                data1.save()

            # return HttpResponse("login successfully")
            return render(request,"patienthome.html")
        else:
            return HttpResponse("entered password is wrong")
    else:
        return HttpResponse("email not register")

    # return HttpResponse('datamatch')

@api_view(['GET','POST'])
def Logout(request):
    print(request.data)
    # return render(request, 'loginpage.html')
    return redirect('loginpage')