from django.contrib import admin

from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description'
    )
    search_fields = (
        'id',
        'name',
        'description'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    search_fields = (
        'id',
        'name'
    )


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'image',
        'author',
        'category',
        'is_published'
    )
    search_fields = (
        'id',
        'name',
        'description',
        'image',
        'author',
        'category',
        'is_published'
    )
    list_filter = ['is_published', 'category', 'author', ]


class IssueAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'book',
        'created_at',
        'issued',
        'issued_at',
        'returned',
        'return_date',
        'email',
        'address',
        'mobile',
    )
    search_fields = (
        'id',
        'user',
        'book',
        'created_at',
        'issued',
        'issued_at',
        'returned',
        'return_date',
        'email',
        'address',
        'mobile',
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Issue, IssueAdmin)
