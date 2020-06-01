import requests
from requests_html import HTMLSession

url = 'https://www.similarweb.com/website/superpharm.pl'

try:
    session = HTMLSession()
    r = session.get(url)
except requests.exceptions.RequestException as e:
    print(e)

get_engagement_values = r.html.find('.engagementInfo-valueNumber')

engagement_names = {'Total Visits': '', 'Bounce Rate': '', 'Avg. Visit Duration': '', 'Pages per Visit': ''}

engagement_values = []

for i in range(len(get_engagement_values)):
    engagement_values.append(get_engagement_values[i].text)

engagement = dict(zip(engagement_names, engagement_values))

print(engagement)