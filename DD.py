# -*- coding: utf-8 -*-
from colorama import init, Fore, Back, Style
from KW import *
from newspaper import Article

import csv
import itertools
import json
import os
import re
import requests
import urllib3


os.environ['no_proxy'] = '*'
init(convert=True)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print(Fore.YELLOW + """
  ______   __    __  ________      _______   ______  __        ______   ______   ________  __    __   ______   ________
/       \ /  |  /  |/        |    /       \ /      |/  |      /      | /      \ /        |/  \  /  | /      \ /        |
$$$$$$$  |$$ |  $$ |$$$$$$$$/     $$$$$$$  |$$$$$$/ $$ |      $$$$$$/ /$$$$$$  |$$$$$$$$/ $$  \ $$ |/$$$$$$  |$$$$$$$$/
$$ |  $$ |$$ |  $$ |$$ |__        $$ |  $$ |  $$ |  $$ |        $$ |  $$ | _$$/ $$ |__    $$$  \$$ |$$ |  $$/ $$ |__
$$ |  $$ |$$ |  $$ |$$    |       $$ |  $$ |  $$ |  $$ |        $$ |  $$ |/    |$$    |   $$$$  $$ |$$ |      $$    |
$$ |  $$ |$$ |  $$ |$$$$$/        $$ |  $$ |  $$ |  $$ |        $$ |  $$ |$$$$ |$$$$$/    $$ $$ $$ |$$ |   __ $$$$$/
$$ |__$$ |$$ \__$$ |$$ |_____     $$ |__$$ | _$$ |_ $$ |_____  _$$ |_ $$ \__$$ |$$ |_____ $$ |$$$$ |$$ \__/  |$$ |_____
$$    $$/ $$    $$/ $$       |    $$    $$/ / $$   |$$       |/ $$   |$$    $$/ $$       |$$ | $$$ |$$    $$/ $$       |
$$$$$$$/   $$$$$$/  $$$$$$$$/     $$$$$$$/  $$$$$$/ $$$$$$$$/ $$$$$$/  $$$$$$/  $$$$$$$$/ $$/   $$/  $$$$$$/  $$$$$$$$/

by Lorenzo Romani - @lorenzoromani

""")

#put your Zenserp tokens in this list:
tokens = ['PASTE YOUR TOKEN(S) HERE']
          


#this loop helps selecting the token with most queries available.  
remainingRequests = []
for token in tokens:
    check_url = "https://app.zenserp.com/api/v2/status"
    check_header = { 'apikey': token }
    data = requests.get(check_url, headers=check_header).text
    left = json.loads(data)
    if 'remaining_requests' in left:
        num = left['remaining_requests']
        remainingRequests.append(num)
    if not 'remaining_requests' in left:
        num = 0
        remainingRequests.append(num)
indices = [i for i, x in enumerate(remainingRequests)]
for idx in indices:
    print("Token n. "+str(idx)+": "+str(remainingRequests[idx])+" queries left"+"\n")
    
zenTokenIdx = int(input("Specify the token you want to use (ITALIAN: 21 queries; ENGLISH,SPANISH: 15 queries needed): "))

#if you have a paid zenserp plan, you can delete from line 38 to line 59 and add another line like this:
# zenToken = "PUT YOUR TOKEN HERE" instead of the following:

zenToken = tokens[zenTokenIdx]

entityNames = []

#in this loop, we define the name of the counterparty we need to assess:

while True:
    counterparty = input("Please specify the entity name: ")
    entityNames.append(counterparty)
    alternativeNames = input("Please specify alternative names, if needed, separated by '|' and without spaces. If not needed, just press return (ex: 'Mc Donalds Pvt. Ltd.'|'McDonalds Private Limited':) ")
    alternativeNamesList = alternativeNames.split('|')
    if alternativeNamesList[0] != '':
        for alternativeName in alternativeNamesList:
            entityNames.append(alternativeName)
    if not counterparty:
        print(Fore.RED + "You need to specify an entity name!")
    else:
        break

#now, we select the language for our search. Currently only Italian, English and Spanish available
while True:
    lang = input("Please define the search language (en/it/es): ")
    if any([lang == "en", lang == "it", lang=="es"]):
        print(Fore.GREEN +"Ok! Will search in the defined language")
        break
    elif any([lang != "en", lang != "it", lang!= "es"]):
        print(Fore.RED +"Language not supported (currently)!")
        continue
    else:
        break

#let's define the confidence interval for our adverse keywords to be considered. If you do not want to skip any news, put an high number, ex: 4000
while True:
    proximity = int(input("Please define a proximity interval (1-4999)..: "))
    if proximity < 1:
        print(Fore.RED + "Please choose a number between 1 and 4999")
    elif proximity > 5000:
        print(Fore.RED + "Please choose a number between 1 and 4999")
    else:
        break
    
keywords = []

#ITALIAN KEYWORDS BLOCK
   
