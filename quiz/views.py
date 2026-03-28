from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Test, Quiz, TestAttempt

# Create your views here.

@login_required
def quiz_home(request):
    today = timezone.now().date()
    today_test = Test.objects.filter(date=today).first()
    attempt = None
    already_attempted = False
    if today_test:
        try:
            attempt = TestAttempt.objects.get(user=request.user, test=today_test)
            already_attempted = True
        except TestAttempt.DoesNotExist:
            pass
    return render(request, 'quizhome.html', {
        'test': today_test,
        'already_attempted': already_attempted,
        'attempt': attempt,
    })

@login_required(login_url='login')
def start_test(request, test_uuid):
    """Renders the test form and processes submission."""
    test = get_object_or_404(Test, uuid=test_uuid)
    today = timezone.now().date()

    # Validate test availability
    if test.date != today:
        messages.error(request, "This test is not available today.")
        return redirect('quiz_home')
    if TestAttempt.objects.filter(user=request.user, test=test).exists():
        messages.error(request, "You have already taken this test.")
        return redirect('quiz_home')

    # Fetch all questions from the test's categories
    questions = Quiz.objects.filter(quiz_category__subject__in=['Reasoning', 'Aptitude'])

    if request.method == 'POST':
        # Calculate score
        total = questions.count()
        score = 0
        for question in questions:
            selected = request.POST.get(f'q_{question.id}')
            if selected and int(selected) == question.correct_option:
                score += 1

        # Save attempt (only counts, no answer details)
        TestAttempt.objects.create(
            user=request.user,
            test=test,
            total_questions=total,
            correct_answers=score
        )
        return render(request, 'test_result.html', {
            'test': test,
            'score': score,
            'total': total,
        })

    # GET: display form
    return render(request, 'test_form.html', {
        'test': test,
        'questions': questions,
    })