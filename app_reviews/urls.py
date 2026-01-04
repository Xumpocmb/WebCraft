from django.urls import path
from . import views

app_name = 'app_reviews'

urlpatterns = [
    path('', views.reviews_page, name='reviews_page'),
    path('like/<int:review_id>/', views.like_review, name='like_review'),
]
