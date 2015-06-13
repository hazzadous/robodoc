import lxml.html
import os.path

article_dir = './archive/raw/'
extract_dir = './archive/text/'

for filename in os.listdir(article_dir):
    with open(os.path.join(article_dir, filename)) as case_file:
        case_content = case_file.read()
        case_html = lxml.html.fromstring(case_content)
        case_body = case_html.cssselect('.sfContentBlock')[0]
        case_text = case_body.text_content()
        with open(os.path.join(extract_dir, filename), 'w') as f:
            f.write(case_text.encode('utf8'))
