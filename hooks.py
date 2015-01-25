import re
from urlwatch import html2txt


def filter(url, data):
    if url == "http://www.klab.com/jp/press/2015":
        return html2txt.html2text(data, method='html2text')

    if type(data) == bytes:
        data = data.decode('utf-8')

    return data

