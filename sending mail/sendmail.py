import smtplib
import getpass

def prompt(prompt):
    return raw_input(prompt).strip()
fromaddr=prompt("From: ")
toaddrs=prompt("To: ").split()
username=raw_input("User Name: ")
password=getpass.getpass("Password: ")
print "ENter message, end with ^D(unix) or ^Z(WIndows):"

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while 1:
    try:
        line = raw_input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print "Message length is " + repr(len(msg))

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg)
    print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"



