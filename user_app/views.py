from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View
from .forms import UserCreationForm

class Register(View):
    template_name = 'registration/register.html'
    template_home = 'home.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password) # автоматич авторизация
            login(request, user)
            return render(request, self.template_home)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)