from django.shortcuts import render

# Create your views here.
def homepage(request):
    # print('user is : ' ,request.user.is_authenticated)
    # p = request.user.is_authenticated
    # if p :
    return render(request, 'home/home.html')
