from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('/anna/')
    return response
