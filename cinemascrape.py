from xml.etree import ElementTree as ET
from datetime import datetime
import csv
# Import BeautifulSoup
content = []
# Read the XML file
with open("filmschedule.xml", "r") as file:
    # Read each line in the file, readlines() returns a list of lines
    content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
root = ET.fromstring(content)
sites = root.findall('.//site')
with open('filmschedule.csv', mode='w') as filmschedule_file:
    fieldnames = ['cinema', 'hall', 'filmName', 'showTime', 'cert', 'yt', 'img']
    schedule_writer = csv.writer(filmschedule_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for site in sites:
    sitename = site.find('name').text
    for performance in root.findall(".//performance"):
               sdate = datetime.strptime(performance.find('time').text, '%Y%m%d%H%M%S')
               evcode = performance.find('eventCode').text
               evsrch = ".//event[@eventCode='" + evcode + "']"
               hall = performance.find('hallName').text
               for event in root.findall(evsrch):
                 name = event.find('name').text
                 length = event.find('length').text
                 synopsis = event.find('synopsis').text
                 yt = event.find('youTubeLink').text
                 cert = event.find('certificate').text
                 imgchk = event.find('imageSmall').text
                 if imgchk and not imgchk.isspace():
                     img = event.find('imageSmall').text
                 else:
                     img = "blank"
                
                 print (sitename + ", " + hall + ",  " + name + ", " + str(sdate) + ", " + cert + ", " + yt + ", " + img)
