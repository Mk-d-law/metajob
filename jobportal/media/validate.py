import requests
from lxml import etree

url = "https://fb.me/jobs_feed_validator.xsd"
response = requests.get(url)
with open("jobs_feed_validator.xsd", "wb") as file:
    file.write(response.content)



def validate_xml(xml_file, xsd_file):
    with open(xsd_file, 'rb') as xsd_fh:
        schema_root = etree.XML(xsd_fh.read())
    schema = etree.XMLSchema(schema_root)

    with open(xml_file, 'rb') as xml_fh:
        xml_doc = etree.parse(xml_fh)

    result = schema.validate(xml_doc)
    if result:
        print("XML file is valid.")
    else:
        print("XML file is invalid.")
        log = schema.error_log
        for error in log:
            print(error.message)

# Download the XML file (if it's a URL) or use an existing local file
xml_url = "jobportal/media/jobs.xml"


validate_xml("metajob.xml", "jobs_feed_validator.xsd")
