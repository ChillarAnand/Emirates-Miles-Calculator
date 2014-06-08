import mechanize
br = mechanize.Browser()
br.set_handle_robots(False)  
br.set_handle_refresh(False)  
br.addheaders = [('User-agent', 'Firefox')]

url = 'http://www.emirates.com/account/english/miles-calculator/miles-calculator.aspx'
response = br.open(url)
response1 = br.response()  # get the response again

br.form = list(br.forms())[0]


br["ddlDepartureAirport"] = ["DEL"]
br["ddlArrivalAirport"] = ["JFK"]

br["ctl00$MainContent$ctl02$Cabin"] = ["rdBusiness"]
#br["ctl00$MainContent$ctl02$Cabin"] = ["*rdBusiness", "rdEconomy", "rdFirst"]

response = br.submit(name="ctl00$MainContent$ctl02$btnSubmit", label="Search")
print response.read()

