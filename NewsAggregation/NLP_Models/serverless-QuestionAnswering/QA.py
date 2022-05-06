import json
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, AutoConfig
import pymongo
import spacy
# from spacy_streamlit import load_model

# client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
# print(client["News"])
# db = client["News"]
# collection = db["GoogleAPI_links"]
# all_data = collection.find()

# def encode(tokenizer, question, context):
#     """encodes the question and context with a given tokenizer"""
#     encoded = tokenizer.encode_plus(question, context)
#     return encoded["input_ids"], encoded["attention_mask"]

# def decode(tokenizer, token):
#     """decodes the tokens to the answer with a given tokenizer"""
#     answer_tokens = tokenizer.convert_ids_to_tokens(
#         token, skip_special_tokens=True)
#     return tokenizer.convert_tokens_to_string(answer_tokens)

# def serverless_pipeline(model_path='./model'):
#     """Initializes the model and tokenzier and returns a predict function that ca be used as pipeline"""
#     tokenizer = AutoTokenizer.from_pretrained(model_path)
#     model = AutoModelForQuestionAnswering.from_pretrained(model_path)
#     def predict(question, context):
#         """predicts the answer on an given question and context. Uses encode and decode method from above"""
#         input_ids, attention_mask = encode(tokenizer,question, context)
#         a =  model(torch.tensor(
#             [input_ids]), attention_mask=torch.tensor([attention_mask]))
#         start_scores = a['start_logits']
#         end_scores = a['end_logits']    
#         ans_tokens = input_ids[torch.argmax(
#             start_scores): torch.argmax(end_scores)+1]
#         answer = decode(tokenizer,ans_tokens)
#         return answer
#     return predict


# question_answering_pipeline = serverless_pipeline()
# for i in all_data:
#     context = i['news_summary']
#     question = "Can you tell me about Akshaya Tritiya"
#     answer = question_answering_pipeline(question, context)
#     if len(answer)>0:
#         print(i['news_summary'])
#     else:
#         continue


entity_list = ['EVENT','GPE', 'MONEY', 'ORG','PERSON', 'PRODUCT', 'QUANTITY', 'TIME']
def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            if str(ent.label_) in entity_list:
                print(ent.text+'-'+str(ent. start_char)+'-'+str(ent.label_))
    else:
        print('No named entities found.')

nlp = spacy.load("en_core_web_sm")
doc = nlp("What is Trump doing this days?")
labels=nlp.get_pipe("ner")
print(show_ents(doc))
