import requests
from requests_html import HTMLSession

url = 'https://www.similarweb.com/website/superpharm.pl'

try:
    session = HTMLSession()
    r = session.get(url)
except requests.exceptions.RequestException as e:
    print(e)

engagement_names = ('Total Visits', 'Avg. Visit Duration', 'Pages per Visit', 'Bounce Rate')
traffic_sources_names = ('Direct', 'Referrals', 'Search', 'Social', 'Email', 'Display')

get_engagement_values = r.html.find('.engagementInfo-valueNumber')
get_traffic_sources_values = r.html.find('.trafficSourcesChart-value')


engagement_values = []

for i in range(len(get_engagement_values)):
    engagement_values.append(get_engagement_values[i].text)

engagement = dict(zip(engagement_names, engagement_values))

traffic_sources_values = []

for i in range(len(get_traffic_sources_values)):
    traffic_sources_values.append(get_traffic_sources_values[i].text)

traffic_sources = dict(zip(traffic_sources_names, traffic_sources_values))

print(engagement)
print(traffic_sources)