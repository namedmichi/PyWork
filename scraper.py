import requests
from bs4 import BeautifulSoup
from selenium import webdriver

dr = webdriver.Chrome()
dr.get("https://de.indeed.com/jobs?q=Webentwickler&l=Rosenheim&from=search&vjk=46d4fa3719e0802b")
soup = BeautifulSoup(dr.page_source, "html.parser")


job_listings = soup.find_all('div', class_='result')

for job_listing in job_listings:
    # Extract the job title
    title_element = job_listing.find(
        'span', id=lambda x: x and x.startswith('jobTitle-'))
    job_title = title_element.text.strip()

    # Extract the company name
    company_element = job_listing.find('span', class_='companyName')
    company_name = company_element.text.strip()

    print("Job Titel:", job_title)

    print("FirmenName:", company_name)
    print("-------------------------------")

    f = open("demofile2.txt", "a")
    f.write("Job Titel:" + job_title)
    f.write("FirmenName:" + company_name)
    f.write("\n")
    f.close()
