import requests
import lxml.html
import urlparse

import ipdb

max_pages = 73
initial_url = 'http://www.medicalprotection.org/uk/casebook-and-resources/page/%s'

for page_num in range(max_pages):
    page_url = initial_url % (page_num,)
    print 'Fetching %s' % (page_url,)
    page = requests.get(page_url)
    content = page.text
    html = lxml.html.fromstring(content)
    for (anchor_num, anchor) in enumerate(html.cssselect('#lane8 .sfGenericList a')):
        url = anchor.attrib['href']
        case_url = urlparse.urljoin(page_url, url)
        print 'Fetching %s' % (case_url,)
        case_page = requests.get(case_url)
        case_content = case_page.text
        with open('./archive/raw/%s-%s.html' % (page_num, anchor_num), 'w') as f:
            f.write(case_content.encode('utf8'))
