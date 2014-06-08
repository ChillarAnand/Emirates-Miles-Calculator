import mechanize
br = mechanize.Browser()
br.open("http://www.gmail.com")
for f in br.forms():
    print f
