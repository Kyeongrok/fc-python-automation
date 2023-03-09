import os
import smtplib
from email.mime.text import MIMEText


class EmailSender:
    email_addr = None
    password = None
    smtp_server_map = {
        'gmail.com':'smtp.gmail.com',
        'naver.com':'smtp.naver.com'
    }
    smtp_server = None

    def __init__(self, email_addr, password):
        print('생성자')
        self.email_addr = email_addr
        self.password = password
        self.smtp_server = email_addr.split('@') # fc.krkim@gmail.com
        print(self.smtp_server)

    def send_email(self, msg, from_addr, to_addr):
        """
        :param msg: 보낼 메세지
        :param from_addr: 보내는 사람
        :param to_addr: 받는 사람
        :return:
        """
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            msg = MIMEText(msg)
            msg['From'] = from_addr
            msg['To'] = to_addr
            msg['Subject'] = '메일 발송 테스트'
            print(msg.as_string())

            smtp.starttls()
            smtp.login(self.email_addr, self.password)
            smtp.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg.as_string())
            smtp.quit()
        print('이메일 전송이 완료 되었습니다.')

if __name__ == '__main__':
    es = EmailSender('fc.krkim@gmail.com', os.getenv('MY_GMAIL_PASSWORD'))
    # es = EmailSender('oceanfog@naver.com', os.getenv('MY_NAVER_PASSWORD'))
    es.send_email('테스트 입니다.\n 네이버 이메일에서 보냄', from_addr='oceanfog@naver.com', to_addr='fc.krkim@gmail.com')