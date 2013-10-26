#! /usr/bin/python 

from linkedin import linkedin
from linkedin import server
import json

API_KEY = 'fnv6hgzvzb8o'
API_SECRET = 'WeSpyxZaKm8dCnnF'
RETURN_URL = 'http://127.0.0.1:8000/'

docs = """http://api.linkedin.com/v1/job-search:(jobs:(id,customer-job-code,active,posting-date,expiration-date,posting-timestamp,expiration-timestamp,company:(id,name),position:(title,location,job-functions,industries,job-type,experience-level),skills-and-experience,description-snippet,description,salary,job-poster:(id,first-name,last-name,headline),referral-bonus,site-job-url,location-description))?distance=10&job-title=product&facets=company,location&facet=industry,6&facet=company,1288&sort=DA"""

# retrivejobs by ID, the count should handled internally 
def getJobs(application, count, keywords, start=0):
    if application != None and count > 0:
	return application.search_job(selectors=[{'jobs': ['id', {'position': ['title','location','job-functions','industries','job-type','experience-level']}]}], params={'keywords': keywords, 'count': count })
	# return application.search_job(params={'keywords': keywords, 'count': count, 'start': start})
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
    dic = {}
    # get job search data 
    for terms in ['Investment Banking Analyst', 'Financial Analyst', 'Accounting', 'Sales and Trading']:
	if application != None:
	    print ' '.join(("Desc:", terms))
	    job_ids = []
	    start_index = 0 
	    while len(job_ids) <50:
		jobs = getJobs(application,20,terms,start_index)
		for job in jobs['jobs']['values']:
		    el = int(job['position']['experienceLevel']['code'])
		    # only retrieve entry or internship jobs
		    if el < 3 and el > 0:
			job_id = job['id']
			job_ids.append(job_id)
			jobinfo = getJobById(application,job_id)
			dic[job_id] = jobinfo
			print "EL job: %s, Dictionary size: %d" % (job_id, len(dic))

		start_index +=20
	    
    
    with open('entryLevelJobs.json','w') as f:
		json.dump(dic,f)
    print "done."



def main():
    app = authorize()
    dumpjobs(app)
    # dumpjobsFromLocal(app,'dumps/jobs.json')

if __name__ == '__main__':
    main()

