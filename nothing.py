#####
## send mail from python use a different sender email
## called sender email spoofing
###

# use SMTP
import smtplib

# set username and password for the email server to connect and send mails 
username = ("isaackroeker@gmail.com")
password = ("1l1k3t0c0d3")

# set fake email sender adress and name 
fake_from = "fakename@gmail.com"
fake_name = "Fake Name"

# set email receiver email adress & name
to_email = ("isaackroeker@gmail.com")
to_name = ("coder")

# set subject
subject = "Spoofing Test "
content = "This is not from Fake Name. It is demo how to fake a sender email adress"

# build the complete email message from all variables
message = f"From: {fake_name} <{fake_from}>\nTo: {to_name} <{to_email}>\nSubject: {subject}\n\n{content}"

# show the email message for debuging
print(message)

# set the email Server and Network Port here it is gmail 
server = smtplib.SMTP("smtp.gmail.com", 587)

# set secure sending 
server.starttls()

# login into the email server
server.login(username, password)

# send the message
server.sendmail(username, to_email, message )

# close mail server connection 
server.close()