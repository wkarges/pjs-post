import requests

# Set the name of the XML file.
xml_file = "post-schema.xml"

# Set the PJS server URL
url = "http://<YourHostname>:<YourPort>/MeterUpdates"

# Set request headers
header = {'Content-Type':'data/xml', 'Accept':'text/plain', 'Connection':'keep-alive', 'Accept-Encoding':'gzip, deflate, br'}

# Open the meterdata xml file and write to body of POST request
with open(xml_file) as xml:
    r = requests.post(url, data=xml, headers=header)
    if r.status_code == 200:
        print('Success!  Response Status Code: ', r.status_code)
    elif r.status_code != 200:
        print('Error, response status code: ', r.status_code)