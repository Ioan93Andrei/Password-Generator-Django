from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.
def home(request):
  return render(request, "generator/home.html", {"password": "123456abc"})

def password(request):

  low_characters = list("qwertyuiopasdfghjklzxcvbnm")
  length = int(request.GET.get("length", 12))

  if request.GET.get("uppercase"):
    low_characters.extend(list("QWERTYUIOPASDFGHJKLZXCVBNM"))

  if request.GET.get("special"):
    low_characters.extend(list("!@#$%^&*?`()~"))

  if request.GET.get("numbers"):
    low_characters.extend(list("0123456789"))

  thepassword = ""

  for x in range(length):
    thepassword += random.choice(low_characters)

  return render(request, "generator/password.html", {"password": thepassword })
  