from .forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class LeaveFeedback(CreateView):
    template_name = 'feedback/leave_feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('post_list')