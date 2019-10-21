# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    if len(news_ticker) + len(headline) <= 140:
        if(news_ticker == ""):
            news_ticker += headline #No space for the first item
        else:
            news_ticker += " {}".format(headline) #if not first, add space...
        #print("we added \n")
        #print(len(news_ticker))
    elif len(news_ticker) < 140:
        news_ticker += " {}".format(headline[0: 139 - len(news_ticker)])
        #print("we added half")
        #print(len(news_ticker))
    else:
        break

print(news_ticker)
print(len(news_ticker))