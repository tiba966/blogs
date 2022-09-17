from django.urls import path
from . import views
from django.contrib import admin
from . import views
from . import api

app_name = "jobs"

urlpatterns = [
    path("", views.index, name="index"),
    path("reply/", views.reply, name="reply"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("blogs_filter/", views.blogs_filter, name="blogs_filter"),

    path("blogs/", views.blogs_list, name="blogs"),
    path("blogs/<int:id>", views.blog_detail, name="blog_detail"),
    # api
    path("api/blogs", api.blogs_api, name="blogs_api"),
    path("api/blogs/<int:id>", api.detail_api, name="detail_api"),
    # class based views
    path(
        "api/v2/blogs",
        api.BlogListApi.as_view(),
        name="BlogListApi",
    ),
    path(
        "api/v2/blogs/<int:id>",
        api.BlogDetail.as_view(),
        name="BlogDetail",
    ),
]
