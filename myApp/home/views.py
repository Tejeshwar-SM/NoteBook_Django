from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
### Class based views ->
class HomeView(TemplateView):
    template_name = 'home/welcome.html'

# def home(request):
#     # return HttpResponse('Hello, World!')
#     return render(request, 'home/welcome.html', {'today': datetime.today()})

class AuthorizationViews(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})