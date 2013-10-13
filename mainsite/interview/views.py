from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from interview.models import Question
from interview.models import Attempt

def genInterview(intv_field):
    return Question.objects.all()[0:5]

single_round = []

def getInterviewQuestion(request):
    print request.method 

    if request.method == 'GET':
	intv_field = ""
	if 'Field' in request.GET: 
	    intv_field = request.GET['Field']
	single_round = genInterview(intv_field)
	
	single_question = {}
	single_question.update(csrf(request))
	single_question ['qid']= single_round[0].id
	single_question['qtext'] = single_round[0].text
	single_question['idx'] = 1
	return render_to_response('question.html',single_question)	
    elif request.method == 'POST':

	single_attempt = Attempt(session = 'xyz', response=request.POST['answer'])
	single_attempt.user_id = 1
	single_attempt.question_id = request.POST['qid'],
	single_attempt.save()
	
	next_idx = int(request.POST['idx'])
	if next_idx < len(single_round):
	    single_question = {}
	    single_question.update(csrf(request))
	    single_question ['qid']= single_round[next_idx].id
	    single_question['qtext'] = single_round[next_idx].text
	    single_question['idx'] = next_idx +1
	    return render_to_response('question.html',single_question)
	else:
	    return render_to_response('summary.html')

def sessiontest(request):
    if 'count' in request.session:
	request.session['count'] += 1
	return HttpResponse('new count=%s' % request.session['count'])
    else:
	request.session['count'] = 1
	return HttpResponse('No count in session. Setting to 1')

def startInterview(request):
    dic = {}
    message = "";
    if 'Field' in request.GET: 
	dic["Field"] = request.GET['Field'] 
    if 'Level' in request.GET: 
	dic["Level"] = request.GET['Level'] 
    if 'Keywords' in request.GET:
	dic["Keywords"] = request.GET['Keywords'] 

    return render_to_response('dashboard.html',dic)	
