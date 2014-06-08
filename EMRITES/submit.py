import re
from mechanize import Browser

br = Browser()
br.open("http://www.emirates.com/account/english/miles-calculator/miles-calculator.aspx")
br.select_form(ddlDepartureAirport-suggest="DEL")
# Browser passes through unknown attributes (including methods)
# to the selected HTMLForm (from ClientForm).
br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)
response = br.submit()  
