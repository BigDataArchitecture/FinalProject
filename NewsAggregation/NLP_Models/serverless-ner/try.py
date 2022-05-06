import json
from transformers import pipeline

ner = pipeline("ner", model='./model', tokenizer='./model')

