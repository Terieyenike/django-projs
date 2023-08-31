from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello world!!!")


def about(request):
  return HttpResponse("Visit my page on https://iamteri.tech")


def hello(request, first_name):
  return HttpResponse(f"Hello {first_name}")


def calculate(request, num1, num2):
  return HttpResponse(f"The total is {num1+num2}")