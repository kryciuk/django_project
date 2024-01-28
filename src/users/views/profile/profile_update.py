from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import reverse
from django.views.generic import UpdateView

from core.base import has_group, redirect_to_dashboard_based_on_group
from users.forms import UserProfileUpdateForm
from users.models import Profile


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "users/profile/profile_update.html"
    model = Profile
    form_class = UserProfileUpdateForm

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.warning(self.request, "You don't have the required permissions to access this page.")
            group = self.request.user.groups.first()
            return redirect_to_dashboard_based_on_group(group.name)
        messages.warning(self.request, "You are not logged in.")
        return redirect_to_dashboard_based_on_group("")

    def get_success_url(self):
        return reverse("profile-update", kwargs={"pk": self.object.id})

    def form_valid(self, form):
        messages.success(self.request, "Profile successfully updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Profile not updated. Please verify correctness of entered data.")
        return super().form_invalid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user.is_authenticated:
            return (self.kwargs.get("pk") == self.request.user.id) or (
                has_group(self.request.user, "Owner") and profile.company == self.request.user.profile.company
            )
        return redirect_to_dashboard_based_on_group("")
