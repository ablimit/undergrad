#! /usr/bin/python 

from linkedin import linkedin
from linkedin import server
import json

API_KEY = 'fnv6hgzvzb8o'
API_SECRET = 'WeSpyxZaKm8dCnnF'
RETURN_URL = 'http://127.0.0.1:8000/'


# retrivejobs by ID, the count should handled internally 
def getJobs(application, count, keywords, start=0):
    if application != None and count > 0:
	# return application.search_job(selectors=[{'jobs': ['id', 'customer-job-code', 'posting-date']}], params={'keywords': keywords, 'count': count })
	return application.search_job(params={'keywords': keywords, 'count': count, 'start': start})
    return None


def getJobById(application,job_id):
    if application != None and job_id !=None:
	return application.get_job(job_id = job_id, selectors=['id',
		'customer-job-code',
		'active',
		'posting-date',
		'expiration-date',
		{'company': ['id', 'name']},
		{'position': ['title', 'location', 'job-functions', 'industries', 'job-type', 'experience-level']},
		'skills-and-experience',
		'description',
		'salary',
		'referral-bonus',
		'site-job-url',
		'location-description'])
    return None


def authorize():
    return server.quick_api(API_KEY, API_SECRET)

def getFileName(term='temp.txt',idx=''):
    sp = term.split()
    if len(idx) >0:
	sp.append(idx)
    sp.append('json')
    f = '.'.join(sp)
    return f

def dumpjobsFromLocal(application=None, fn = None):
    dic = {}
    if fn != None:
	data = json.load(open(fn,'r'))
	if application != None:
	    for job_id in data.keys():
		print ' '.join(("job_id:", str(job_id)))
		job = getJobById(application,job_id)
		dic[job_id] = job
    # dump those jobs
    with open('jobs.json','w') as f:
	json.dump(dic,f)

    print "done."

def dumpjobs(application=None):
    fn_coll = []
    # get job search data 
    for terms in ['Investment Banking Analyst', 'Financial Analyst', 'Accounting', 'Sales and Trading']:
	if application != None:
	    print ' '.join(("Desc:", terms))
	    job_coll = getJobs(application,20,terms,0)
	    fn = getFileName(terms,'0-19')
	    fn_coll.append(fn)
	    with open(fn,'w') as f:
		json.dump(job_coll,f)
	    
	    job_coll = getJobs(application,20,terms,20)
	    fn = getFileName(terms,'20-39')
	    fn_coll.append(fn)
	    with open(fn,'w') as f:
		json.dump(job_coll,f)
	    
	    job_coll = getJobs(application,10,terms,40)
	    fn = getFileName(terms,'40-49')
	    fn_coll.append(fn)
	    with open(fn,'w') as f:
		json.dump(job_coll,f)
    
    dic = {}
    for f in fn_coll:
	data = json.load(open(f))
	if application != None:
	    for item in data['jobs']['values']:
		job_id = item['id']
		print ' '.join(("job_id:", str(job_id)))
		job = getJobById(application,job_id)
		dic[job_id] = job
    # dump those jobs
    with open('jobs.json','w') as f:
	json.dump(dic,f)

    print "done."



def main():
    app = authorize()
    # dumpjobs(app)
    dumpjobsFromLocal(app,'dumps/jobs.json')

if __name__ == '__main__':
    main()

