from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest,JsonResponse
from django.db import IntegrityError
from django.contrib import messages
from django.core.exceptions import MultipleObjectsReturned
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import User,UserRequest,Create

# Create your views here.

def index(request):
    status_true = UserRequest.objects.filter(RequestStatus = True)
    paginator = Paginator(status_true,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'earth/index.html',{'status_true':page_obj})

def profile(request,name):
    if request.user.is_authenticated:
        try:
            user_page = User.objects.get(username = name)
            status_true = UserRequest.objects.filter(RequestStatus = True).order_by('-id')
            status_false = UserRequest.objects.filter(RequestStatus = False)
            checkuserrequest = UserRequest.objects.filter(Username=request.user).exists()
            if request.method == 'POST':
                if UserRequest.objects.filter(Username=request.user).exists():
                    messages.info(request,'you already have a request')
                else:
                    Username = request.user
                    About =  request.POST['about']
                    Title =  request.POST['title']
                    Goal =  request.POST['goal']
                    ProofPic1 = request.FILES['image1']
                    usersrequest = UserRequest.objects.create(Username = Username,About=About,ProofPic1=ProofPic1,Title=Title,Goal=Goal)
                    usersrequest.save()
                    return HttpResponseRedirect(reverse('profile',args=[request.user]))
        except User.DoesNotExist:
            return HttpResponseRedirect(reverse('not_found'))
        
        if 'deletefundraise' in request.POST:
            UserRequest.objects.get(Username = request.user).delete()
            return HttpResponseRedirect(reverse('profile', args=[request.user]))
    else:
        return HttpResponseRedirect(reverse('login'))
    return render(request,'earth/userprofile.html',{'user_page':user_page,'status_false':status_false,'status_true':status_true,'checkuserrequest':checkuserrequest})

def authrequest(request,id):
    try:
        statusrequest = UserRequest.objects.get(pk = id)
        if 'confirm' in request.POST:
            UserRequest.objects.filter(pk = id).update(RequestStatus = True)
            return HttpResponseRedirect(reverse('profile',args=[request.user]))
    except UserRequest.DoesNotExist:
        return HttpResponseRedirect(reverse('not_found'))
    return render(request,'earth/authrequest.html',{'statusrequest':statusrequest})

def requestpage(request,rid):
    if request.user.is_authenticated:
        requestdetails = UserRequest.objects.get(pk = rid)
        width = requestdetails.Donation * 100/requestdetails.Goal
    else:
        return HttpResponseRedirect(reverse('login'))
    return render(request,'earth/requestpage.html',{'requestdetails':requestdetails,'width':width}) 

def donate_material(request,benefactor_id):
    benefactor_name =  UserRequest.objects.get(pk = benefactor_id)
    try:
        if request.method == 'POST':
            Title = request.POST['title']
            Description =  request.POST['description']
            ItemImage = request.FILES['itemimage']
            Owner = request.user
            Amount = request.POST['amount']
            Benefactor = benefactor_name.Username
            if ItemImage != "":
                donate = Create.objects.create(Title = Title,Description = Description,ItemImage = ItemImage,Owner=Owner,Amount = Amount,Benefactor = Benefactor)
                donate.save()
                return HttpResponseRedirect(reverse('commerce'))
            else:
                messages.info(request,'Uplaod item image')
    except:
        messages.info(request,'Uplaod item image')
    return render(request,'earth/donate_material.html',{'benefactor_name':benefactor_name})

def commerce(request):
    items = Create.objects.all()
    return render(request,'earth/e-commerce.html',{'items':items}) 

def product(request,itemid):
    try:
        item = Create.objects.get(pk=itemid)
    except Create.DoesNotExist:
        return HttpResponseRedirect(reverse('not_found'))
    return render(request,'earth/product.html',{'item':item})
    
def purchase(request,purchaseid):
    try:
        purchaseitem = Create.objects.get(pk=purchaseid)
        donation_name =  UserRequest.objects.get(Username=purchaseitem.Benefactor)
        shipping = 1000
        VAT = 400
        Total = shipping + VAT + purchaseitem.Amount
        if request.method == 'POST':
            purchase_amount = purchaseitem.Amount
            newamount = donation_name.Donation + purchase_amount
            UserRequest.objects.filter(Username = purchaseitem.Benefactor).update(Donation = newamount) 
            Create.objects.get(pk=purchaseid).delete()
            messages.info(request,'Thank you for shopping with us')
            return HttpResponseRedirect(reverse('commerce'))  
    except Create.DoesNotExist:
        return HttpResponseRedirect(reverse('not_found'))
    return render(request,'earth/purchase.html',{'purchaseitem':purchaseitem,'j':donation_name.Username,'shipping':shipping,'VAT':VAT,'Total':Total})

def payment(request,paymentid):
    userrequest_pay = UserRequest.objects.get(pk = paymentid)
    if request.method == 'POST':
        amount = request.POST['amount']
        if amount != "":
            amount_paid = int(amount)
            currentamount = userrequest_pay.Donation
            new_amount = currentamount + amount_paid
            UserRequest.objects.filter(pk = paymentid).update(Donation = new_amount)
            messages.info(request,f'Thank you for supporting {userrequest_pay.Username}')
            return HttpResponseRedirect(reverse('profile' ,args=[request.user]))
        else:
            messages.info(request,'pls enter amount')
    return render(request,'earth/Payment.html',{'userrequest_pay':userrequest_pay})

def not_found(request):
    return render(request,'earth/404.html')



@csrf_exempt
def receiver(request,receivername):
    try:
        requestprogress = UserRequest.objects.get(Username=request.user)
        return JsonResponse({'status':0,'amount':requestprogress.Donation})
    except UserRequest.DoesNotExist:
        return JsonResponse({'status':1,'amount':'Please first make a request'})


# authentication views
# register view
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['firstname']
        password = request.POST['password']
        confirmp = request.POST['password2']
        email = request.POST['email']
        UserType = request.POST['usertype']
        if confirmp == password:
            if first_name == "":
                messages.info(request,'Firstname is compulsory')
            else:
                try:
                    user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, password = password, email = email ,UserType = UserType)
                    user.save()
                    login(request,user)
                    return HttpResponseRedirect(reverse('profile',args=[request.user]))
                except IntegrityError:
                    messages.info(request,'username is already taken')
        else:
            messages.info(request,'passwords do not match')
        

    return render(request,'earth/register.html')

# login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(f"UserProfile/{request.user}")
        else:
            messages.info(request,'credentials invalid')
    return render(request,'earth/login.html')

# logoutview
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))