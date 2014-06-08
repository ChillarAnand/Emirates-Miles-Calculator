import urllib, urllib2


page = 'http://www.emirates.com/account/english/miles-calculator/miles-calculator.aspx'

raw_params = {"ddlDepartureAirport" : "DEL", "ddlArrivalAirport" : "JFK", "ctl00$MainContent$ctl02$Cabin" : ["rbEconomy"] }

params = urllib.urlencode(raw_params)
request = urllib2.Request(page, params)
page = urllib2.urlopen(request)
print page.read()

