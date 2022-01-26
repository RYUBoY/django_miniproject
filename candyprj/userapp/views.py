from django.shortcuts import render

# Create your views here.
from audioop import reverse
from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
def signup(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        birth = request.POST.get('birth')
        mail = request.POST.get('mail')
        m = User(id=id, pw=pw, name=name, birth=birth, mail=mail)

        m.save()
        return HttpResponse(
            '가입 완료<br>%s %s %s %s %s ' % (id, pw, name, birth, mail))
    else:
        return render(request, 'userapp/signup.html')

def profile(request):
    profile = User.objects.get(id = 'abc')
    return render(request, 'userapp/profile.html',{'profile':profile})



def update(request):
    update = User.objects.get(id= 'abc')
    if request.method == "POST":
        
        update.pw = request.POST.get('pw')
        update.name = request.POST.get('name')
        update.birth = request.POST.get('birth')
        update.mail = request.POST.get('mail')
       
        update.save()
        # return HttpResponseRedirect(reverse('profile'))
        return render(request, 'userapp/profile.html')

    else:
        update = User
        return render(request, 'userapp/update.html', {'update':update})



def login(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        try:
            m = User.objects.get(id=id, pw=pw)
        except User.DoesNotExist as e:
            return HttpResponse('로그인 실패')
        else:
            request.session['id'] = m.id
            request.session['name'] = m.name
            

        # return render(request,'boardapp/main.html')
        return redirect('../../board/main')
    else:
        return render(request, 'userapp/login.html')

def logout(request):
    # del request.session['id'] # 개별 삭제
    # del request.session['name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    # return render(request,'boardapp/main.html')
    return redirect('../../board/main')

# def profile(request):
#     id = request.session.get('id')
#     profile = User.objects.get(id = id)
#     return render(request, 'userapp/profile.html',{'profile':profile})