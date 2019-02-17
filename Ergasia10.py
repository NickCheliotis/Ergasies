import urllib.request
BR=0
P=0

url=input("Hey,please give me a url:")
if (url[0:3]!="http") or (url[0:4]!="https"):
    url="https://"+url
x=urllib.request.urlopen(url)
HtmlCode=(x.read())
BR=HtmlCode.count("<br>")
P=HtmlCode.count("<p>")
print ("There are "+BR+"<br>"+"and"+P+"<p>")



