'''
Email Automation file for our newsletter
This module consist for automated email generation which loads our html tempelate and replaces the tags which we have mentioned 
with the custom news from our "newsletter_data" file

Author Parth Shah shah.parth3@northeastern.edu'
Created at 4th May 2022
'''

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
from bs4 import BeautifulSoup
import re
from nltk import tokenize
import nltk
import newsletter_data
nltk.download('punkt')
import pandas as pd

def email(country = "India ",topic = "Business"):
    '''
    This Function loads the data from our newsletter_data module and makes the template for our newsletter
    This is a customized function which takes in country and topic as input and select the data likewise
    Parameters:
    ---------------------
    country: string
        Name of the country for which news should be fetched
        Default: India🇮🇳
    topic: string
        Topic of the news for which news should be fetched
        Default: Business
    '''
    data_columns = ["news_title","news_summary","news_top_image","news_source","news_sentiments","news_link"]
    data_dict = newsletter_data.create_data(country,topic)

    template = open('NewsAggregation/Newsletter/beefree-lhj0o8hryao.html')
    soup = BeautifulSoup(template.read(), "html.parser")
    for k in range(1,7):
        news_title = data_dict[str(k-1)][data_columns[0]+str(k)]
        news_sentiment_score = data_dict[str(k-1)][data_columns[4]+str(k)][0]['score']
        news_sentiment_text = data_dict[str(k-1)][data_columns[4]+str(k)][0]['label']
        summary = data_dict[str(k-1)][data_columns[1]+str(k)]
        source = data_dict[str(k-1)][data_columns[3]+str(k)]
        image_link = data_dict[str(k-1)][data_columns[2]+str(k)]
        news_link = data_dict[str(k-1)][data_columns[5]+str(k)]
        if k in [2,3]:
            a = tokenize.sent_tokenize(summary)
            summary = a[0]
        tags = ['newstitle'+str(k),'newssummary'+str(k),'newsimage'+str(k),'newsauthor'+str(k),'newssentiments'+str(k),'newslink'+str(k)]
        replace = [news_title,summary,image_link,source,str(round(news_sentiment_score,2)*100) + "% " + news_sentiment_text,news_link]
        for i in range(len(tags)):
            try:
                print(tags[i])
                article_template = soup.find(id=tags[i])
                print(article_template)
                if tags[i] == 'newsimage'+str(k):
                    article_template['src'] = image_link
                if tags[i] == 'newslink'+str(k):
                     article_template['href'] = news_link
                else:
                    for j in article_template:
                        article_template.string.replace_with(replace[i])
            except:
                continue

    html = soup

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    sender_email = "bigdat517+1@gmail.com" 
    receiver_email =  "parth981@gmail.com" #shah.parth3@northeastern.edu","parigi.s@northeastern.edu","samanta.an@northeastern.edu"
    password = 'syhrkmppaptdfdds' 

    # initialise message instance
    msg = MIMEMultipart()
    msg["Subject"] = "Top 5 News,📰 you should know!"
    msg["From"] = sender_email
    msg['To'] = ""

    html = soup    
    part2 = MIMEText(html, "html")

    msg.attach(part2)

    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # check connection
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # check connection
        server.login(sender_email, password)

        # Send email here
        server.sendmail(sender_email, receiver_email, msg.as_string())

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

if __name__ == '__main__':
    email()
