'''
This is the preliminary work for an API wrapper.  This API wrapper will call the
D.C. LIMS API system, streamlining the calls.

Dependencies: Requests;
API help from DC Council Website:http://lims.dccouncil.us/api/Help


|Signature-------------------------------------------|
|Written for DC Policy Center by Michael Watson; 2017|
|www.DCPolicyCenter.org / DC-Policy-Center.github.io |
|github:M-Watson & MW-DC-Policy-Center               |
|----------------------------------------------------|
'''

#Requests is used for all of the API calls.
import requests, json
from bs4 import BeautifulSoup as bs
def topLevelTest(toPrint):
    print(toPrint)
    return(toPrint)

class get:
#*****************************************************************************#
    def latestLaws(rowLimit,**kwargs):
        '''GETs latest legislation that have been made into official laws'''

        q = {}
        verbose = kwargs.get('verbose',False)
        head = {'content-type':'application/json'}


        website = 'http://lims.dccouncil.us/api/v1/Legislation/LatestLaws?%s'%(rowLimit)
        if(verbose == True):print('GET- Latest Laws')
        response = requests.get(website,data=json.dumps(q),headers=head)
        if(verbose == True):print('RESPONSE: '+ str(response))
        return(response)

class calendar:
    page_number = 1
    url = "http://dccouncil.us/events/list/?tribe_paged=%s"%page_number

    re = request.get(url)

    soup = bs(re.content,"lxml")

    calendar_date = soup.find("div",{'class':'listing-header__subhead'})
    articles = soup.find_all('article')
    ul_list = []
    for article in articles:
        ul_list.append(article.ul)

'''  *****************        APPENDICES   *************************
                    I.Changes to look into or needed
                    II.
                    III.
                    IV.

*****************        END APPENDICES   *************************'''
