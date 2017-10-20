#!/user/bin/python3

from datetime import datetime
from subprocess import getoutput
from os import environ, getcwd
from os.path import join
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def py_mailer():
    """
    Function to obtain bash mail from /var/mail/$USER and send it in a email to specified email addr.
    """
    try:
        mail_from = ''
        mail_passwd = ''
        mail_to = ''
        mail_subj = 'bash mail {}'.format(datetime.strftime(datetime.now(), '%Y-%m-%d'))
        mail_server = 'smtp.gmail.com'
        mail_port = 587

        get_mail_cmd = 'cat /var/mail/{}'.format(environ['USER'])
        get_mail_cmd = 'cat /var/mail/$USER'
        bash_respone = getoutput(get_mail_cmd)

        if bash_respone:
            mail_body = bash_respone
        else:
            mail_body = "no mail to report at this time"

        msg = MIMEMultipart()
        msg['From'] = mail_from
        msg['To'] = mail_to
        msg['Subject'] = mail_subj
        msg.attach(MIMEText(mail_body, 'plain'))
        mail_body = msg.as_string()

        server = smtplib.SMTP(mail_server, mail_port)
        server.starttls()
        server.login(mail_from, mail_passwd)

        server.sendmail(
            from_addr=mail_from,
            to_addrs=mail_to,
            msg=mail_body,

        )
        server.quit()
    except Exception as _err:
        _msg = "main: error - type: {type} \t|\t{error}".format(
            type=type(_err).__name__,
            error=_err.args
        )
        print(_msg)
        _path = join(getcwd(), 'logs/err_{}.log'.format(datetime.strftime(datetime.now(), '%Y-%m-%d')))
        with open(_path, 'w') as _out:
            _out.write(_msg)
            _out.close()


if __name__ == '__main__':
    py_mailer()
