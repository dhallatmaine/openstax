import requests
from bs4 import BeautifulSoup
from pathlib import Path

URL = 'https://openstax.org/apps/cms/api/v2/pages/30/'
json = requests.get(URL).json()

books = json['books']
for book in books:
    pdf_url = book['high_resolution_pdf_url']
    if pdf_url is None:
        continue
    title = book['title']
    print ("Downloading %s" % title)
    filename = Path(title + '.pdf')
    pdf_contents = requests.get(pdf_url)
    filename.write_bytes(pdf_contents.content)
    print ("Downloaded %s" % title)

