import json
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline


def serverless_pipeline(model_path='./model'):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    def predict(statement):
        sentiment_results = nlp(statement)
        return sentiment_results

    return predict

# initializes the pipeline
sentiment = serverless_pipeline()

def handler(event,context):
    try:
        # loads the incoming event into a dictonary
        body = json.loads(event['body'])
        # uses the pipeline to predict the answer
        answer = sentiment(statement=body['context'])
        print(answer)

        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True

            },
            "body": json.dumps({'answer': str(answer)})
        }
    except Exception as e:
        print(repr(e))
        return {
            "statusCode": 500,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps({"error": repr(e)})
        }