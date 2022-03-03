from django.urls import path
from .views import GetFeedbackView, SuccessView, ShowTeachersView

urlpatterns = [
    path('', GetFeedbackView.as_view(), name='GetFeedbackView'),
    path('success/', SuccessView.as_view(), name='SuccessView'),
    path('teachers', ShowTeachersView.as_view(), name='ShowTeachersView'),

]
