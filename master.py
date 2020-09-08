import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def find_job_information_from_site():
    """Finds and returns job information within the webpage."""
    site_url = "http://aesoponline.com/"
    username = "CASawyer"
    password = "Alex0602!"

    driver = webdriver.Chrome()
    driver.get(site_url)

    # Wait for login page to load, then login.
    username_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Username"))
    )
    password_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Password"))
    )
    time.sleep(2)
    username_element.send_keys(username)
    password_element.send_keys(password)
    driver.find_element_by_id("qa-button-login").click()




def format_message_from_job_info(job_info):
    raise NotImplementedError


def send_text_message(message):
    raise NotImplementedError


def send_email(message):
    raise NotImplementedError


def master():
    """Master execution method for Christyl bot."""
    print("Starting master execution")
    job_info = find_job_information_from_site()
    message = format_message_from_job_info(job_info)
    # If you cannot get the below to work, then just send an email instead, in the send email method.
    send_text_message(message)


if __name__ == '__main__':
    master()
