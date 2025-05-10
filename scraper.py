from bs4 import BeautifulSoup
import requests
import time
from colorama import init, Fore, Style

print(f"Enter the Job that you need to find :")
job_name = input(f"{Fore.GREEN}>>  {Style.RESET_ALL}")
init()

print(
    f"\nEnter the Number of Job pages that you need to find ",
    end="",
)
print(f"{Fore.RED}( Note : 1 page contains 25 jobs ){Style.RESET_ALL}:")
try:
    job_count = int(input(f"{Fore.GREEN}>>  {Style.RESET_ALL}"))
except Exception as e:
    print(f"{Fore.RED}Please enter a valid number{Style.RESET_ALL}")
    exit(0)
print(f"\nSearching for Jobs...")
json_file = open(f"Jobs/{job_name}_jobs.json", "w")
json_file.write("[")
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

    for jobs in jobs_:
        if count:
            json_file.write(",")
        # print(f"Job Number : {count + 1}")
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
        skill_required = [
            skill.text.strip() for skill in skill_required if skill.text.strip()
        ]
        place = jobs.find("li", class_="srp-zindex location-tru").text.strip()
        json_file.write("{")
        json_file.write(f'"Job Title" : "{job_title}",')
        json_file.write(f'"Job Link" : "{job_link}",')
        json_file.write(f'"Job Description" : "{job_description}",')
        json_file.write(f'"Skill Required" : "{",".join(skill_required)}",')
        json_file.write(f'"Location" : "{"".join(place.split())}"')
        json_file.write("}")
        json_file.write("\n\n")


while True:
    if job_count < page_no:
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

json_file.write("]")
json_file.close()
print(f"\n\n{Fore.GREEN}Job Search Completed{Style.RESET_ALL}\n\n")
print(
    f"Total Time Taken : {Fore.GREEN}{end_time - start_time} seconds {Style.RESET_ALL}"
)
print(f"Total Jobs Found :{Fore.GREEN} {count} {Style.RESET_ALL}")
print(
    f"You can find the jobs in {Fore.GREEN}Jobs/{job_name}_jobs.json{Style.RESET_ALL}"
)
print("--------------------------------------------------------")
