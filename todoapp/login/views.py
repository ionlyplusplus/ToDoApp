from django.shortcuts import render

# Create your views here.
def loginn(request):
    if request.method == 'POST':
        datauser = json.loads()
