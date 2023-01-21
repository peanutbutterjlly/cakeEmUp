from django.contrib import admin

from .models import CustomerSubmission, Post, PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ("post", "images")

    class Meta:
        model = PostImage


@admin.register(CustomerSubmission)
class CustomerSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created", "delivery", "phone")

    class Meta:
        model = CustomerSubmission
