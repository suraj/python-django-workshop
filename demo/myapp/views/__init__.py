from django.shortcuts import render
from django.views.generic import TemplateView, ListView, \
            DetailView, UpdateView, CreateView

from django.shortcuts import render_to_response
from django.http import HttpResponse

from myapp.models import Student
from myapp.forms import AddStudentForm

# Create your views here.

class LandingPage(TemplateView):
    template_name = "landing.html"


def defaultLandingPage(request, **kwargs):
    return render_to_response("landing.html")

# def defaultLandingPage(request, **kwargs):
#     return HttpResponse("<h1>Welcome!</h1>"


class AddStudent(CreateView):
    model = Student
    template_name = "add.html"
    success_url = "/"

    form_class = AddStudentForm

