import lxml.html
import os.path
import json

article_dir = './archive/raw/'
extract_dir = './archive/text/'

for filename in os.listdir(article_dir):
    with open(os.path.join(article_dir, filename)) as case_file:
        case_doc = json.loads(case_file.read())
        case_content = case_doc['content']
        case_url = case_doc['url']
        case_html = lxml.html.fromstring(case_content)
        case_body = case_html.cssselect('.sfContentBlock')[0]
        case_title = case_html.cssselect('#ContentPlaceHolder_ctl00_ctl00_ctl00_detailContainer_mainShortTextFieldLiteral_0')[0].text_content()
        case_text = case_body.text_content()
        with open(os.path.join(extract_dir, filename), 'w') as f:
            doc = {
                'title': case_title,
                'url': case_url,
                'text': case_text
            }
            f.write(json.dumps(doc))
