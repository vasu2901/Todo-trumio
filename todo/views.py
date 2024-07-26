from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Todo
from datetime import datetime


def index(req):
    return HttpResponse("Hello World")

def create_todo(req, res):
    user0 = User.objects.get(name=req.name)
    if(user0):
        newtodo = Todo.objects.create(
            title = req.title,
            user_id = user0,
            timestamp = datetime.now(),
            status = True
        )   
        newtodo.save()
        return HttpResponse(newtodo)
    else:
        user0 = User.objects.create(name = req.name)
        user0.save()
        newtodo = Todo.objects.create(
            title = req.title,
            user_id = user0,
            timestamp = datetime.now(),
            status = True
        )   
        newtodo.save()

def update_todo(req):
    todo = Todo.objects.filter(title=req.title)
    todo.status = False
    todo.save()
    return HttpResponse(todo)

def delete_todo(req):
    todo = Todo.objects.filter(title=req.title)
    todo.delete()
    return HttpResponse("deleted")
