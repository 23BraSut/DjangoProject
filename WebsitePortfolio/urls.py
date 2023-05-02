from django.urls import path
from . import views
from .views import submit_ticket

urlpatterns = [
    # https://www.programink.com/django-tutorial/django-urls-views.html
    path('', views.index, name='index'),
    path('book-tickets/', views.book_tickets, name='book_tickets'),
    path('submit-ticket/', submit_ticket, name='submit_ticket'),
    path('about/', views.about, name='about'),
    path('photos/', views.photos, name='photos'),
    path('login/', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    path('home/', views.home, name='home'), # changed the URL path and view name
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
