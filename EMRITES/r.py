import requests

URL = 'http://www.emirates.com/account/english/miles-calculator/miles-calculator.aspx'
payload = {
     "ddlDepartureAirport" : "DEL",
     "ddlArrivalAirport" : "JFK"
        }

session = requests.session()
r = requests.post(URL, data=payload)
print r.cookies

with open("requests_results.html", "w") as f:
    f.write(r.content)
