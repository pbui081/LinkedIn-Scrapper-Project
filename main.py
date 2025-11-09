import requests
from bs4 import BeautifulSoup


#link to testing here

#https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?trk=guest_homepage-basic_guest_nav_menu_jobs&start=100

link_get = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?trk=guest_homepage-basic_guest_nav_menu_jobs&start=100'


testing = requests.get(link_get)


### Beautiful Soup testing below

#BeautifulSoup object that converts html file to parseable nested data structure
soup = BeautifulSoup(testing.text, 'lxml')

### Writing file to have a prettier html file
testing_file = "testing_file.txt"
with open(testing_file, "w") as file:
    file.write(soup.prettify())

print(soup.find_all('span', class_ = "sr-only"))

print("-----------")

test = (soup.span.contents[0].strip())
test_2 = (soup.span.contents)
print(test)
print(test_2)

