#MAIN CODE
import wikipedia
from search_func import *
from basic_func import *
from mult_search_func import multsearch
from query_def import * #give query options
from content_to_list import * #lists of sentences

#Function to define and work with a query
def get_new_query():
    while True:
        try:
            search = input("Enter new search term: ")
            #Important element to change the 'query' variable
            global query
            query = wikipedia.page(search)
        except wikipedia.exceptions.DisambiguationError:
            check = input("Be more specific! Would you like a list of all relevant pages? [y/n]: ")
            if "y" in check:
                print(wikipedia.search(search,results=100))
                continue
            else:
                continue
        except wikipedia.exceptions.PageError:
            print("That page apparently does not exist. Please try again")
            continue
        print("New Query Found: %s" % query)
        query_given(query) #from import
        break

#Input reciever without defined query
while True:
    #Input Line
    do = input("Next: ")
    if "new" in do:
        get_new_query() #keep funcdef in wiki.py
    elif "mult" in do:
        sw = do[5:]
        pagesdata = input("Enter pages separated by comma: ")
        pageslist = list(pagesdata.split(","))
        multsearch(pageslist,sw)
    elif "find" in do:
        n=1
        sw = do[5:]
        query = input("Enter page to search: ")
        report_sentences(query,sw)
    elif "search" in do:
        query = do[7:]
        print(wikipedia.search(query))
    elif "quit" in do:
        break
    elif "-h" in do:
        print("Useful commands: Title of page: name, Page URL: url, Content, images, links, Search for a word: search")
    else:
        print("Command not found! Please try again!")
