from .models import Skill


def skills_context(request):
    return {"skills": Skill.objects.all()}