from django.shortcuts import render, get_object_or_404, redirect
from .models import Review

def reviews_page(request):
    reviews = Review.objects.all()
    return render(request, 'app_reviews/reviews_page.html', {'reviews': reviews})

def like_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.likes += 1
    review.save()
    # Redirect back to the page the user was on, or a default page
    return redirect(request.META.get('HTTP_REFERER', 'app_reviews:reviews_page'))