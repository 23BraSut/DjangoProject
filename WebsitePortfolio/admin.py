from django.contrib import admin
from .models import Ticket
from .models import Question, Choice

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Question)
admin.site.register(Choice)