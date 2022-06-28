from django.shortcuts import render, redirect
from .models import Portfolio, Contact
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def portfolio(request):
	if request.method=="POST":
		contact=Contact()
		name=request.POST.get('name')
		phone=request.POST.get('phone')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		message=request.POST.get('message')
		contact.name=name
		contact.phone=phone
		contact.email=email
		contact.subject=subject
		contact.message=message
		contact.save()
		messages.success(request, 'Thank you for contacting me.')
		return redirect('/')


	items=Portfolio.objects.all()
	return render(request, 'portfolio.html', {'items': items})
