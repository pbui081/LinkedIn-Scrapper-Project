import requests
import re
from bs4 import BeautifulSoup


#link to testing here

link_get = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python&location=United%2BStates&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=4339591541&position=3&pageNum=0&start=25'


get_request = requests.get(link_get)

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
        print("Error Occurred")
        exit(-1)
        pass


def grab_soup_attributes():
    pass

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




print("--------- Now grabbing the job description from the first + second linked job ---------")
first_job = link_list[0]
second_job = link_list[1]

print(link_list)

grabbing_job_website = requests.get(first_job)
converting_job_link = BeautifulSoup(grabbing_job_website.text, 'lxml')

first_soup =  link_to_soup(first_job, "first_job_html.txt")
second_soup = link_to_soup(second_job, "second_job_html.txt")

print("__________________________________________________________")
#job 1
job_desc = first_soup.find(class_ = "show-more-less-html__markup")
job_desc_all = first_soup.find_all(class_ = "show-more-less-html__markup")

print(job_desc)
# when using .find() and accessing the attribute of the results, we must ensure that the members of the object
# are to be non-None, when using find_all(), it is guaranteed to return a type of something. 
if job_desc is not None:
    print(type(job_desc.attrs.get('p')))
else:
    print("none found")
print(type(job_desc_all[0]).attrs.get('p'))
print(type(first_soup))


print("__________________________________________________________")



#show-more-less-html__markup to find the job description block 


class LinkedInScrapper:

    #create the various lists to store the information from the website
    def __init__(self):
        #initialize a dictionary for storing job information that'll be uploaded to the database
        # we want a dictionary of a string key, and an array of strings with the information of that job
        # {string, [string]}
        job_information = {}

    


        

