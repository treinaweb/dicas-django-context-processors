from django.urls import path

from .views import job_list, job_detail, job_list_by_skill

app_name = "jobs"
urlpatterns = [
    path("", job_list, name="job_list"),
    path("<int:pk>/", job_detail, name="job_detail"),
    path("skill/<int:skill_pk>/", job_list_by_skill, name="job_list_by_skill"),
]
