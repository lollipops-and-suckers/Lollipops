from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import (
		WebsiteContent
	)

from django.views import generic
from . forms import ContactForm, Notification

from django.core.mail import send_mail
from django.conf import settings

def index(request):
	form = None

	website_content = WebsiteContent.objects.get(pk=1) # If you know there is only one object that matches your query,
     
	if request.is_ajax():
		if (request.POST['tag'] == 'Notification'):
			form = Notification(request.POST)
		elif (request.POST['tag'] == 'contactForm'):
			form = ContactForm(request.POST)
		if form.is_valid():
			form.save()		
			if (request.POST['tag'] == 'contactForm'):
				name = request.POST['name']
				email = request.POST['email']
				message = request.POST['message']
				send_mail(f'Contact form - Lollipop from {name} @ {email}', message, 'settings.EMAIL_HOST_USER', ['nkosi7@msn.com'], fail_silently=False)
			return JsonResponse({
                'msg': 'valid'
            })
		else:
			print(form)
			return JsonResponse({'msg': 'invalid'})
		
	context = {
		'website_content': website_content,
	}

	return render(request, 'main/index.html', context)