from django.urls import path
from . import apiviews

urlpatterns = [
    path('questions/', apiviews.questions_view, name='question_view'),
    path('questions/<int:question_id>/', apiviews.question_detail_view, name='question_detail_view'),
]
