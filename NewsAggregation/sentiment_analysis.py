# transformers
import pymongo
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline, AutoModelForTokenClassification

client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
print(client["UserData"])
db = client["UserData"]
collection = db["Google_News"]

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert",max_length=512)
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
nlp = pipeline("sentiment-analysis", model = model, tokenizer=tokenizer)
news_text = []
a = collection.find()
for data in a:
    try:
        clean_text= data['news_summary'].replace("\n", " ")       
        clean_text= ''.join([c for c in clean_text if c != "'"])
        print(clean_text)
        sentiment = nlp(str(clean_text))
        print(sentiment)
        news_text.append(sentiment)
    except:
        print("Cannot do sentiment analysis")

print(news_text)
