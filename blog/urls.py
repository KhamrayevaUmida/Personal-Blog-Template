from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('about/', AboutView.as_view()),
    path('category/', CategoryView.as_view()),
    path('contact/', ContactView.as_view()),
    path('index2/', Index2View.as_view()),
    path('postDetails/', PostDetailsView.as_view()),
    path('privacy/', PrivacyView.as_view()),
]
