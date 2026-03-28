from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from quiz.models import Test, TestAttempt

# Create your views here.

@staff_member_required
def dashboard_home(request):
    """Show results for today's test, or if no test today, list recent tests."""
    today = timezone.now().date()
    today_test = Test.objects.filter(date=today).first()

    if today_test:
        attempts = TestAttempt.objects.filter(test=today_test).select_related('user')
        return render(request, 'today_results.html', {
            'test': today_test,
            'attempts': attempts,
        })
    else:
        # Show list of all tests (or recent tests)
        tests = Test.objects.all().order_by('-date')
        return render(request, 'test_list.html', {
            'tests': tests,
        })

@staff_member_required
def test_results(request, test_id):
    """Show results for a specific test."""
    test = get_object_or_404(Test, id=test_id)
    attempts = TestAttempt.objects.filter(test=test).select_related('user')
    return render(request, 'test_results.html', {
        'test': test,
        'attempts': attempts,
    })