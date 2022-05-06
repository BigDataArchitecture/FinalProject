import json
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, AutoConfig
from transformers import T5ForConditionalGeneration, T5Tokenizer

def serverless_pipeline(model_path='./model'):
    # initialize the model architecture and weights
    model = T5ForConditionalGeneration.from_pretrained(model_path)
    # initialize the model tokenizer
    tokenizer = T5Tokenizer.from_pretrained(model_path)
    def predict(context):
        """predicts the answer on an given question and context. Uses encode and decode method from above"""
        # encode the text into tensor of integers using the appropriate tokenizer
        inputs = tokenizer.encode("summarize: " + context, return_tensors="pt", max_length=512, truncation=True)
        outputs = model.generate(
                inputs, 
                max_length=150, 
                min_length=40, 
                length_penalty=2.0, 
                num_beams=4, 
                early_stopping=True)
        answer = tokenizer.decode(outputs[0])
        return answer
    return predict

# initializes the pipeline
question_answering_pipeline = serverless_pipeline()

def handler(event, context):
    try:
        # loads the incoming event into a dictonary
        body = json.loads(event['body'])
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