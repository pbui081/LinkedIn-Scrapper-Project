import requests
import re
from bs4 import BeautifulSoup
import sqlite3
from flask import Flask, render_template

#link to testing here

link_get = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python&location=United%2BStates&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=4339591541&position=3&pageNum=0&start=25'




"""
Helper Function that converts given link into BeautifulSoup Object for HTML parsing and writes output to txt file for debugging
Args:


"""
# Helper Function here
#link: string val that links to the linkedin site
#file_to_write: string val that represents txt file name we want to write to
def link_to_soup(link, file_to_write) -> BeautifulSoup:
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

"""
def grab_job_desc(soup_object : BeautifulSoup) -> str:
    try:
        job_description = soup_object.find(class_ = "show-more-less-html__markup")
        if(job_description is not None):
            return job_description.get_text(" ", strip=True)
        else:
            print("Error has occured looking up element")
            exit(-1)
    except:
        print("Error has occured while grabbing job description")
        exit(-1)
    pass    

def strip_tag(list_package: list) -> list:
    for i in range(len(list_package)):
        list_package[i] = list_package[i].get_text(strip=True)
    return list_package

def grab_job_points(soup_object : BeautifulSoup) :
    try:
        job_point = soup_object.find(class_="show-more-less-html__markup")
        
        if job_point:
            find_bullet_points = job_point.find_all("li")
            if find_bullet_points:
                
                return strip_tag(find_bullet_points)
            
        else:
            
            print("Error has occured looking up element")
            exit(-1)
            
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
            print("Error has occured looking up element")
            exit(-1)  
        
    except:
        print("Error has occured grabbing Company Name")
        exit(-1)

### Beautiful Soup testing below

#BeautifulSoup object that converts html file to parseable nested data structure
#soup = BeautifulSoup(get_request.text, 'lxml')

### Writing file to have a prettier html file

soup = link_to_soup(link_get, "joblist.txt")

#This is going to output a list of all the tag elements that match this regex form 
listed_span = soup.find_all(class_="base-card__full-link")

print("--------- listed span --------")
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

first_soup =  link_to_soup(first_job, "first_job_html.txt")
second_soup = link_to_soup(second_job, "second_job_html.txt")




######## This grabs the job description below 

print("__________________________________________________________")
#job 1

job_point = first_soup.find("ul", class_="show-more-less-html__markup")
if job_point:
    job_point.find_all("li")

print(grab_company_name(first_soup))
print(grab_job_points(first_soup))


print("__________________________________________________________")


#job 2 
print(grab_company_name(second_soup))




    

print("__________________________________________________________")

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
        

