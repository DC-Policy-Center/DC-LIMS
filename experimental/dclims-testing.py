import requests
import json
def advancedSearch(**kwargs):
    '''Advanced search into Legislation. Expects a LegislationSearchCriteria in the
    request body. The search criteria can include various combinations to search for
    Legislation that match. RowLimit limits the number of results. Offset defines
    the starting record in the result recordset.'''



    verbose = kwargs.get('verbose',False)
    try: kwargs.pop('verbose')
    except: pass
    rowLimit = kwargs.get('rowLimit')
    try: kwargs.pop('rowLimit')
    except: pass
    offSet = kwargs.get('offSet')
    try: kwargs.pop('offSet')
    except: pass


    q = kwargs
    head = {'content-type':'application/json'}     #Requests JSON response
    #Building API call from request building
    website = 'http://lims.dccouncil.us/api/v1/Legislation/AdvancedSearch?%s'%(rowLimit)
    if(verbose == True):print('WEBSITE: '+ str(website))
    #Sending POST request
    response = requests.get(website,data=json.dumps(q),headers=head)
    if(verbose == True):print('RESPONSE: '+ str(response))
    return(response)


options = {
            'StartDate': "02-14-2019",
            #api wrapper call options section
            'verbose':True,
            #api call options section
            'offSet':'0',
            'rowLimit':'100',
}


csvHeader = []
csvHeader.append('Introducer') #Initialize empty list for headers for CSV writing
dataHeaders = [     'Id','CouncilPeriod','ShortTitle','Introducer',
                    'LegislationNumber','LawNumber','ActNumber',
                    'IntroductionDate','Modified','CommitteeReferral',
                    'CommitteeReferralComments','Deemed','DeemedOn',
                    'LegislationStatus','Category','Subcategory','DocumentUrl']
introducerException = 0



# Using API helper to send POST request to LIMS

response = advancedSearch(**options)
data_json = response.json()
