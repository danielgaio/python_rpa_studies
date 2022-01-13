import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# emissor e receptor do email
from_addr = 'robospython@gmail.com'
to_addr = 'robospython@gmail.com'

# criar objeto de envio de e-mail
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'E-mail de teste'

# corpo do e-mail
body = ''' R-mail enviado automaticamente pela automação. '''

msg.attach(MIMEText(body, 'plain'))

# servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)
