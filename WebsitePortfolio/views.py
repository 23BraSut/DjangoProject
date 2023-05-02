from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from datetime import datetime
from django.core.exceptions import ValidationError
# https://stackoverflow.com/questions/71328869/whats-gettext-lazy-on-django-is-for
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from .models import Question, Choice
from django.http import HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
@login_required
def index(request):
   return render(request, "index.html")

def book_tickets(request):
    return render(request, "book_ticket.html")

def submit_ticket(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValidationError(_('Invalid date format. Enter the date in YYYY-MM-DD format.'))

        # Creating a new instance
        ticket = Ticket.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date
        )


        # Redirect to inde when successful
        return redirect('index')

    return render(request, 'book_tickets.html')

def about(request):
    return render(request, 'about.html')

def photos(request):
    return render(request, 'photos.html')

def user_login(request):
    return render(request, 'login.html')
#same as the poll project
def authenticate_user(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  if user is None:
      return HttpResponseRedirect(
          reverse('login')
     )
  else:
    login(request, user)
    return HttpResponseRedirect(
      reverse('index')
  )


from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        
        # Check if any required fields are empty
        if not username or not password or not confirm_password:
            messages.error(request, "Please enter values for all required fields.")
            return redirect('register')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        
        # Create user object
        user = User.objects.create_user(username=username, password=password)
        
        # Save user to the database
        user.save()
        
        messages.success(request, "Account created successfully.")
        return redirect('index')
        
    #  render the register page with any error messages
    context = {'error_message': messages.get_messages(request)}
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# https://realpython.com/django-social-post-3/#:~:text=Django%20puts%20data%20in%20request,on%20your%20elements.
# https://stackoverflow.com/questions/63885614/how-to-save-user-input-in-database-from-django-form
@require_POST
def vote(request, question_id):
    choice_id = request.POST.get('choice')
    choice = get_object_or_404(Choice, id=choice_id)
    choice.votes += 1
    choice.save()
    return redirect('results', question_id=question_id)

@login_required
def home(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
