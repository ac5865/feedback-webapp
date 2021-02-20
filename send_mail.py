import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port= 2525
    smtp_server = 'smtp.mailtrap.io'
    login ='ac5865'
    password ='Brg@2961'
    message = f"<h3> New Feedback Submission</h3>
    <ul>
    <li>Customer: {customer}</li>
    <li>Dealer: {dealer}</li>
    <li>Ratings: {rating}</li>
    <li>Comments: {comments}</li></ul>"

    sender_email = 'email@example.com'
    receiver_email ='anushkachoudhary.ac@gmail.com'
    msg=MIMEText(message, 'html')
    msg['Subject']='Feedback'
    msg['From']=sender_email
    msg['To']=receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.send_message(sender_email, receiver_email, msg.as_string())