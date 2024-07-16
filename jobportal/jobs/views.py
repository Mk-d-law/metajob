from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from typing import List, Tuple

def job_feed(request):
    jobs: List[Job] = Job.objects.all()
    response = HttpResponse(content_type='application/xml')
    response['Content-Disposition'] = 'attachment; filename="jobs.xml"'

    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<jobs>'

    for job in jobs:
        xml += f'''
        <job>
            <id><![CDATA[{job.id}]]></id>
            <title><![CDATA[{job.title}]]></title>
            <description><![CDATA[{job.description}]]></description>
            <location><![CDATA[{job.location}]]></location>
            <country><![CDATA[{job.country}]]></country>
            <language><![CDATA[{job.language}]]></language>
            <link><![CDATA[{job.link}]]></link>
            <pubdate><![CDATA[{job.pubdate}]]></pubdate>
            <updated><![CDATA[{job.updated}]]></updated>
            <salary><![CDATA[{job.salary}]]></salary>
            <company><![CDATA[{job.company}]]></company>
            <expire><![CDATA[{job.expire}]]></expire>
            <jobtype><![CDATA[{job.jobtype}]]></jobtype>
        </job>
        '''

    xml += '</jobs>'
    response.write(xml)
    return response
