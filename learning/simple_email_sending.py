'''
python email sending practice
MIMEText is used to write email msg
email.utils.localtime is uses to get local time
smtplib is used to send email
getpass is a safeway to input pass word
'''
from email.mime.text import MIMEText
from email.utils import localtime
import smtplib
import getpass

'''
special notice:
most email web has to open SMTP/POP by yourself in setting
after opening SMTP/POP, you should replace mypassword with serial code 
given by email web instead of your login pw.
If not, may raise 535 error
'''
myfromaddr  = input("From: ") #input email fromaddress
mypassword  = getpass.getpass("Password: ")#input email password in a safe way
mytoaddr    = input("To: ")#input email toaddress

mysmtpserver = "smtp.qq.com" #use qq email here

#official doc: MIMEText(_text,_subtype='plain',charset=None,*,policy=compat32)
mymsgcontent = "hello, through the Great Wall, we'll see a bigger world.;->"
sendtime="\nSEND TIME: " + localtime().strftime("%Y-%m-%d %H:%M:%S")
mymsg = MIMEText(mymsgcontent+sendtime,'plain','utf-8')

'''
official doc:
class smtplib.SMTP(host='',port=0,local_hostname=None,[timeout]source_address=None)
'''
serverport = 25 #SMTP default port is 25
server = smtplib.SMTP(mysmtpserver,serverport)
server.starttls() # sending email in a safe way 
server.set_debuglevel(1) # 1 for debug msg shown, 2 for level results in these messages being timestamped
server.login(myfromaddr,mypassword) 
server.sendmail(myfromaddr,[mytoaddr],mymsg.as_string())#mytoaddr is in list cause you may send email to a group
server.quit()

'''
SMTP support with statement, in with statement, no need to write quit(),cause quit() is automatically used in with statement
with smtplib.SMTP(mysmtpserver,serverport) as server:
    server.starttls()
    server.set_debuglevel(1)
    server.login(myfromaddr,mypassword)
    server.sendmail(myfromaddr,[mytoaddr],mymsg.as_string())
'''

