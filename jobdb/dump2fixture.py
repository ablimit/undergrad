#! /usr/bin/python 

import json
import sys

def dumpjobsFixture(fn = 'dumps/jobs.json', dumpname ='dumps/jobs.fixture.json'):
    data = [] 
    if fn != None:
	jobs = json.load(open(fn,'r'))
	for job_id in jobs.keys():
		print "job_id: %s" % job_id
		# dic = {"model": "interview.jobs", "fields": {'id': '', 'url': 'www.linkedin.com', 'description': '', 'title': '', 'company': '', 'skills': '', 'related_questions': ''}}
		dic = {"model": "interview.jobs", 'pk': job_id, "fields": {'description': '?', 'title': '?', 'company': '?', 'skills': '?', 'related_questions': ''}}
		# dic = {"model": "interview.jobs", "fields": {'id': '', 'related_questions': '?'}}
		if jobs[job_id].get("siteJobUrl", None):
		    dic["fields"]["url"] = jobs[job_id]["siteJobUrl"]
		if jobs[job_id].get("description", None):
		    dic["fields"]["description"] = jobs[job_id]["description"]
		if jobs[job_id]['position'].get("title", None):
		    dic["fields"]["title"] =jobs[job_id]["position"]["title"]
		if jobs[job_id]["company"].get("name", None):
		    dic["fields"]["company"] = jobs[job_id]["company"]["name"]
		if jobs[job_id].get("skillsAndExperience", None):
		    dic["fields"]["skills"] = jobs[job_id]["skillsAndExperience"]
		data.append(dic)
	# dump those jobs
	with open(dumpname,'w') as f:
	    json.dump(data,f)
    print "dump fixture done."

def main():
    dumpjobsFixture()

if __name__ == '__main__':
    main()

