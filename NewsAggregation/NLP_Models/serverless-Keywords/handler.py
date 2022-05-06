import json
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, AutoConfig
from transformers import T5ForConditionalGeneration, T5Tokenizer
from keybert import KeyBERT

def serverless_pipeline():
    # initialize the model architecture and weights
    def predict(context):
        kw_model = KeyBERT("distilbert-base-nli-mean-tokens")
        keywords = kw_model.extract_keywords(
            context,
            keyphrase_ngram_range=(1, 1),
            use_mmr=True,
            stop_words="english",
            top_n=10)        
        return keywords
    return predict

# initializes the pipeline
question_answering_pipeline = serverless_pipeline()

def handler(event, context):
    try:
        # loads the incoming event into a dictonary
        body = json.loads(event['body'])
        print(body)
        # uses the pipeline to predict the answer
        answer = question_answering_pipeline(context=body['context'])
        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True

            },
            "body": json.dumps({'answer': answer})
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