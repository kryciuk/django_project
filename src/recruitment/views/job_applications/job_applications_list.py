import django_filters
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView

from recruitment.models import JobApplication


class JobApplicationsView(UserPassesTestMixin, ListView):
    model = JobApplication
    template_name = "recruitment/job_applications/job_applications.html"
    context_object_name = "job_applications"
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.groups.filter(name="Recruiter").exists() or
            self.request.user.groups.filter(name="Manager").exists()
            or self.request.user.groups.filter(name="Owner").exists()
            or self.request.user.is_superuser
        )

    def get_queryset(self):
        return JobApplication.objects.filter(job_offer__company=self.request.user.profile.company,
                                             status=JobApplication.Status.RECEIVED).order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Job Applications - CloudStaffHub"
        return context