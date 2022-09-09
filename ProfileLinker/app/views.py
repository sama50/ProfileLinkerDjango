from django.shortcuts import render , redirect ,HttpResponseRedirect
from app.forms import uploadimg , AddLink
from app.models import Details , LinkData , ShareDetails
from django.contrib.auth import logout
import uuid
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        fm = uploadimg()
        detailsfm  = AddLink()
        imgdata = None
        linkdata = None
        # print(Details.objects.exists(user=request.user))
        # if Details.objects.check(user=request.user):
        #     imgdata = Details.objects.get(user=request.user)
        #     linkdata = LinkData.objects.filter(user=request.user)
        try:
            imgdata = Details.objects.get(user=request.user)
            linkdata = LinkData.objects.filter(user=request.user)
        except:
            pass
        return render(request,'index.html',{'fm':fm,'detailsfm':detailsfm,'imgdata':imgdata,'linkdata':linkdata})
    else:
        return HttpResponseRedirect('/login/')

def uploadurl(request):
    if request.method == 'POST':
        fm = uploadimg(request.POST,request.FILES)
        
        if fm.is_valid():
            name = fm.cleaned_data['name']
            eduaction = fm.cleaned_data['Education']
            email = fm.cleaned_data['email']
            image = fm.cleaned_data['image']
            f = Details(user=request.user,name=name,Education=eduaction,email=email,image=image)
            f.save()
    return redirect('/')

def addsocialLink(request):
    print("***********")

    if request.method == 'POST':
        detailsfm = AddLink(request.POST)
        if detailsfm.is_valid():
            namelink = detailsfm.cleaned_data['nameLink']
            link = detailsfm.cleaned_data['link']
            f = LinkData(user=request.user,nameLink=namelink,link=link)
            f.save()
    return redirect('/')

def DeletebyId(request,id):
    if request.method == 'POST':
        d = LinkData.objects.get(id=id)
        d.delete()

    return redirect('/')

def logoutby(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def profileget(request):
    
    # detailuser = Details.objects.get(user=name)
    myid = None
    try:
        myid = ShareDetails.objects.get(user=request.user).nameid
    except:
        randomid = uuid.uuid4()
        f = ShareDetails(user=request.user,nameid=randomid)
        f.save()
        get = ShareDetails.objects.get(nameid=randomid)
        myid = randomid
    return redirect(str(myid)+'/')

def showprofile(request,id):
    print(id)
    oid = ShareDetails.objects.get(nameid=id)
    print(oid.user)
    data = Details.objects.get(user=oid.user)
    linkdata = LinkData.objects.filter(user=oid.user)
    return render(request, 'profile.html',{'data':data,'linkdata':linkdata})