if lang == "it":
    keywords.append(kw_it1)
    keywords.append(kw_it2)
    keywords.append(kw_it3)
    keywords.append(kw_it4)
    keywords.append(kw_it5)
    keywords.append(kw_it6)
    keywords.append(kw_it7)

#ENGLISH KEYWORDS BLOCK
    
if lang == "en":
    keywords.append(kw_en1)
    keywords.append(kw_en2)
    keywords.append(kw_en3)
    keywords.append(kw_en4)
    keywords.append(kw_en5)

#SPANISH KEYWORDS BLOCK

if lang == "es":
    keywords.append(kw_es1)
    keywords.append(kw_es2)
    keywords.append(kw_es3)
    keywords.append(kw_es4)
    keywords.append(kw_es5)


sourcesList = []
snippets = []

#here we define some variables for the zenserp api. for details, check the api reference

base_url_ita = "google.it"
base_url_en = "google.com"
base_url_es = "google.es"
location_ita = "Metropolitan City of Rome,Lazio,Italy"
location_usa = "New York,New York,United States"
location_es = "Granada,Andalusia,Spain"

#here we tokenize the name of the entity. it is a key part of the script in order to assess how bad a news might be
entityRaw = counterparty.strip('"')
counterparty_split = entityRaw.split(' ')
counterparty_token = '_'.join(counterparty_split).upper()

if len(entityNames) == 1:
    pattern = counterparty.strip('"')
if len(entityNames) > 1:
    pattern = str(str(tuple(entityNames)).replace(", ","|")).replace("'","").replace('"','')

#now, we generate two empty csv files with the name of the counterparty within the running script directory

path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(path, counterparty_token+"_REPORT"+".csv")
sources_file = os.path.join(path, counterparty_token+"_SOURCES"+".csv")

#lets start the main function. It searches google via the zenserp api for adverse media

