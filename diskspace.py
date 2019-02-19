import psutil
import smtplib, ssl
def send_mail(threhold):
	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	sender_email = "mailer@gmail.com"
	receiver_email = "example@gmail.com"
	password = "*****"
	message = """\
Subject: Disk Usage High

Free up the disk space. Disk usage reached to """+str(threhold)

	context = ssl.create_default_context()
	with smtplib.SMTP(smtp_server, port) as server:
	    server.ehlo()  # Can be omitted
	    server.starttls(context=context)
	    server.ehlo()  # Can be omitted
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)
def disk_usage():
	threhold=psutil.disk_usage(".").percent
	if(threhold>90):
		send_mail(threhold)
disk_usage()
