import sys
import functions

def main():

    if len(sys.argv) == 3:

        classes = [ "Economy", "Business", "First" ]
        departure = sys.argv[1]
        arrival = sys.argv[2]

        for clas in classes:
            html_data = functions.get_return_data(departure, arrival, clas)   
            functions.parse_data(html_data, clas, 0)
            html_data2 = functions.get_oneway_data(html_data)
            functions.parse_data(html_data2, clas, 1)

        functions.print_data()

    else:
        print "Usage: python emirates.py <departure> <arrival>"
        print "Example: python emirates.py DEL JFK"


if __name__ == "__main__":
    main()
