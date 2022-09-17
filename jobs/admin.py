from django.contrib import admin
from .models import  Blog, Index, About, Category
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'email',
        'comment',
    ]





class AboutAdmin(admin.ModelAdmin):
    list_display = [
        "id",
       
        "image_middle_about",
    ]


class IndexAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "text_about_index",
        "text_about_index_ar",
        "text_index",
        "text_index_ar",
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ar_name",
        "en_name"
    ]


class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "image_one",
        "date",
        "category",
        'tutorial_Video',
        "authors",
        "authors_ar",
        "title",
        "title_ar",
        "desc1",
        "desc1_ar",
        "desc2",
        "desc2_ar",
        "blank",
        "blank_ar",
        "desc3",
        "desc3_ar",
        "desc4",
        "desc4_ar",
        "desc5",
        "desc5_ar",
        "desc6",
        "desc6_ar",
        "subtitle",
        "subtitle_ar",
        "subtitle_desc1",
        "subtitle_desc1_ar",
        "subtitle_desc2",
        "subtitle_desc2_ar",
        "subtitle2",
        "subtitle2_ar",
        "subtitle2_desc1",
        "subtitle2_desc1_ar",
        "subtitle2_desc2",
        "subtitle2_desc2_ar",
        "subtitle2_desc3",
        "subtitle2_desc3_ar",
        "subtitle3",
        "subtitle3_ar",
        "subtitle3_desc1",
        "subtitle3_desc1_ar",
                "subtitle4",
        "subtitle4_ar",
        "subtitle4_desc1",
        "subtitle4_desc1_ar",
         "subtitle4_desc2",
        "subtitle4_desc2_ar",
         "subtitle4",
        "subtitle4_ar",
        
    ]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)


admin.site.register(Index, IndexAdmin)


admin.site.register(About, AboutAdmin)
