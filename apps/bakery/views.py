from decouple import config
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView

from .forms import SubmitForm
from .models import CustomerSubmission as Submit
from .models import Post


class IndexView(SuccessMessageMixin, CreateView):
    """homepage"""

    model = Submit
    template_name = "bakery/index.html"
    form_class = SubmitForm
    success_url = reverse_lazy("bakery:gallery")
    success_message = "Your request was successfully submitted"

    def get_context_data(self, **kwargs):
        """passing multiple models to the template"""
        context = super(IndexView, self).get_context_data(**kwargs)
        # only grab the 6 latest posts
        context["cakes"] = Post.objects.all()[:6]
        return context

    def form_valid(self, form):
        """overwrite the save method to send an email upon save"""
        response = super(IndexView, self).form_valid(form)
        if form.is_valid():
            recipients = (config("CHEF"), config("EMAIL_HOST_USER"))
            send_mail(
                "ORDER PLACED",
                f"you have an order from {form.cleaned_data['name']}.",
                config("EMAIL_HOST_USER"),
                recipient_list=recipients,
                fail_silently=True,
            )
        return response


class GalleryView(ListView):
    """gallery page to see all the photos"""

    model = Post
    context_object_name = "posts"  # variable name passed to the template
    template_name = "bakery/gallery.html"


class FormView(SuccessMessageMixin, CreateView):
    """form page to submit an order"""

    model = Submit
    template_name = "bakery/form.html"
    form_class = SubmitForm
    success_url = reverse_lazy("bakery:gallery")
    success_message = "Your request was submitted"

    def form_valid(self, form):
        """overwrite the save method to send text upon save"""
        response = super(FormView, self).form_valid(form)
        return response


class PricingView(TemplateView):
    """pricing page"""

    template_name = "bakery/pricing.html"
