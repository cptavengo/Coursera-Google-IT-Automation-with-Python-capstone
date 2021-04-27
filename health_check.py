#! /usr/bin/env python3

import shutil
import psutil
import emails
import os
import socket

def main():
    percent_used = psutil.cpu_percent(1)

    space = shutil.disk_usage("/")
    remaining_percent = (space[2] / space[0])*100

    mem_used = psutil.virtual_memory()
    free_mem = mem_used[0]/10**6

    host_IP = socket.gethostbyname("localhost")

    if percent_used > 80:
        error_subject = "Error - CPU usage is over 80%"
        email_block(error_subject)
    elif remaining_percent < 20:
        error_subject = "Error - Available disk space is less than 20%"
        email_block(error_subject)
    elif free_mem < 500:
        error_subject = "Error = Available memory is less than 500MB"
        email_block(error_subject)
    elif host_IP != "127.0.0.1":
        error_subject = "Error - localhost cannot be resolved to 127.0.0.1"
        email_block(error_subject)

def email_block(error_message):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get("USER"))
    subject = error_message
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body)
    print(message)
    emails.send_email(message)


if __name__ == "__main__":
    main()
