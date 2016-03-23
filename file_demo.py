import urllib

def read_text():
    quotes=open("C:\Users\Rajeshwar Rao P\Desktop\Shivani\infosys\movie_quotes.txt")
    words=quotes.read()
    print(words)
    check_profanity(words)
    quotes.close()
    

def check_profanity(words):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+words)
    #http://isithackday.com/arrpi.php?text=   tom cruise pirate language
    output=connection.read()
    print(output)
    connection.close()

read_text()
