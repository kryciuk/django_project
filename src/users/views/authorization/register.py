from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.views.generic import FormView

from core.base import make_nice_error_keys
from core.consts import GROUPS
from recruitment.models import Company
from users.forms import CreateUserForm
from users.models import Profile


class RegisterView(FormView):
    template_name = "users/authorization/register.html"
    form_class = CreateUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Register - CloudStaffHub"
        return context

    def form_invalid(self, form):
        messages.warning(self.request, make_nice_error_keys(form.errors))
        return super().form_invalid(form)

    def form_valid(self, form):
        if not form.is_valid():
            return self.form_invalid(form)
        else:
            self.request.user = form.save()
        email_domain = self.request.user.email.split(sep="@")[-1]
        company = Company.objects.filter(email_domain=email_domain).first()
        if company is None:
            candidate_group = Group.objects.get(name="Candidate")
            candidate_group.user_set.add(self.request.user)
        else:
            employee_group = Group.objects.get(name="Employee")
            employee_group.user_set.add(self.request.user)
            profile = Profile.objects.filter(user=self.request.user).first()
            profile.company = company
        messages.success(self.request, f"Account created successfully for {self.request.user.username}.")
        return redirect("login")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            group = self.request.user.groups.first()
            match group.name:
                case GROUPS.GROUP__OWNER:
                    return redirect("dashboard-owner")
                case GROUPS.GROUP__EMPLOYEE:
                    return redirect("dashboard-employee")
                case GROUPS.GROUP__MANAGER:
                    return redirect("dashboard-manager")
                case GROUPS.GROUP__CANDIDATE:
                    return redirect("dashboard-candidate")
                case GROUPS.GROUP__RECRUITER:
                    return redirect("dashboard-recruiter")
                case _:
                    return redirect("dashboard-employee")
        return super().get(request, *args, **kwargs)
