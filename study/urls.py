from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('students', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls))


    # # path('students', views.StudentView), # FBV
    # path('students', views.StudentView.as_view()),  # CBV
    # # path('students/<int:pk>', views.StudentDetailView), # FBV
    # path('students/<int:pk>', views.StudentDetailView.as_view()),  # CBV

    # # path('score', views.score_view), # FBV
    # path('score', views.ScoreView.as_view()),  # CBV
    # # path('score/<int:pk>', views.score_detail_view), # FBV
    # path('score/<int:pk>', views.ScoreDetailView.as_view()),  # CBV

    # path('students/<int:pk>/score', views.StudentScoreView),
]
