from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import pipeline

def get_model(model):
  """Loads model from Hugginface model hub"""
  sentiment = pipeline("sentiment-analysis", model=model)
  try:
    model = AutoModelForSequenceClassification.from_pretrained(model)
    model.save_pretrained('./model')
  except Exception as e:
    raise(e)

def get_tokenizer(tokenizer):
  """Loads tokenizer from Hugginface model hub"""
  try:
    tokenizer = AutoTokenizer.from_pretrained(tokenizer)
    tokenizer.save_pretrained('./model')
  except Exception as e:
    raise(e)

get_model('finiteautomata/bertweet-base-sentiment-analysis')
get_tokenizer('finiteautomata/bertweet-base-sentiment-analysis')