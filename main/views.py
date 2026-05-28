from django.db import models
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Post, MarketplaceSite, ContactMessage

# 1. Home Page View
def home(request):
    return render(request, 'main/home.html')

# 2. About Us View
def about(request):
    return render(request, 'main/about.html')

# 3. Privacy Policy View
def privacy(request):
    return render(request, 'main/privacy.html')

# 4. Blog List View
def blog_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'main/blog_list.html', {'posts': posts})

# 5. Single Blog Post View
def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'main/blog_detail.html', {'post': post})

# 6. Marketplace Table View
def marketplace(request):
    sites = MarketplaceSite.objects.all()
    return render(request, 'main/marketplace.html', {'sites': sites})

# 7. Contact Form Submission View
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # ڈیٹا بیس میں سیو کرنا
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        
        # کامیابی کا میسج دکھانا
        messages.success(request, "Your message has been sent successfully!")
        
    return render(request, 'main/contact.html')
def marketplace(request):
    query = request.GET.get('q') # سرچ بار سے لفظ لینا
    if query:
        # نام یا کیٹیگری میں تلاش کرنا
        sites = MarketplaceSite.objects.filter(
            models.Q(domain_name__icontains=query) | 
            models.Q(category__icontains=query)
        )
    else:
        sites = MarketplaceSite.objects.all()
    
    return render(request, 'main/marketplace.html', {'sites': sites, 'query': query})