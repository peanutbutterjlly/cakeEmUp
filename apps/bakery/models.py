from datetime import date, timedelta

from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from PIL import Image

two_weeks_out = date.today() + timedelta(days=14)


class Post(TimeStampedModel):
    """data-table to hold posts"""

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """define where to go for a specific instance of a post"""
        # reverse returns the full path as a string, then we let the view handle the 'redirect'
        return reverse("bakery:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ("-created",)


class PostImage(models.Model):
    """data-table to hold images related to posts"""

    post = models.ForeignKey(
        Post, default=None, on_delete=models.CASCADE, related_name="images"
    )
    images = models.ImageField(upload_to="img/post/")

    def __str__(self):
        return self.post.title

    def save(self, *args, **kwargs) -> None:
        """resize image to 800px wide and save as webp"""
        super().save(*args, **kwargs)
        with Image.open(self.images.path) as img:
            width, height = img.size
            target_width = 300
            h_coefficient = width / target_width
            target_height = int(height / h_coefficient)
            img = img.resize((target_width, target_height), Image.ANTIALIAS)
            img.save(self.images.path, "webp", optimize=True, quality=99)


class CustomerSubmission(TimeStampedModel):
    """data-table to hold bake requests"""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    image = models.ImageField(blank=True, upload_to="img/request/")
    delivery = models.BooleanField(default=False)
    date_needed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
