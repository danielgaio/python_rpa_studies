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
msg['Subject'] = 'Acesse meu site pessoal'

# corpo do e-mail
html = '''
<html>
  <body>
    <p>Oi,<br>
      como você está?<br>
      <a href='https://www.danielgaio.com'> Daniel site pessoal</a><br>
      Blog de conteúdo técnico.
    </p>
  </body>
</html>
'''

part1 = MIMEText(html, 'html')
msg.attach(part1)

# servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)

# inicia conexão segura
s.starttls()
s.login(from_addr, os.environ.get('P_EMAIL_SEND'))

# prepara texto a ser enviado
text = msg.as_string()

s.sendmail(from_addr, to_addr, text)

s.quit()
