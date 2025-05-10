from bs4 import BeautifulSoup
import requests


# print("Enter the Job that you need to find :")
job_name = "python"
web_page = requests.get(
    f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords={job_name}&txtLocation="
).text

soup = BeautifulSoup(web_page, "lxml")

jobs = soup.find("li", class_="clearfix job-bx wht-shd-bx")


def find_job():
    job_header = jobs.header.div
    job_title = job_header.h2.text
    job_link = job_header.a["href"]
    job_description = jobs.find("ul", class_="list-job-dtl clearfix").text.replace(
        "\n", ""
    )
    skill_required = jobs.find("ul", class_="list-job-dtl clearfix").div.find_all(
        "span"
    )
    place = jobs.find("li", class_="srp-zindex location-tru").text.strip("")
