from django.contrib import admin
from interview.models import Question, User, Attempt, Jobs

admin.site.register(Question)
admin.site.register(User)
admin.site.register(Attempt)
admin.site.register(Jobs)

