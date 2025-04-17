import requests #Used to make HTTP requests to web pages
from bs4 import BeautifulSoup #Used to parse and navigate the HTML
import pprint #Used to print the output in a cleaner format

#Making the requests for the first and second page
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

#Parse the HTML content
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

#Getting the articles title, links and subtext which is the votes, username
links = soup.select('.titleline > a') 
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a') 
subtext2 = soup2.select('.subtext')

#Merges both page 1 and page 2 of Hacker News
mega_links = links + links2
mega_subtext = subtext + subtext2

#Function to sort the list after extracting all the wanted data
def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

#Function to get the information relevant to us
def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)
 #Print final list
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
