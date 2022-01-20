import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

# emissor e receptor do email
from_addr = os.environ.get('EMAIL_SEND')
to_addr = os.environ.get('EMAIL_RECEIVE')

# criar objeto de envio de e-mail
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Venha conhecer nosso restaurante!'

# corpo do e-mail
body = '''
  Este é o texto do corpo do e-mail.
'''

msg.attach(MIMEText(body, 'plain'))

# anexo
file_name = 'Panfleto.pdf'
anexo = open(file_name, 'rb')

# preparar objeto de anexo
payload = MIMEBase('application', 'octet-stream')
payload.set_payload((anexo).read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition',
                   'attachment; filename={}'.format(file_name))

msg.attach(payload)

# servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)

# inicia conexão segura
s.starttls()
s.login(from_addr, os.environ.get('P_EMAIL_SEND'))

# prepara texto a ser enviado
text = msg.as_string()

s.sendmail(from_addr, to_addr, text)

s.quit()
