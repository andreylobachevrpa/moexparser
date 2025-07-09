import smtplib
import config
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime, timedelta
from modules.browser import Browser
from modules.excel import Excel


def get_previous_month_info():
    """Метод для получения дат"""
    current_date= datetime.now()
    first_day_current_month = current_date.replace(day=1)
    last_day_previous_month = first_day_current_month - timedelta(days=1)
    first_day_previous_month = last_day_previous_month.replace(day=1)
    return {
        'first_day': str(first_day_previous_month.day),
        'last_day': str(last_day_previous_month.day),
        'month_number': last_day_previous_month.strftime('%m'),
        'year': str(last_day_previous_month.year)
    }
    
def send_email(file_path, email_body, email_to='andreylobachev.forstudy@gmail.com',login_smtp=config.login_smtp,password_smtp=config.password_smtp):  
    file_name = Path(file_path).name
    msg = MIMEMultipart()
    msg['From'] = login_smtp
    msg['To'] = email_to
    msg['Subject'] = 'Отчёт по валютам'
    msg.attach(MIMEText(email_body, 'plain'))     
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())      
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={file_name}",
    )
    msg.attach(part)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(login_smtp, password_smtp)
        server.send_message(msg)      

def test():
    browser = Browser()
    browser.open_browser()
    browser.acceptance_agreement()
    month_info = get_previous_month_info()
    browser.currency_and_date_selection(currency_type='USD/RUB',month_info=month_info) 
    usd_data = browser.get_data()
    browser.currency_and_date_selection(currency_type='JPY/RUB',month_info=month_info)
    jpy_data = browser.get_data()
    excel = Excel()
    excel_filepath = excel.create_excel_file(usd_data, jpy_data)
    email_body = excel.get_info(excel_filepath)
    send_email(excel_filepath, email_body)

if __name__ == '__main__':
    test()