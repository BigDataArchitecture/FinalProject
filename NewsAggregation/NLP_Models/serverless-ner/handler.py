import json
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, AutoConfig
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


def serverless_pipeline(model_path='./model'):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForTokenClassification.from_pretrained(model_path)
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    def predict(statement):
        ner_results = nlp(statement)
        return ner_results

    return predict

# initializes the pipeline
question_answering_pipeline = serverless_pipeline()

def handler(event,context):
    try:
        # loads the incoming event into a dictonary
        body = json.loads(event['body'])
        # uses the pipeline to predict the answer
        answer = question_answering_pipeline(statement=body['context'])
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
