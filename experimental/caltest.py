import requests
from bs4 import BeautifulSoup as bs
import re
import time

date = time.strftime("%m-%d-%y")

page_number = 1
file_name = 'out-{}.tsv'.format(date)



#headers = 'index\tcommittee\tsubject\tdate\n'
#headers_list = ['index','committee','subject','date']

headers = 'index\tcommittee\tdate\tsubject\n'
headers_list = ['index','committee','date','subject']


with open(file_name,'w') as f:
    f.write(headers)

for page in range(4):

    print(page_number)
    url = "http://dccouncil.us/events/list/?tribe_paged=%s"%str(page_number)

    res = requests.get(url)

    soup = bs(res.content,"lxml")

    calendar_date = soup.find("div",{'class':'listing-header__subhead'})
    articles = soup.find_all('article')
    ul_list = []
    hearing_dict = {}
    article_number = 0
    article_dict_list = []
    for article in articles:
        article_number +=1
        date = 'missing-date'
        committee = 'missing-committee'
        subject = 'missing-subject'


        date = article.time
        #date = re.match(r"<time datetime=\"(.*)\+0000",str(date))
        date = re.match(r"<time datetime=\"(.*)\-0400",str(date))
        try:
            date = date.group(1)
        except:
            date = 'NONETYPE'

        try:
            committee = article.a['title']
        except:
            committee = 'missing-committee'

        subj_list = []
        try:
            for item in article.ul:
                for item_2 in item:
                    if item_2 != '\n':

                        try:
                            searching = re.search(r"<a href=\"(.*)\">",str(item_2))
                            new_subj = searching.group(1)
                        except:
                            new_subj = item_2

                        '''
                        if '/Legislation/' in str(new_subj):
                            print('test' + str(new_subj))
                            new_subj = re.match(r"\</a>\,(.*)\</span\>",str(new_subj))
                            print(new_subj.group(1))
                            '''
                        subj_list.append(new_subj)
        except: subj_list = ['NoneType']

        subject = subj_list #article.ul

        hearing_dict={
            'index':article_number,
            'committee':committee,
            'subject':subject,
            'date':date}
        article_dict_list.append(hearing_dict)
        #print(article_dict_list)
        ul_list.append(article.ul)


    with open(file_name,'a') as f:
        for line in article_dict_list:

            for key in headers_list:
                '''
                if key == headers_list[len(headers_list)-1]:
                    output = str(line[key])
                    f.write(output)
                    f.write('\n')
                    '''
                if key == 'subject':
                    output = '\n'
                    f.write(output)
                    for item in line[key]:
                        #print(item)
                        output = '\t\t\t' + str(item) + '\n'
                        f.write(output)
                else:
                    output = str(line[key]) + '\t'
                    f.write(output)
    page_number += 1
