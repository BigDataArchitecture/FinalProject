from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import smtplib
import ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls

sender_email = "bigdat517+1@gmail.com" # TODO: replace with your email address
receiver_email = ["bigdat517+1@gmail.com"] # TODO: replace with your recipients
password = 'syhrkmppaptdfdds'  # TODO: replace with your 16-digit-character password 

# initialise message instance
msg = MIMEMultipart()
msg["Subject"] = "Test email"
msg["From"] = sender_email
msg['To'] = ", ".join(receiver_email)

## Plain text
# text = """\
# Hi,
# How are you?
# This is a test email"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
    </p>
  </body>
</html>
"""
#part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
# body_text = MIMEText(text, 'plain')  # 
# msg.attach(body_text)  # attaching the text body into msg

# html = """\
# <html>
#   <body>
#     <p>Hi,<br>
#     <br>
#     Hi me! This is a test email for the project report. <br>
#     Thank you. <br>
#     </p>
#   </body>
# </html>
# """

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