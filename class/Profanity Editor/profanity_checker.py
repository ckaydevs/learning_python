import urllib

def read_text():
    #creating an object of file type.
    quotes=open("C:\Users\Ckay\Desktop\python codes\class\Profanity Editor\movie_quotes.txt")
    contents_of_file=quotes.read()#reading the file
    print(contents_of_file)
    quotes.close()#closing the connection
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    #opening a connection with profanity checker
    connection=urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)#sending the file-data to profanity checker website of google and opening connection.
    output=connection.read()# reading the website output
    print("Profanity Checker:"+output)
    connection.close()#closing the connection
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()
