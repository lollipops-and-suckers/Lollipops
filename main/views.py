from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate
	)

from django.views import generic


from . forms import ContactForm, Notification

def index(request):
	form = ContactForm()
	# if request.method == "POST":
	# 	form = ContactForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	#       return redirect("{% url 'home' %}")
	if request.is_ajax():
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()			
			return JsonResponse({
                'msg': 'valid'
            })
		else:
			return JsonResponse({'msg': 'invalid'})

	return render(request, 'main/index.html', {'form': form, 'navbar': 'page1'})	
#class IndexView(generic.TemplateView):
# class IndexView(generic.FormView):
# 	template_name = "main/index.html"

# 	# def get_context_data(self, **kwargs):
# 	# 	context = super().get_context_data(**kwargs)
		
# 	# 	testimonials = Testimonial.objects.filter(is_active=True)
# 	# 	certificates = Certificate.objects.filter(is_active=True)
# 	# 	blogs = Blog.objects.filter(is_active=True)
# 	# 	portfolio = Portfolio.objects.filter(is_active=True)
		
# 	# 	context["testimonials"] = testimonials
# 	# 	context["certificates"] = certificates
# 	# 	context["blogs"] = blogs
# 	# 	context["portfolio"] = portfolio
# 	# 	return context
	
# 	form_class = ContactForm
# 	success_url = ("#contact")
	
# 	def form_valid(self, form):
# 		form.save()
# 		messages.success(self.request, 'Thank you. We will be in touch soon.')
# 		return super().form_valid(form)
	
# 	def form_invalid(self, form):
# 		messages.error(self.request, 'Something has gone wrong.')
# 		return super().form_invalid(form)

class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"