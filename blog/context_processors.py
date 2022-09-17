from jobs.models import Category

def index(request):
    return {
        'categories': Category.objects.all(),
        }