import os
from django.conf import settings
from django.http import HttpResponse
from .models import Job
from typing import List
from datetime import datetime

#metajob generate
def metajob_generate(request):
    jobs: List[Job] = Job.objects.all()

    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<source>'

    # Publisher and feed info
    xml += '<publisher-name>untappped</publisher-name>'
    xml += '<publisher-url>http://www.untappped.com</publisher-url>'
    current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')
    xml += f'<last-build-date>{current_time}</last-build-date>'

    for job in jobs:
        xml += '<job>'
        xml += f'<title><![CDATA[{job.title}]]></title>'
        xml += f'<date><![CDATA[{job.postdate.strftime("%Y-%m-%d %H:%M:%S %z")}]]></date>'
        xml += f'<id><![CDATA[{job.jobid}]]></id>'
        xml += f'<description><![CDATA[{job.jobdesc}]]></description>'
        xml += f'<job-type><![CDATA[{job.jobtype}]]></job-type>'
        xml += f'<company-name><![CDATA[{job.eid.companyname}]]></company-name>'
        xml += f'<company-id><![CDATA[{job.eid}]]></company-id>'
        xml += f'<company-full-address><![CDATA[{job.eid.address}]]></company-full-address>'
        xml += f'<company-facebook-url><![CDATA[{job.eid.fblink}]]></company-facebook-url>'
        xml += f'<company-url><![CDATA[{job.eid.website}]]></company-url>'
        xml += f'<country><![CDATA[{job.eid.location}]]></country>'
        xml += f'<salary><![CDATA[{job.basicpay}]]></salary>'
        xml += f'<salary-currency><![CDATA[{job.salary_currency}]]></salary-currency>'
        xml += f'<salary-type><![CDATA[{job.salary_type}]]></salary-type>'
        xml += f'<facebook-apply-data>'
        xml += f'    <application-callback-url><![CDATA[https://untappped/singlejob/{job.jobid}]]></application-callback-url>'
        xml += f'</facebook-apply-data>'
        xml += '</job>'

    xml += '</source>'

    # Define the path to save the XML file
    file_path = os.path.join(settings.MEDIA_ROOT, 'metajob.xml')

    # Write the XML content to a file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(xml)

    # Create an HTTP response with the XML content
    return HttpResponse("MetaJob XML feed generated successfully.")

#metajob feed
def metajob_feed(request):
    # Define the path to save the XML file
    file_path = os.path.join(settings.MEDIA_ROOT, 'metajob.xml')

    # Read the XML content from the file
    with open(file_path, 'r', encoding='utf-8') as f:
        xml = f.read()

    # Create an HTTP response with the XML content
    response = HttpResponse(xml.encode('utf-8'), content_type='application/xml')
    response['Content-Disposition'] = 'inline; filename="metajob.xml"'
    return response

#jobgrind generate
def jobgrin_generate(request):
    jobs: List[Job] = Job.objects.all()

    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<source>'

    # Publisher and feed info
    xml += '<publisher>untappped</publisher>'
    xml += '<publisherurl>http://www.untappped.com</publisherurl>'

    for job in jobs:
        xml += '<job>'
        xml += f'<title><![CDATA[{job.title}]]></title>'
        xml += f'<date><![CDATA[{job.postdate.strftime("%Y-%m-%d %H:%M:%S %z")}]]></date>'
        xml += f'<referencenumber><![CDATA[{job.jobid}]]></referencenumber>'
        xml += f'<url><![CDATA[https://untappped/singlejob/{job.jobid}]]></url>'
        xml += f'<description><![CDATA[{job.jobdesc}]]></description>'
        
        xml += f'<companyName><![CDATA[{job.eid.companyname}]]></companyName>'
        xml += f'<email><![CDATA[{job.eid.email}]]></email>'
        xml += f'<postalcode><![CDATA[{job.eid.pincode}]]></postalcode>'
        xml += f'<city><![CDATA[{job.eid.city}]]></city>'
        xml += f'<state><![CDATA[{job.location}]]></state>'
        xml += f'<country><![CDATA[{job.eid.location}]]></country>'
        xml += f'<salary><![CDATA[{job.basicpay}]]></salary>'
        
        xml += '</job>'

    xml += '</source>'

    # Define the path to save the XML file
    file_path = os.path.join(settings.MEDIA_ROOT, 'jobgrin.xml')

    # Write the XML content to a file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(xml)

    # Create an HTTP response with the XML content
    return HttpResponse("jobgrin XML feed generated successfully.")

#jobgrind feed
def jobgrin_feed(request):
    # Define the path to save the XML file
    file_path = os.path.join(settings.MEDIA_ROOT, 'jobgrin.xml')

    # Read the XML content from the file
    with open(file_path, 'r', encoding='utf-8') as f:
        xml = f.read()

    # Create an HTTP response with the XML content
    response = HttpResponse(xml.encode('utf-8'), content_type='application/xml')
    response['Content-Disposition'] = 'inline; filename="jobgrin.xml"'
    return response

