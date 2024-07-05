from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
class MessageList(ListView):
    model = Message
    ordering = ['-id']     
class MessageView(DetailView):
    model = Message
class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content']    
    success_url = reverse_lazy('msg_list')  
class MessageDelete(DeleteView):
    model = Message
    success_url = '/message/'