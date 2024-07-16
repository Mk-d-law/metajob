from celery import shared_task
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .models import Job

@shared_task
def generate_xml_feed():
    jobs = Job.objects.all()
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
    path = default_storage.save('jobs.xml', ContentFile(xml))
    return path
