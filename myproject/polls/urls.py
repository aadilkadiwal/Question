from django.urls import path
from . import apiviews

urlpatterns = [
    path('questions/', apiviews.questions_view, name='question_view'),
    path('questions/<int:question_id>/', apiviews.question_detail_view, name='question_detail_view'),
    path('questions/<int:question_id>/choices/', apiviews.choices_view, name='choices_view'),
    path('questions/<int:question_id>/vote/', apiviews.vote_view, name='vote_view'),
    path('questions/<int:question_id>/result/', apiviews.question_result_view, name='question_result_view'),
    path('multiple-questions/', apiviews.multiple_question_view, name='multiple_question_view'),
]
