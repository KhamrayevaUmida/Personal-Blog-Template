from django.shortcuts import render
from .models import Post
from .models import TopPost
from django.views.generic import TemplateView

def main(request):
    posts = Post.objects.all()
    tposts = TopPost.objects.all()
    context = {
        'posts': posts,
        'tposts': tposts,
    }
    return render(request, 'index.html', context)

class AboutView(TemplateView):
    template_name = "about.html"

class CategoryView(TemplateView):
    template_name = "category.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class Index2View(TemplateView):
    template_name = "index-2.html"

class PostDetailsView(TemplateView):
    template_name = "post-details.html"

class PrivacyView(TemplateView):
    template_name = "privacy.html"
