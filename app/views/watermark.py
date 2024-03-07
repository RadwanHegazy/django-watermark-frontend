from django.shortcuts import render, redirect
from globals.request_manager import Action
from front_end.settings import MAIN_URL
from globals.decorators import login_required



@login_required
def WatermarkView (request) : 
    context = {}
    
    if request.method == "POST" :
        user = request.COOKIES.get('user',None)
        headers = {'Authorization':f"Bearer {user}"}

        def get(name) : 
            return request.POST.get(name,None)
    
        action = Action(
            headers=headers,
            url=MAIN_URL + '/watermark/create/',
            data={
                'text': get('text'),
                'type': get('type'),
            }
        )

        action.files = {
            'original' : request.FILES.get('original',None)
        }

        action.post()

        if action.is_valid() : 
            context['msg'] = 'جاري اضافة العلامة المائية'
        else:
            context['msg'] = 'يوجد خطأ اثناء بدأ العملية'

    return render(request,'add_watermark.html',context)