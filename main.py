import requests
import re
from bs4 import BeautifulSoup


#link to testing here

link_get = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python&location=United%2BStates&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=4339591541&position=3&pageNum=0&start=25'


testing = requests.get(link_get)


### Beautiful Soup testing below

#BeautifulSoup object that converts html file to parseable nested data structure
soup = BeautifulSoup(testing.text, 'lxml')

### Writing file to have a prettier html file
job_list_html = "joblist.txt"
job_description_html = "JobDescription.txt"
with open(job_list_html, "w") as file:
    file.write(soup.prettify())

def has_href(href):
    return href.has_attr('href)')

listed_span = soup.find_all(href=re.compile("https://www.linkedin.com"))
print(listed_span)

for i in listed_span:
    print("----------- Listed Elements from Website --------------")
    #attrs grabs the attribute/attribute values from the tag
    #get grabs the specific value from the dictionary
    job_link = i.attrs.get('href')
    grabbing_job_website = requests.get(job_link)
    converting_job_link = BeautifulSoup(grabbing_job_website.text, 'lxml')

    with open(job_description_html, "w") as file:
        file.write(converting_job_link.prettify())

    job_description = converting_job_link.find_all('a', class_ = 'core-section-container')

    print("xxxxxx Job Link xxxxxx")
    print(i.attrs.get('href'))

    print("xxxxxx Grabbing the job description") 
    print(job_description)




print("------ Testing the contents of span below -----")

test = (soup.span.contents[0].strip())
test_2 = (soup.span.contents)
print(test)
print(test_2)




class LinkedInScrapper:

    #create the various lists to store the information from the website
    def __init__(self):
        #initialize a dictionary for storing job information that'll be uploaded to the database
        # we want a dictionary of a string key, and an array of strings with the information of that job
        # {string, [string]}
        job_information = {}

    


        

