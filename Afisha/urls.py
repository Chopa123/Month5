from django.contrib import admin
from django.urls import path , include
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.DirectorListApiView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailApiView.as_view()),
    path('api/v1/movies/', views.MovieListApiView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailApiView.as_view()),
    path('api/v1/reviews/', views.ReviewListApiView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailApiView.as_view()),
    path('api/v1/movies/reviews/', views.MovieReviewApiView.as_view()),
    path('api/v1/users/' , include('users.urls'))
]
