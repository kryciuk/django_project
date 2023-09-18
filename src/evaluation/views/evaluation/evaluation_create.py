from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.views.generic import CreateView

from evaluation.forms import EvaluationCreateForm
from evaluation.models import Evaluation, Questionnaire


class EvaluationCreateView(CreateView):
    model = Evaluation
    form_class = EvaluationCreateForm
    template_name = "evaluation/evaluation_create.html"
    context_object_name = "evaluation"

    def get_context_data(self, **kwargs):
        context = super(EvaluationCreateView, self).get_context_data(**kwargs)
        context["form"].fields["employee"].queryset = User.objects.filter(
            profile__company=self.request.user.profile.company
        )
        context["form"].fields["questionnaire"].queryset = Questionnaire.objects.filter(
            created_by=self.request.user
        )
        return context

    def form_valid(self, form):
        form.instance.manager = self.request.user
        form.instance.date_created = datetime.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("dashboard-manager")
