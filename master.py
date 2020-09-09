import time
import os
import smtplib, ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from job import job


def find_available_jobs_from_site():
    """ Finds and returns job information within the webpage."""
    site_url = "http://aesoponline.com/"
    username = "CASawyer"
    password = "Alex0602!"

    driver = webdriver.Chrome()
    driver.get(site_url)

    # Wait for login page to load, then login.
    username_element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "Username"))
    )
    password_element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "Password"))
    )
    time.sleep(2)
    username_element.send_keys(username)
    password_element.send_keys(password)
    driver.find_element_by_id("qa-button-login").click()

    # Pull the available jobs
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "tabs")))
    time.sleep(3)
    available_jobs_element = driver.find_element_by_id("availableJobsTab")
    num_of_jobs_element = available_jobs_element.find_element_by_tag_name("span")
    num_of_jobs = int(num_of_jobs_element.text)

    if num_of_jobs > 0:
        available_jobs_element = driver.find_element_by_id("availableJobs")
        job_table_element = available_jobs_element.find_element_by_tag_name("table")
        all_job_elements = job_table_element.find_elements_by_tag_name("tbody")
        list_of_job_objects = []

        for job_element in all_job_elements:
            summary_element = job_element.find_element_by_class_name("summary")
            detail_element = job_element.find_element_by_class_name("detail")

            # Teacher name, title, and report to are within summary.
            teacher_name = summary_element.find_element_by_class_name("name").text
            teacher_title = summary_element.find_element_by_class_name("title").text
            report_to = summary_element.find_element_by_class_name("reportToLocation").text

            # Rest of info is in detail element.
            start_date = detail_element.find_element_by_class_name("itemDate").text
            end_date = detail_element.find_element_by_class_name("multiEndDate").text
            if end_date == "":
                end_date = start_date
            start_time = detail_element.find_element_by_class_name("startTime").text
            end_time = detail_element.find_element_by_class_name("endTime").text
            duration_name = detail_element.find_element_by_class_name("durationName").text
            location = detail_element.find_element_by_class_name("locationName").text
            list_of_job_objects.append(job(teacher_name, teacher_title, report_to, start_date, end_date,
                                           start_time, end_time, duration_name, location))

        return list_of_job_objects
    else:
        # If there are no available jobs, quit all execution right here.
        exit()


def format_message_from_job_info(list_of_available_jobs):
    """ This method will take the list job objects, and return a message about them that can be sent. """
    message = str(len(list_of_available_jobs)) + " jobs available" + os.linesep + os.linesep

    for available_job in list_of_available_jobs:
        message += available_job.get_string_rep_of_job() + os.linesep + os.linesep

    return message


def send_email(message):
    """ Sends an email to Christyl"""
    port = 465  # For SSL
    sender_email_address = "throwfake1212@gmail.com"
    to_email_address = "christyl.acosta@gmail.com"
    smtp_server = "smtp.gmail.com"
    password = "Christyl0602@"

    # Create a secure SSL context
    context = ssl.create_default_context()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email_address, password)
        server.sendmail(sender_email_address, to_email_address, message)


def master():
    """Master execution method for Christyl bot."""
    print("Starting master execution")
    list_of_available_jobs = find_available_jobs_from_site()
    message = format_message_from_job_info(list_of_available_jobs)
    # If you cannot get the below to work, then just send an email instead, in the send email method.
    print(message)
    send_email(message)


if __name__ == '__main__':
    master()
