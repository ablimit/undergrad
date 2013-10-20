from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField()
    answer = models.TextField()
    category = models.CharField(max_length=100)
    
    def __unicode__(self):
	return '\n'.join ((self.text,self.answer, self.category))

class User(models.Model):
    linkedin_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __unicode__(self):
	return '\n'.join ((self.linkedin_id,'\t'.join((self.first_name,self.last_name)),self.email))

class Attempt(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    session = models.CharField(max_length=100)
    response = models.TextField()
    attempt_date = models.DateField(auto_now=True)
    
    def __unicode__(self):
	return '\n'.join ((self.session,self.response))

class Jobs(models.Model):
    id  = models.CharField(max_length=100,primary_key=True)
    url = models.URLField(max_length =500,null=True)
    description = models.TextField(null=True)
    title = models.TextField(null=True)
    company = models.CharField(max_length=100, null=True)
    skills = models.TextField(null=True)
    related_questions = models.TextField(null=True)
    
    def __unicode__(self):
	return self.id

