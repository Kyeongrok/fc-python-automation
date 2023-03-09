import os

from libs.email_sender import EmailSender

if __name__ == '__main__':
    es = EmailSender('oceanfog@naver.com', os.getenv('MY_NAVER_PASSWORD'),
                     manager_name='김미령',
                     template_filename='templates/email_template_1.html')
    es.send_all_emails('이메일리스트_with_attachment.xlsx')
