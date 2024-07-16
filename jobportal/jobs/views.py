import os
from django.conf import settings
from django.http import HttpResponse
from .models import Job
from typing import List

def job_feed(request):
    jobs: List[Job] = Job.objects.all()

    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<source>'

    # Publisher and feed info
    xml += '<publisher-name>Your ATS</publisher-name>'
    xml += '<publisher-url>http://www.yourdomain.com</publisher-url>'
    xml += '<last-build-date>2024-07-16 12:00:00 +0000</last-build-date>'

    for job in jobs:
        xml += '<job>'
        xml += f'<title><![CDATA[{job.title}]]></title>'
        xml += f'<date><![CDATA[{job.date.strftime("%Y-%m-%d %H:%M:%S %z")}]]></date>'
        xml += f'<id><![CDATA[{job.job_id}]]></id>'
        xml += f'<photo-url><![CDATA[{job.photo_url}]]></photo-url>'
        xml += f'<description><![CDATA[{job.description}]]></description>'
        xml += f'<job-type><![CDATA[{job.job_type}]]></job-type>'
        xml += f'<company-name><![CDATA[{job.company_name}]]></company-name>'
        xml += f'<company-id><![CDATA[{job.company_id}]]></company-id>'
        xml += f'<company-full-address><![CDATA[{job.company_full_address}]]></company-full-address>'
        xml += f'<company-facebook-url><![CDATA[{job.company_facebook_url}]]></company-facebook-url>'
        xml += f'<company-data-policy-url><![CDATA[{job.company_data_policy_url}]]></company-data-policy-url>'
        xml += f'<company-url><![CDATA[{job.company_url}]]></company-url>'
        xml += f'<company-page-matching-approach><![CDATA[{job.company_page_matching_approach}]]></company-page-matching-approach>'
        xml += f'<full-address><![CDATA[{job.full_address}]]></full-address>'
        xml += f'<country><![CDATA[{job.country}]]></country>'
        xml += f'<salary-min><![CDATA[{job.salary_min}]]></salary-min>'
        xml += f'<salary-max><![CDATA[{job.salary_max}]]></salary-max>'
        xml += f'<salary-currency><![CDATA[{job.salary_currency}]]></salary-currency>'
        xml += f'<salary-type><![CDATA[{job.salary_type}]]></salary-type>'
        xml += f'<facebook-apply-data>'
        xml += f'    <application-callback-url><![CDATA[{job.facebook_apply_data_callback_url}]]></application-callback-url>'
        xml += f'    <custom-questions-url><![CDATA[{job.facebook_apply_data_custom_questions_url}]]></custom-questions-url>'
        xml += f'    <form-config>'
        xml += f'        <email-field><optional>FALSE</optional></email-field>'
        xml += f'        <phone-number-field><optional>FALSE</optional></phone-number-field>'
        xml += f'        <work-experience-field><optional>FALSE</optional></work-experience-field>'
        xml += f'    </form-config>'
        xml += f'</facebook-apply-data>'
        xml += '</job>'

    xml += '</source>'

    # Define the path to save the XML file
    file_path = os.path.join(settings.MEDIA_ROOT, 'jobs.xml')

    # Write the XML content to a file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(xml)

    # Create an HTTP response with the XML content
    response = HttpResponse(xml, content_type='application/xml')
    response['Content-Disposition'] = 'attachment; filename="jobs.xml"'
    return response
