import mechanize
from bs4 import BeautifulSoup
from tabulate import tabulate

miles_data = []



def browse():

    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
    br.addheaders = [('User-Agent', ua), ('Accept', '*/*')]
    return br




def get_return_data(departure, arrival, class_type):

    try:
        br = browse()
        url = 'http://www.emirates.com/account/english/miles-calculator/miles-calculator.aspx'
        response = br.open(url)

        br.form = list(br.forms())[0]
        br["ddlDepartureAirport"] = [departure]
        br["ddlArrivalAirport"] = [arrival]
        br["ctl00$MainContent$ctl02$Cabin"] = [ "rd" + class_type]

        response = br.submit(name="ctl00$MainContent$ctl02$btnSubmit", label="Search")

        html_data = response.read()
        return html_data

    except:
       print "Error: Unable to get return data "





def parse_data(html_data, clas, ticket_flag):

    try:
        soup = BeautifulSoup(html_data)

        table = soup.find("div", { "class" : "filteredTabs"  } )

        ticket = ["return", "oneway"][ticket_flag]
        tiers = ["blue", "silver", "gold", "platinum"]

        for tier in tiers:
             id_string = tier + ticket + "Earn"
             bre = table.find("div", { "id" : id_string  }).findAll("td")
             saver_miles =  bre[0].get_text()
             flex_miles = bre[1].get_text()

             global miles_data
             miles_data.append([clas, ticket, tier, "Saver", saver_miles])
             miles_data.append([clas, ticket, tier, "Flex", flex_miles])

    except:
        print "Error while parsing data"




def get_oneway_data(html_data):

    try:
        soup = BeautifulSoup(html_data)
        oneway_link = soup.find("a", {"rel" : "onewayEarn"})
        root_link = "http://emirates.com"
        oneway_link = oneway_link["href"]
        url = root_link + oneway_link
        
        br = browse()
        response = br.open(url)
        html_data2 = response.read()
        return html_data2

    except:
        print "Error: Unable to get oneway link"




def print_data():
    global miles_data 
    print tabulate(miles_data, headers = ["Class Type", "Ticket Type", "Tier Type", "Fare Type", "Skywards Miles"])
