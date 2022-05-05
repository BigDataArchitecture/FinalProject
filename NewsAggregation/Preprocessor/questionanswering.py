import pymongo
import pandas as pd



def questionanswer():
    keyword=input('Enter keywords for news: ')
    client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
#print(client["News"])
    db = client["News"]
    collection = db["GoogleAPI"]
    regex_query = { "news_summary" : {"$regex" : keyword} }
    #myquery = { "news_summary": "Singapore" }

    mydoc = collection.find(regex_query)

    #mydoc= unique.find(regex_query)
    #unique_dataset = collection.distinct("news_title")

    # print()
    news=[]
    for x in mydoc:
        a=x["news_title"]
        news.append(a)

    df = pd.DataFrame(news)
    df2=df.drop_duplicates(0, inplace=False)
    return df2

if __name__ == "__main__":
    answer=questionanswer()
    print(answer)