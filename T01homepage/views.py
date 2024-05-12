from django.shortcuts import render

# Create your views here.
def homepage(requests):
    data={'askForEmail': True}
    return render(requests,'homepage/main.html',data)


