from django.shortcuts import render, redirect
from globals.request_manager import Action
from front_end.settings import MAIN_URL

def LoginView (request) : 
    context = {}

    if request.method == "POST" : 
        action = Action(
            url = MAIN_URL + "/user/login/",
            data = {
                "email" : request.POST.get('email',None),
                "password" : request.POST.get('password',None),
            }
        )

        action.post()

        if action.is_valid() : 
            respones = redirect('home')
            respones.set_cookie('user',action.json_data()['access'])
            return respones
        context['error'] = 'البيانات غير صحيحة'

    return render(request,'login.html',context)