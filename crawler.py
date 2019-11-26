# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 04:19:39 2019

@author: Trent T
"""


from bs4 import BeautifulSoup
import csv
import requests

test_url = "https://forums.whirlpool.net.au/thread/9jwq5mn3"
url = test_url

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r  = requests.get(url, headers=headers)

url_data = r.text

soup = BeautifulSoup(url_data, "lxml")

#first grab title
title = soup.title.text
print("Scraping Page: ", title)

#url = input("Enter a website to extract the URL's from: ")
with open(title + '.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['User Post', 'Quoted Comment', 'Reply'])
        
    test_url = "https://forums.whirlpool.net.au/thread/9jwq5mn3"
    url = test_url
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r  = requests.get(url, headers=headers)
    
    url_data = r.text
    
    soup = BeautifulSoup(url_data, "lxml")
    
    #first grab title
    title = soup.title.text
    print(title)
    
    #GRAB ALL REPLIES
    for reply in soup.findAll("div", {"class": "replyblock"}):
        #start with username
        user = reply.find('div', attrs={'class': 'replyuser'})
        username = user.find('div', attrs={'class': 'username'}).text.strip()
        print(username)
        reply_text = reply.find('div', attrs={'class': 'replytext'})
        
        all_questions = ''
        all_answers = ''
    
    
        questions = reply_text.find_all('span', attrs={'class': 'wcrep1'})
        answers = reply_text.find_all('p', attrs={'class': None})
        
        for question in questions:
            all_questions += question.text + " ** "
            
        for answer in answers:
            response = answer.find('span', attrs={'class': 'wcrep1'})
    
            if (response == None): 
                print(answer)
                all_answers += answer.text + " ** "   
            #all_questions += question.text + ' ** '
            
        #for text in reply_text:
        print("Q: ", all_questions, "A: ", all_answers)
        
        writer.writerow([username, all_questions, all_answers])
       # print(all_questions)
        
