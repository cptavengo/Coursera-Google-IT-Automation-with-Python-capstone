#! /usr/bin/env python3

import os
import datetime
import reports
import emails
import re
import json

def get_name_weight():
    cwd = os.getcwd()
    data = os.listdir(cwd)
    pdf_list = []
    for files in data:
        regex = r"(json)"
        json_search = re.search(regex, files)
        if json_search is None:
            continue
        json_search = json_search.groups()
        if json_search[0] == "json":
            with open(files) as json_file:
                json_data = json.load(json_file)
                pdf_list_2 = [json_data["name"], json_data["weight"]]
                pdf_list.append(pdf_list_2)
    return(pdf_list)

def main(list):
    final_fruit_entry = ""
    for i in range(len(list)):
        fruit_name = "name: " + list[i][0] + "<br/>"
        fruit_weight = "weight: " + str(list[i][1]) + " lbs" + "<br/>"
        fruit_entry = fruit_name + fruit_weight + "<br/>"
        final_fruit_entry += fruit_entry
    d = datetime.date.today()
    reports.generate_report("processed.pdf", "Processed Update on " +
                           d.strftime("%B %d, %Y"), final_fruit_entry)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get("USER"))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
    message = emails.generate_email(sender, receiver, subject, body, "processed.pdf")
    emails.send_email(message)

if __name__ == "__main__":
    main(get_name_weight())
