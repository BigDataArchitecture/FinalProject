from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import smtplib
import ssl
from bs4 import BeautifulSoup
import re
from nltk import tokenize
import nltk
import newsletter_data
nltk.download('punkt')

# def email(news_title,news_sentiment_score,news_sentiment_text,keywords,summary,source,image_link):
def email():
    data_columns = ["news_title","news_summary","news_top_image","news_source","news_sentiments","news_link"]
    data_dict = newsletter_data.create_data()
    print(data_dict["0"])
    # news_title = "news_title"
    # news_sentiment_score = 50
    # news_sentiment_text = "Positive"
    # summary = "summary"
    # source = "india"
    # image_link = "image_link"

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

    #     # for j in article_template:
    #     #     article_template.string.replace_with(replace[i])
    #     # i['src'] = "https://www.geo.tv/assets/uploads/updates/2022-04-30/414543_060559_updates.jpg"
    #     # print(i.find(text=re.compile("images/facebook2x.png")).replace_with("Parth"))
    # # article_template.string.replace_with('Bar')



    # # new_text=article_template.find(text=re.compile("images/facebook2x.png")).replace_with("Parth")
    # # print(new_text)

    html = soup

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    sender_email = "bigdat517+1@gmail.com" # TODO: replace with your email address
    receiver_email = ["parth981@gmail.com","shah.parth3@northeastern.edu","parigi.s@northeastern.edu","samanta.an@northeastern.edu"] # TODO: replace with your recipients
    password = 'syhrkmppaptdfdds'  # TODO: replace with your 16-digit-character password 

    # initialise message instance
    msg = MIMEMultipart()
    msg["Subject"] = "Top 5 News,📰 you should know!"
    msg["From"] = sender_email
    msg['To'] = ""

    html = soup    
    # '<html><body><style> .intro{ width: 360px;border: 3px solid #1DA1F2; padding: 10px;}</style><div class="intro"><p style="font-family:Times New Roman; color: ' + change(news_sentiment_text, color = True)+'; font-size: 20px;">' + change(news_sentiment_text, color = False) + " "+ news_sentiment_score + "%"  + '</p>'+ keywords + '<h1>'+ news_title + '</h1><p style = "text-align: justify;text-justify: inter-word;">'+summary +'<p>' + '📍' + '<i><u>' + country + '</i></u>'+' ℹ️ ' + source + '</div></body></html>'
    part2 = MIMEText(html, "html")

    #body_html = MIMEText(text, 'plain')  # parse values into html text
    #msg.attach(part1)  # attaching the text body into msg
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
