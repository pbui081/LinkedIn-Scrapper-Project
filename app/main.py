import requests
import re
from bs4 import BeautifulSoup
import sqlite3
from flask import Flask, render_template
import os

#link to testing here


#link_get = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword_input}&location=United%2BStates&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=4339591541&position=3&pageNum=0&start={increment}'


link_get = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start=25"

#keyword_input = link_get.format("Software", 25)

print("---------- Link Here ----------")

"""
Helper Function that converts given link into BeautifulSoup Object for HTML parsing and writes output to txt file for debugging
Args:


"""
# Helper Function here
#link: string val that links to the linkedin site
#file_to_write: string val that represents txt file name we want to write to
def link_to_soup(link : str, file_to_write : str) -> BeautifulSoup:
    try:
        link_request = requests.get(link)
        soup_object = BeautifulSoup(link_request.text, 'lxml') 
        with open(file_to_write, "w") as file:
            file.write(soup_object.prettify())
        return soup_object

    except:
        print("Error Occurred: link_to_soup from: ", file_to_write)
        exit(-1)
        pass

"""
Grabs the LinkedIn Job Description

Args:
    soup_object (BeautifulSoup Object): Nested HTML data structure converted by BeautifulSoup4

Expected reutrn: string type

Depecrated, grab_job_points is more built for the task needed 

"""
def grab_job_desc(soup_object : BeautifulSoup) -> str:
    try:
        job_description = soup_object.find(class_ = "show-more-less-html__markup")
        if(job_description is not None):
            return job_description.get_text(" ", strip=True)
        else:
            print("Error has occured looking up element from show-more-less-html__markup, returning empty string")
            return ""
    except:
        print("Error has occured while grabbing job description")
        exit(-1)
    pass    

"""
Helper function get strip the <tags> from <li> bullet points when finding job points
Parameters:
    list_package: list to parse through
    
returns: list value of stripped string tags
"""
def strip_tag(list_package: list) -> list:
    stripped_list = []
    for position in range(len(list_package)):
        list_package[position] = list_package[position].get_text(strip=True)
        
        if list_package[position] != '':
            stripped_list.append(list_package[position])


    return stripped_list

def grab_job_points(soup_object : BeautifulSoup) :
    try:
        job_point = soup_object.find(class_="show-more-less-html__markup")
        
        if job_point:
            find_bullet_points = job_point.find_all("li")
            if find_bullet_points:
                
                return strip_tag(find_bullet_points)
            
        else:
            
            print("Error has occured looking up element from show-more-less-html__mark, returning empty string")
            return ""
            
    except:
        print("error has occured grabbing job points in file")
        exit(-1)
        pass

def grab_company_name(soup_object : BeautifulSoup) -> str:
    try:
        company_name = soup_object.find(class_ = "topcard__org-name-link topcard__flavor--black-link")
        if(company_name is not None):
            return company_name.get_text(strip=True)
        else:
            print("Error has occured looking up element text from topcard__org-name-link topcard__flavor--black-link returning empty string")
            return ""
        
    except:
        print("Error has occured grabbing topcard__org-name-link topcard__flavor--black-link")
        exit(-1)
        
def grab_date_posted(soup_object : BeautifulSoup) -> str:
    try:
        grabbed_date = soup_object.find(class_ = "main-job-card__listdate")
        if(grabbed_date):
            return grabbed_date.get_text(strip=True)
        
        else:
            print("No information found from main-job-card__listdatem returning empty string")
            return ""
    except:
        print("No data extracted from main-job-card__listdate")
        exit(-1)
      

def grab_job_location(soup_object : BeautifulSoup) -> str:
    try:
        job_location = soup_object.find(class_ = "main-job-card__location")
        if(job_location):
            return job_location.get_text(strip=True)
        else:
            print("Error grabbing job location text from main-job-card__location, returning empty string")
            return ""
    except:
        print(" no data extracted from main-job-card__location")
        exit(-1)

def grab_position(soup_object : BeautifulSoup) -> str:
    try:
        position = soup_object.find(class_ = "description__job-criteria-text description__job-criteria-text--criteria")
        if (position):
            return position.get_text(strip=True)
        else:
            return ""
        
    except:
        
        exit(-1)

"""
Creating a dictionary of all the information from the pages of linkedin
key: company name
value: 
"""
def create_scraped_list():
    pass

"""
### Beautiful Soup testing below

#BeautifulSoup object that converts html file to parseable nested data structure
#soup = BeautifulSoup(get_request.text, 'lxml')

### Writing file to have a prettier html file
"""

soup = link_to_soup(link_get, "debug/joblist.txt")

#This is going to output a list of all the tag elements that match this regex form 
listed_span = soup.find_all(class_="base-card__full-link")

print("--------- listed job information here --------")
print(listed_span)

link_list = []

for i in listed_span:
    job_link = i.attrs.get('href') # grabs link
    link_list.append(job_link) # appends to list


job_list = []


print("--------- Now grabbing the job description from the first + second linked job ---------")
first_job = link_list[0]
second_job = link_list[1]

grabbing_job_website = requests.get(first_job)
converting_job_link = BeautifulSoup(grabbing_job_website.text, 'lxml')

first_soup =  link_to_soup(first_job, "debug/first_job_html.txt")
second_soup = link_to_soup(second_job, "debug/second_job_html.txt")


with open("/mnt/c/Users/trioa/Documents/GitHub/Website-test/app/debug/wdyny case.txt", "r") as fp:
    debug_soup = BeautifulSoup(fp, "lxml")


######## This grabs the job description below 

print("____________________________job1______________________________")
#job 1

print(grab_company_name(first_soup))
print(grab_job_points(first_soup))

print(grab_job_location(first_soup))
print(grab_date_posted(first_soup))
print(grab_position(first_soup))

print("______________________________job2____________________________")

#job 2 
print(grab_company_name(second_soup))
print(grab_job_points(second_soup))

print(grab_job_location(second_soup))
print(grab_date_posted(second_soup))
print(grab_position(second_soup))



print(job_list)

#show-more-less-html__markup to find the job description block 


class LinkedInScrapper:

    #create the various lists to store the information from the website
    def __init__(self):
        #initialize a dictionary for storing job information that'll be uploaded to the database
        # we want a dictionary of a string key, and an array of strings with the information of that job
        # {string, [string]}
        job_information = {}

    

class db: 
    def __init__(self):
        self.db = sqlite3.connect("job_info.sqlite")
        self.cursor = self.db.cursor()

        #This creates the table which we'll load up with information
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                company TEXT,      
                job_desc, TEXT,
                location TEXT,
                date_added TEXT
            )

        """)
        self.db.commit()

    def insert_information(self, company : str, job_desc : str, location : str, date_added, str):
        self.cursor.execute("""
            INSERT INTO jobs (title, company, job_desc, location, date_added)
                            
                            """)

    #This is going to delete the database in order to refresh the table with new job information
    def refresh_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS jobs")
        self.db.commit()

        self.db.close()
        