#indeed generate
def indeed_generate(request):
    jobs: List[Job] = Job.objects.all()

    # Initialize the XML content
    xml = '<?xml version="1.0" encoding="utf-8"?>'
    xml += '<source>'
    xml += '<publisher>untappped</publisher>'
    xml += '<publisherurl>http://untappped.com</publisherurl>'
    current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')
    xml += f'<last-build-date>{current_time}</last-build-date>'

    for job in jobs:
        xml += '<job>'
        xml += f'<title><![CDATA[{job.title}]]></title>'
        xml += f'<date><![CDATA[{job.postdate.strftime("%Y-%m-%d %H:%M:%S %z")}]]></date>'
        xml += f'<referencenumber><![CDATA[{job.jobid}]]></referencenumber>'
        xml += f'<requisitionid><![CDATA[{job.jobid}]]></requisitionid>'  # Assuming requisitionid is the same as jobid
        xml += f'<url><![CDATA[https://untappped/singlejob/{job.jobid}]]></url>'
        xml += f'<company><![CDATA[{job.eid.companyname}]]></company>'
        xml += f'<sourcename><![CDATA[{job.eid.companyname}]]></sourcename>'
        xml += f'<city><![CDATA[{job.eid.city}]]></city>'
        xml += f'<state><![CDATA[{job.location}]]></state>'
        xml += f'<country><![CDATA[{job.eid.location}]]></country>'
        xml += f'<postalcode><![CDATA[{job.eid.pincode}]]></postalcode>'
        
        xml += f'<email><![CDATA[{job.eid.email}]]></email>'
        xml += f'<description><![CDATA[{job.jobdesc}]]></description>'
        xml += f'<salary><![CDATA[{job.basicpay}]]></salary>'
        
        xml += f'<jobtype><![CDATA[{job.jobtype}]]></jobtype>'
        xml += '</job>'

    xml += '</source>'

    # Define the path to save the XML file
    file_path = os.path.join(settings.MEDIA_ROOT, 'indeed.xml')

    # Write the XML content to a file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(xml)

    # Create an HTTP response with the XML content
    return HttpResponse("indeed XML feed generated successfully.")

#indeed feed
def indeed_feed(request):
    # Define the path to save the XML file
    file_path = os.path.join(settings.MEDIA_ROOT, 'indeed.xml')

    # Read the XML content from the file
    with open(file_path, 'r', encoding='utf-8') as f:
        xml = f.read()

    # Create an HTTP response with the XML content
    response = HttpResponse(xml.encode('utf-8'), content_type='application/xml')
    response['Content-Disposition'] = 'inline; filename="indeed.xml"'
    return response

#adzuna generate
def adzuna_generate(request):
    # Get all jobs from the database
    jobs: List[Job] = Job.objects.all()

    # Create the root element
    xml = '<?xml version="1.0" encoding="UTF-8" ?>\n<jobs>\n'

    for job in jobs:
        # Create <job> element
        xml += '    <job>\n'
        xml += f'        <title><![CDATA[{job.title}]]></title>\n'
        xml += f'        <id><![CDATA[{job.jobid}]]></id>\n'
        xml += f'        <description><![CDATA[{job.jobdesc}]]></description>\n'
        xml += f'        <url><![CDATA[https://untappped/singlejob/{job.jobid}]]></url>\n'
        xml += f'        <location><![CDATA[{job.eid.city}]]></location>\n'
        xml += f'        <country><![CDATA[{job.eid.location}]]></country>\n'
        xml += f'        <salary><![CDATA[{job.basicpay}]]></salary>\n'
        xml += f'        <company><![CDATA[{job.eid.companyname}]]></company>\n'
        xml += '    </job>\n'

    # Close the root element
    xml += '</jobs>'

    # Define the path to save the XML file
    file_path = os.path.join(settings.MEDIA_ROOT, 'adzuna.xml')

    # Write the XML content to a file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(xml)

    # Create an HTTP response with the XML content
    return HttpResponse("adzuna XML feed generated successfully.")

#adzuna feed
def adzuna_feed(request):
    # Define the path to save the XML file
    file_path = os.path.join(settings.MEDIA_ROOT, 'adzuna.xml')

    # Read the XML content from the file
    with open(file_path, 'r', encoding='utf-8') as f:
        xml = f.read()

    # Create an HTTP response with the XML content
    response = HttpResponse(xml.encode('utf-8'), content_type='application/xml')
    response['Content-Disposition'] = 'inline; filename="adzuna.xml"'
    return response


    