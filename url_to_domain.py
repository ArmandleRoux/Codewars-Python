def url_domain(url):
    if "www." in url:
        domain = url[url.index('.')+1:]
    elif "//" in url:
        domain = url[url.index('//')+2:]
    else:
        domain = url
    domain = domain.split("/")[0]
    if len(domain.split('.')[0]) > 3:
        return domain.split('.')[0]
    elif len(domain.split('.')[1]) > 3:
        return domain.split('.')[1]
    return domain.split('.')[0]


print(url_domain("http://www.googlewww.com"))
print(url_domain("http://google.co.jp"))
print(url_domain("https://en.wikipedia.org"))
print(url_domain("www.blabla.awww.com"))
print(url_domain("https://www.121shyphen-site.org.com"))
print(url_domain("ja.co.za"))

