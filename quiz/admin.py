from django.contrib import admin
from .models import Test, TestAttempt, Quiz, QuizCategory

# Register your models here.
admin.site.register(TestAttempt)
admin.site.register(Test)
admin.site.register(QuizCategory)
admin.site.register(Quiz)