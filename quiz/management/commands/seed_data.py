# quiz/management/commands/seed_data.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from quiz.models import QuizCategory, Quiz, Test

class Command(BaseCommand):
    help = 'Seed initial data for the quiz app'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        
        # Create categories
        categories = ['Aptitude', 'Reasoning']
        for cat_name in categories:
            obj, created = QuizCategory.objects.get_or_create(subject=cat_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {cat_name}'))
            else:
                self.stdout.write(f'Category already exists: {cat_name}')
        
        # Get category objects
        aptitude = QuizCategory.objects.get(subject='Aptitude')
        reasoning = QuizCategory.objects.get(subject='Reasoning')
        
        # Aptitude questions
        aptitude_questions = [
            {
                'question': 'What is 15 + 7?',
                'option1': '20',
                'option2': '21',
                'option3': '22',
                'option4': '23',
                'correct_option': 3
            },
            {
                'question': 'If a train travels 60 km in 1 hour, how far will it travel in 2.5 hours?',
                'option1': '120 km',
                'option2': '150 km',
                'option3': '180 km',
                'option4': '200 km',
                'correct_option': 2
            },
            {
                'question': 'What is the square root of 144?',
                'option1': '10',
                'option2': '11',
                'option3': '12',
                'option4': '13',
                'correct_option': 3
            }
        ]
        
        for q in aptitude_questions:
            obj, created = Quiz.objects.get_or_create(
                quiz_category=aptitude,
                question=q['question'],
                defaults={
                    'option1': q['option1'],
                    'option2': q['option2'],
                    'option3': q['option3'],
                    'option4': q['option4'],
                    'correct_option': q['correct_option']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Aptitude question: {q["question"][:30]}...'))
            else:
                self.stdout.write(f'Aptitude question already exists: {q["question"][:30]}...')
        
        # Reasoning questions
        reasoning_questions = [
            {
                'question': 'If all Bloops are Razzies and all Razzies are Lazzies, then all Bloops are Lazzies. This is an example of:',
                'option1': 'Deductive reasoning',
                'option2': 'Inductive reasoning',
                'option3': 'Abductive reasoning',
                'option4': 'Analogical reasoning',
                'correct_option': 1
            },
            {
                'question': 'Complete the series: 2, 4, 8, 16, ?',
                'option1': '24',
                'option2': '32',
                'option3': '30',
                'option4': '28',
                'correct_option': 2
            },
            {
                'question': 'If "MADAM" is written as "NBNBN", then "CIVIC" is written as?',
                'option1': 'DJDJD',
                'option2': 'DJBJB',
                'option3': 'DJDKB',
                'option4': 'DJWJC',
                'correct_option': 1
            }
        ]
        
        for q in reasoning_questions:
            obj, created = Quiz.objects.get_or_create(
                quiz_category=reasoning,
                question=q['question'],
                defaults={
                    'option1': q['option1'],
                    'option2': q['option2'],
                    'option3': q['option3'],
                    'option4': q['option4'],
                    'correct_option': q['correct_option']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Reasoning question: {q["question"][:30]}...'))
            else:
                self.stdout.write(f'Reasoning question already exists: {q["question"][:30]}...')
        
        # Create a test for today's date if not exists
        today = timezone.now().date()
        test_title = "Daily Test"
        test_obj, created = Test.objects.get_or_create(
            date=today,
            defaults={'title': test_title}
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created test for today: {test_title}'))
        else:
            self.stdout.write(f'Test for today already exists: {test_obj.title}')
        
        self.stdout.write(self.style.SUCCESS('Seeding completed.'))