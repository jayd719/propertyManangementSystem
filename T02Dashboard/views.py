from django.shortcuts import render,HttpResponse
from .apps import toggleButton

# def dashhome(request):
#     return render(request,'dashboard/dashboard.html')
def dashhome(request):
    if request.method=="POST":
        username = request.POST["status"]
    return render(request,'dashboard/appHome.html')

def clicked(request):
    status = request.POST.get('status')
    toggleButton(status)
    return HttpResponse("success")