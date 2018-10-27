# import the smtplib module. It should be included in Python by default
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# set up the SMTP server

class Eroica_SMTP:
    MY_ADDRESS = 'eroicamildmayredirector@outlook.com';
    ER_INFO = 'twoodhouse97@gmail.com';
    PASSWORD = 'wun-7hm-LXT-y25';

    try:
        eroica_server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        eroica_server.starttls();
        eroica_server.login(MY_ADDRESS, PASSWORD);
    except:
        print('not connected to outlook server')


    def send_mail(self,origin_name,origin_email,message_body):
        msg = MIMEMultipart()       # create a message

        # setup the parameters of the message
        msg['From']=self.MY_ADDRESS
        msg['To']=self.ER_INFO
        msg['Subject']="MESSAGE FROM "+origin_name;
        mess_header = 'MESSAGE FROM: '+origin_name+' \n\n contact details: '+origin_email+'\n\n Message: \n\n';
        message = mess_header + message_body;

        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        self.eroica_server.send_message(msg)

        del msg

        print('SENT THE MAIL.')
