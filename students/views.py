from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.views.generic import ListView,FormView,DeleteView,CreateView,UpdateView,View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
class StudnetView(ListView):
    model = StudentRecord
    template_name="./home.html"
    # def get(self, request):
    #     if request.GET.get("search") != "":
            
    #     return super().get(request)
    def get_queryset(self):
        search=self.request.GET.get("search","")
        return StudentRecord.objects.filter(name__icontains=search)
    
class StudentFormView(CreateView):
    template_name="./insert.html"
    model=StudentRecord
    fields="__all__"
    success_url ="/"
    # def form_valid(self,form):
    #     form.save()
    #     return super().form_valid(form)
class DeleteStudentView(DeleteView):
    model = StudentRecord
    success_url="/"
    template_name="./delete.html"
class EditStudentView(UpdateView):
    model=StudentRecord
    fields="__all__"
    success_url="/"
    template_name="insert.html"
class LoginStudentView(FormView):
    template_name="./login.html"
    form_class=AuthenticationForm
    success_url="/"
    def post(self,req):
        username=req.POST.get("username")
        password=req.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(req,user)
                return redirect("home")
            else:  
                return HttpResponse("inactivated")
        else:
            return HttpResponse("login cheeking is fail")
class LogoutView(View):
    def get(self,req):
        logout(req)
        return redirect("login")
class SingupView(CreateView):
    model=User
    fields=["username","first_name","last_name","email","password"]
    template_name="singup.html"
    success_url="/login-student/"
    def form_valid(self,form):
        user =form.save(commit=False)
        user.password=make_password(user.password)
        user.save()
        return  super().form_valid(form)