from django.db import models

# Create your models here.
# simliar to polls model
class Ticket(models.Model):
    """
    A model representing a ticket for an event.

    Attributes:
        name (str): The name of the ticket holder.
        email (str): The email address of the ticket holder.
        phone (str): The phone number of the ticket holder.
        date (datetime.date): The date of the event the ticket is for.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Question(models.Model):
    """
    A model representing a question for a poll.

    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime.datetime): The date and time the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    """
    A model representing a choice for a poll question.

    Attributes:
        question (Question): The question this choice belongs to.
        choice_text (str): The text of the choice.
        votes (int): The number of votes this choice has received.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text