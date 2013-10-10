from django.contrib import admin
from interview.models import Question, User, Attempt

admin.site.register(Question)
admin.site.register(User)
admin.site.register(Attempt)

