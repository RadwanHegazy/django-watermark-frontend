from django.shortcuts import redirect

def LogoutView (request) : 
    response = redirect('home')
    response.delete_cookie('user')
    return response