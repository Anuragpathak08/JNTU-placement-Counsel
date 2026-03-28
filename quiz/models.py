from django.db import models
from django.conf import settings
import uuid 

# Create your models here.
class QuizCategory(models.Model):
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.subject


class Quiz(models.Model):
    OPTION_CHOICES = [
        (1, "Option 1"),
        (2, "Option 2"),
        (3, "Option 3"),
        (4, "Option 4"),
    ]
    quiz_category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question = models.TextField(verbose_name='quiz questions')
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    correct_option = models.IntegerField(choices=OPTION_CHOICES)

class Test(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

class TestAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    total_questions = models.IntegerField()
    correct_answers = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.test}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'test'],
                name='unique_user_test_attempt'
            )
        ]



