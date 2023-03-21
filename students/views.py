from django.shortcuts import render
from .models import *
from django.views.generic import ListView,FormView,DeleteView,CreateView,UpdateView
# from .forms import *
# def home(r):
#     data={
#         "student":StudentRecord.objects.all()
#     }
#     return render(r,"student_list.html",data)
class StudnetView(ListView):
    model = StudentRecord
    # template_name="./home.html"
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