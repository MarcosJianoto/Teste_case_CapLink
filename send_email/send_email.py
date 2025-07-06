import smtplib
from email.message import EmailMessage
import mimetypes
from send_email.variables_necessary import *

msg = EmailMessage()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject
msg.set_content(message)


def sending_email(name_arquive):
    try:
        path_name_archive = f"{name_folder}/{name_arquive}"

        mime_type, _ = mimetypes.guess_type(path_name_archive)

        if (mime_type is None):
            mime_type = 'application/octet-stream'

        mime_type, mime_subtype = mime_type.split('/')

        with open(path_name_archive, 'rb') as archive:
            msg.add_attachment(archive.read(), maintype=mime_type,
                               subtype=mime_subtype, filename=path_name_archive)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email:
            email.login(sender, password_google)
            email.send_message(msg)

        return True

    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return False
