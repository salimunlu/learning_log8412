from django.shortcuts import render

from .models import Topic


# Create your views here.
def index(request):
    """Home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
