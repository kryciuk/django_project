from django.urls import path

from recruitment.views.job_applications import (
    JobApplicationsClosedView,
    JobApplicationsDetailView,
    JobApplicationsUnderReviewView,
    JobApplicationsView,
)
from recruitment.views.job_offers import (
    JobOffersApplyView,
    JobOffersCreateView,
    JobOffersDetailView,
    JobOffersListView,
    JobOffersUpdateView,
)

urlpatterns = []

urlpatterns_job_offers = [
    path("job-offers", JobOffersListView.as_view(), name="job-offers"),
    path("job-offers/<int:pk>", JobOffersDetailView.as_view(), name="job-offer-detail"),
    path(
        "job-offers/update/<int:pk>",
        JobOffersUpdateView.as_view(),
        name="job-offer-update",
    ),
    path("job-offers/create", JobOffersCreateView.as_view(), name="job-offer-create"),
    path(
        "job-offers/<int:pk>/apply",
        JobOffersApplyView.as_view(),
        name="job-offer-apply",
    ),  # job-offers/<int:pk>/candiates/<int:pk>
]

urlpatterns_job_applications = [
    path(
        "job-applications/received",
        JobApplicationsView.as_view(),
        name="job-applications",
    ),
    path(
        "job-applications/closed",
        JobApplicationsClosedView.as_view(),
        name="job-applications-closed",
    ),
    path(
        "job-applications/review",
        JobApplicationsUnderReviewView.as_view(),
        name="job-applications-review",
    ),
    path(
        "job-applications/detail/<int:pk>",
        JobApplicationsDetailView.as_view(),
        name="job-applications-detail",
    ),
]

urlpatterns += urlpatterns_job_offers + urlpatterns_job_applications
