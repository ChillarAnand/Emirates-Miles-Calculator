import mechanize
import sys

br = mechanize.Browser()

url = sys.argv[1]

br.open(url)

for form in br.forms():
    print form.name 
    print form