def search(baseurlLang, location, zenToken):
    startPoint = [0, 100, 200]
    headers = { 'apikey': zenToken }
    with open(sources_file,'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter ="|" )
        kw_disambiguate = input("Do you want to disambiguate search by a specific term? y/n ")
        if kw_disambiguate == "y":
            kwDis = input("Plese specify the term/name/place (You can use AND/OR/NOT/SITE/BEFORE/AFTER/ operators too!): ")
            for point in startPoint:
                for keyword in keywords:                   
                    newKw = counterparty+" "+kwDis
                    print("[*] Searching: "+newKw+keyword)                                                     
                    params = (
                       ("q",newKw+keyword),
                       ("device","desktop"),
                       ("location",location),
                       ("num","100"),
                       ("search_engine",baseurlLang),
                       ("start",point)
                    )                                
                    response = requests.get('https://app.zenserp.com/api/v2/search', params=params, headers=headers).text                   
                    data = json.loads(response)
                    if 'organic' in data:
                        for row in data['organic']:
                            if 'url' in row:
                                link = row['url']
                                snippet = row['description']                          
                                if link and snippet:
                                    snippets.append(snippet)
                                    sourcesList.append(link)
                    if not 'organic' in data:
                        print("[!] Results not available or token expired")                                                       
            print("\n")
            print(Fore.WHITE +"""*** SOURCES LIST SAVED IN SCRIPT'S DIRECTORY ***""")
            print("\n")
            for article in sourcesList:
                position = sourcesList.index(article)                    
                print(article)
                rows = [article]
                writer.writerow(rows)                
        if kw_disambiguate == "n":
            for point in startPoint:
                for keyword in keywords:                    
                    print("\n")
                    print("[*] Searching: "+counterparty+keyword)  
                    print("\n")                                   
                    params = (
                       ("q",counterparty+keyword),
                       ("device","desktop"),
                       ("location",location),
                       ("num","100"),
                       ("search_engine",baseurlLang),
                       ("start",point)
                    )                                   
                    response = requests.get('https://app.zenserp.com/api/v2/search', params=params, headers=headers).text                   
                    data = json.loads(response)
                    if 'organic' in data:
                        for row in data['organic']:
                            if 'url' in row:
                                link = row['url']
                                snippet = row['description']                            
                                if link and snippet:
                                    snippets.append(snippet)
                                    sourcesList.append(link)                                
                    if not 'organic' in data:
                        print("[!] Results not available or token expired")                               
            for article in sourcesList:
                position = sourcesList.index(article)                    
                print(article)
                rows = [article]
                writer.writerow(rows)
            print("\n")
            print(Fore.WHITE +"""*** SOURCES LIST SAVED IN SCRIPT'S DIRECTORY ***""")
            print("\n")                
                 
   
#this function finds out if each news/url might contain negative allegations and defines a reputation risk score for each news, based on our list of keywords
def __init__(issueLang):
    with open(file,'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter ="|" )
        header = ['URL','Issue','Distance','Snippet','N. Mentions','Total Issues', 'Risk Score']
        writer.writerow(header)
        for url in set(sourcesList):
            if not url.endswith(('pdf', 'Pdf', 'PDF', 'xml', 'XML', 'Xml', 'ppt', 'PPT', 'Ppt')):
                try:
                    check = requests.head(url, verify=False, timeout=10, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"})
                except Exception:
                    print(Fore.RED + "[!] SKIPPED: {URL}".format(URL=url))                  
                    continue
                headers_check = str(check.headers)
                if headers_check and not re.search("text/html", headers_check, flags=re.IGNORECASE):
                    print(Fore.RED + "[!] SKIPPED: {URL}".format(URL=url))                   
                    continue
                if headers_check and re.search("text/html", headers_check, flags=re.IGNORECASE):
                    try:                    
                        print(" >>> Processing: " + url)
                        article = Article(url)
                        article.download()
                        article.parse()
                        text = article.text
                    except Exception:
                        continue
                    if text:
                        sub_ = re.subn(pattern,counterparty_token,text,flags=re.IGNORECASE)
                        soup = sub_[0]
                        page_total_issues = []
                        min_distance_issues = []
                        min_distance_count = []
                        for issue in issueLang:
                            issue_split = issue.split(' ')
                            issue_token = '_'.join(issue_split).upper()
                            if re.search(issue, soup, flags=re.IGNORECASE):
                                soup2 = re.sub(issue, issue_token, soup, flags=re.IGNORECASE)
                                issue_list = []
                                issue_list.append(issue_token)
                                without_punctuation = re.sub('[^0-9a-zA-ZÞëÖÅŨÄÊÜþÒÌŒÕÑüäíáõÂÐÎæũßãÓóÇÈîËôöÝÀÁÆúýâèøẽœÿìïÍñÉẼÔÛÏẞÚÙåðûàêòùØÃ&@_.+]+', ' ', soup2)
                                single_spaced_text = re.sub('\s+', ' ', without_punctuation).strip()
                                textList = single_spaced_text.split()
                                if counterparty_token in textList:
                                    position = textList.index(counterparty_token)
                                    before = position - 50
                                    after = position + 50
                                    if before >= 0:
                                        raw = textList[before:after]
                                    if before < 0:
                                        raw = textList[position:after]
                                    snippet = (' '.join(raw))
                                    page_issue_mentions = []
                                    for issue_token in issue_list:
                                        counter = textList.count(issue_token)
                                        page_issue_mentions.append(counter)
                                        page_total_issues.append(counter)
                                    total = sum(page_issue_mentions)
                                    issue_indexes = [index for index, value in enumerate(textList) if value == issue_token]
                                    entity_indexes = [index for index, value in enumerate(textList) if value == counterparty_token]
                                    distances = [abs(item[0] - item[1]) for item in itertools.product(issue_indexes, entity_indexes)]
                                    try:
                                        if int(min(distances)) <= int(proximity):
                                            min_distance_count.append(int(min(distances)))
                                            print(Fore.GREEN+"[*] "+Fore.YELLOW+"{item} ".format(item=url)+Fore.CYAN+"> {issue}, ".format(issue=issue_token)+Fore.RED+"{distance}".format(distance=min(distances)))
                                            min_distance_issues.append(issue)
                                            rows = [url, issue_token, min(distances), snippet, total]
                                            writer.writerow(rows)          
                                    except ValueError:
                                        print(Fore.RED + "[!] PARTIAL MATCH: {URL} > {issue}".format(URL=url, issue=issue_token))
                                        rows = [url, issue_token, "CHECK MANUALLY", snippet, total]
                                        writer.writerow(rows)
                                        continue        
                        total_issues = sum(page_total_issues)
                        if len(min_distance_count) > 0:
                            risk_score = len(min_distance_issues)/(sum(min_distance_count)/len(min_distance_count))
                            rows = [url, " ", " ", " ", " ", total_issues, risk_score]
                            writer.writerow(rows)
                           
if lang == "it":
    search(base_url_ita, location_ita, zenToken)

if lang == "en":
    search(base_url_en, location_usa, zenToken)
    
if lang == "es":
    search(base_url_es, location_es, zenToken)    
                     
while True:
    print(Fore.GREEN + "       ")
    analisys = input("Do you want to analyze the collected sources? y/n: ")
    if analisys == "y" and lang == "it":
        print("\n")
        print(Fore.GREEN + """*** ANALYSIS OF {num} SOURCES ***""".format(num=len(sourcesList)))
        print("\n")
        __init__(kw_negative_it)
        break
    elif analisys == "y" and lang == "en":
        print("\n")
        print(Fore.GREEN + """*** ANALYSIS OF {num} SOURCES ***""".format(num=len(sourcesList)))
        print("\n")
        __init__(kw_negative_en)
        break
    elif analisys == "y" and lang == "es":
        print("\n")
        print(Fore.GREEN + """*** ANALYSIS OF {num} SOURCES ***""".format(num=len(sourcesList)))
        print("\n")
        __init__(kw_negative_es)
        break    
    elif analisys == "n":
        print(Fore.RED + "ANALYSIS ABORTED. SOURCES LIST SAVED")
        break
    elif analisys != "y" or analisi != "n":
        print(Fore.RED + "Please say 'y' or 'n'")
    else:
        break    

