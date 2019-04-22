import bs4

"""

    From book: Web Scraping with Python page 98:

    from urllib.request import urlopen

    textPage = urlopen("http://mysite.com/chapter1.txt")
    print(str(textPage.read(), 'utf-8'))

    html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_langauge)")
    bsObj = BeautifulSoup(html)
    content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
    content = bytes(content, "UTF-8"
    content = content.decode("UTF-8")

    Check for: <meta charset="utf-8"> or <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=iso8859-1">
    """


def run():
    bsObj = bs4.BeautifulSoup(open('index.html'),features='html.parser')
    print(bsObj)
    header = bsObj.find("header").get_text()
    print(header)

if __name__ == '__main__':
    run()
