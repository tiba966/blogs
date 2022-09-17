from django.db.models import F
from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.paginator import Paginator
from rest_framework import generics, permissions
from .models import Replay, Blog, Index, About 
from .serializers import (
    ReplaySerializer,
    CategorySerializer,
    IndexSerializer,
    
    AboutSerializer,
)
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .filters import BlogFilter
from django.core.paginator import Paginator
from django.utils.translation import get_language, activate

from django.core.mail import send_mail, EmailMessage


def reply(request):
    """Renders the create replay page."""
    assert isinstance(request, HttpRequest)
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer(queryset, many=True)

    return render(
        request,
        "reply.html",
        {
            "data": serializer_class.data,
        },
    )


def index(request):
    assert isinstance(request, HttpRequest)
    queryset = Index.objects.all()
    serializer_class = IndexSerializer(queryset, many=True)

    blogs = Blog.objects.all()

    # Show many contacts per page for stories
    paginator_story = Paginator(blogs, 10000000000000000)
    page_number_story = request.GET.get("page")
    page_obj_story = paginator_story.get_page(page_number_story)

    context = {
        "data": serializer_class.data,
        "blog": page_obj_story,
    }
    return render(request, "index.html", context)


def contact(request):
    about_image_bg = About.objects.all()

    if request.method == "POST":
        name = request.POST.get("full_name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject = request.POST.get("subject")
        data = {
            "name": name,
            "email": email,
      "subject": subject,

            "message": message,
        }
        print(data)

        message = '''
        Subject :{}
        New message :{}
        email :{}
        From: {}
        '''.format(
            data["subject"], data["message"], data["email"], data["name"]
        )

        if name and message and email and subject:
            try:
                send_mail(
                    data["name"],
                    message,
                    from_email="tabtickb@gmail.com",
                    recipient_list=["tabtickb@gmail.com"],
                    fail_silently=False,
                )

            except Exception as error:
                print("error")
                print(error)
                return HttpResponse("Invalid header found.")
    return render(
        request,
        "contact.html",
        {
            "about_image_bg": about_image_bg,
        },
    )


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
    finally:
        activate(cur_language)


def about(request):
    """Renders the create about page."""
    assert isinstance(request, HttpRequest)
    queryset = About.objects.all()
    serializer_class = AboutSerializer(queryset, many=True)

    return render(
        request,
        "about.html",
        {"data": serializer_class.data, },
    )

def blogs_filter(request):

    order = request.GET.get("order", None)
    if order == "popularity":
        blogs = Blog.objects.order_by("-views")
    elif order == "latest":
        blogs = Blog.objects.all().order_by("-date")
    else:
        blogs = Blog.objects.all()
        
    blogs = BlogFilter(request.GET, queryset=blogs).qs
  
    # Show many contacts per page.
    # paginator = Paginator(blogs, 1)
    # page_number = request.GET.get("page")
    # blogs = paginator.get_page(page_number)

    if blogs:
        context = {
            "blogs": blogs,
        }  # template name

    else:
        context = {"message": "There are no blogs available at the moment."}
    return render(request, "blogs_filter.html", context)

def blogs_list(request):

    blogs = Blog.objects.all().order_by("-date")
    myfilter = BlogFilter(request.GET, queryset=blogs)
    blogs = myfilter.qs

    # Show many contacts per page.
    paginator = Paginator(blogs, 100000000000000000000)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    print("hello")

    if blogs:
        context = {
            "blogs": page_obj,
            "myfilter": myfilter,
        }  # template name

    else:
        context = {"message": "There are no stories available at the moment."}
    return render(request, "blogs.html", context)


def blog_detail(request, id):

    blog = Blog.objects.filter(id=id).last()
    blog.views = F("views") + 1
    blog.save()
    blog.refresh_from_db()
    context = {"blog": blog,  'num_visits': blog.views}
    return render(request, "blog_detail.html", context)




def clear(request):
    return HttpResponse("")

