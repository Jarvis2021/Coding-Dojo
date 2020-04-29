from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("Displays list of all blogs")

def create(request):
    return redirect("/")

def show(request,id):
    return HttpResponse(f"Placeholder to display blog:{id}")

def edit(request,id):
    return HttpResponse(f"Placeholder to edit blog {id}")

def destroy(request,id):
    return redirect("/")
