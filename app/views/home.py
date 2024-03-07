from django.shortcuts import render, redirect
from globals.request_manager import Action
from front_end.settings import MAIN_URL
from globals.decorators import login_required

@login_required
def HomeView (request) : 
    context = {}
    user = request.COOKIES.get('user',None)
    headers = {'Authorization':f"Bearer {user}"}
    action = Action(
        headers=headers,
        url=MAIN_URL + '/watermark/get/'
    )

    action.get()
    
    context['files'] = action.json_data()

    return render(request,'home.html',context)