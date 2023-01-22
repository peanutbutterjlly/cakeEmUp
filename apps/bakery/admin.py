from django.contrib import admin

from .models import CustomerSubmission, Post, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    inlines = [PostImageAdmin]
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Post


@admin.register(CustomerSubmission)
class CustomerSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created", "delivery", "phone")

    class Meta:
        model = CustomerSubmission
