import mechanize

url = "http://www.emirates.com/account/english/miles-calculator/miles-calculator.aspx"
br = mechanize.Browser()
br.set_handle_robots(False) # ignore robots
br.open(url)



"""
f = br.select_form(nr=0)

print f

br.select_form(nr=0)
#br["ddlDepartureAirport"] = "DEL"
#br["ddlArrivalAirport"] = "JFK"


res = br.submit()
content = res.read()

with open("mechanize_results.html", "w") as f:
    f.write(content)
"""
