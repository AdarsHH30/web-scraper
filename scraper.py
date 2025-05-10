from bs4 import BeautifulSoup
import requests
import time

print("Enter the Job that you need to find :")
job_name = input("")
page_no = 1
web_page = requests.get(
    f"https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords={job_name}&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&pDate=I&sequence={page_no}&startPage=1"
).text

start_time = time.time()
soup = BeautifulSoup(web_page, "lxml")

jobs_ = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

count = 0


def find_job():
    global count
    print("--------------------------------------------------------")
    for jobs in jobs_:
        print(f"Job Number : {count + 1}")
        count += 1
        job_header = jobs.header.div
        job_title = job_header.h2.text
        job_title = " ".join(job_title.split())
        job_link = job_header.a["href"]
        job_description = jobs.find("ul", class_="list-job-dtl clearfix").text
        job_description = " ".join(job_description.split())
        skill_required = jobs.find("ul", class_="list-job-dtl clearfix").div.find_all(
            "span"
        )
        place = jobs.find("li", class_="srp-zindex location-tru").text.strip("")

        print(f"Job Title : {job_title}")
        print(f"Job Link : {job_link}")
        print(f"Job Description : {job_description}")
        print(f"Skill Required is :", end=" ")
        print(",".join([skill.text.strip() for skill in skill_required]))
        print("\n\n")
    print("--------------------------------------------------------")


# print(f"Skill Required : {skill}")
# print(f"Skill Required : {skill}")
# print(f"Location : {place}")
# print("--------------------------------------------------------")


while True:
    if count >= 3000:
        # print("3000 Jobs Found")
        break
    try:
        web_page = requests.get(
            f"https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords={job_name}&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&pDate=I&sequence={page_no}&startPage=1"
        ).text
        soup = BeautifulSoup(web_page, "lxml")
        jobs_ = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
        page_no += 1
        if len(jobs_) == 0:
            break
        find_job()
    except Exception as e:
        # print(e)
        break

end_time = time.time()

print(f"Total Time Taken : {end_time - start_time} seconds")
print(f"Total Jobs Found : {count}")
print("--------------------------------------------------------")
