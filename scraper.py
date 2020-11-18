from urllib.request import urlopen
from bs4 import BeautifulSoup
from plyer import notification

import os
import time

#global counter
#counter = 0 #our incremental for a new job
totalJob = [] #declaring an empty job List array

#here we are creating a job class to hold each object
class jobClass:
	def __init__(self, title, description, location, date):
		self.title = title
		self.description = description
		self.location = location
		self.date = date

def scrapGumtree():
	currentCounter = 0
	url_to_scrape = "https://www.gumtree.co.za/s-admin-jobs/kwazulu+natal/v1c9254l3100002p1"
	request_page = urlopen(url_to_scrape)
	page_html = request_page.read()
	request_page.close()

	html_soup = BeautifulSoup(page_html, 'html.parser')

	cactus_items = html_soup.find_all('div', class_="related-ad-content")
	#here we are running a loop and printing out all the information
	for cactus in cactus_items:

		title = cactus.find('div', class_="title").text
		description = cactus.find('div', class_="description-content").text
		location = cactus.find('div', class_="location-date").text
		date = cactus.find('span', class_="creation-date").text
		#word to look for 
		timescope1 = 'mins ago'
		timescope2 = 'an hr ago'
		timescope3 = 'hrs ago'
		
		if timescope1 in date or timescope2 in date or timescope3 in date: 
			currentCounter += 1
			print(str(len(totalJob)) +" total Job")
			print(str(currentCounter) +" current Job Counter")
			if(len(totalJob) < currentCounter):
				totalJob.append(jobClass(title, description, location, date)) #here we are adding the new job to the list
				#os.system('notify-send "'+((totalJob[currentCounter -1].title).encode('ascii', 'ignore'))+'" "'+((totalJob[currentCounter -1].description).encode('ascii', 'ignore'))+'"')
				notification.notify(
                                        title = ((totalJob[currentCounter -1].title).encode('ascii', 'ignore')).decode('utf-8'),
                                        message = ((totalJob[currentCounter -1].description).encode('ascii', 'ignore')).decode('utf-8'),
                                        app_name = 'Gumtree Admin Notification',
                                        app_icon = 'gumtree_logo_icon_145211.ico'
                                 )
                                        
				print(title)
				print(description)
				print(location)
				print(date)
				print("============================================================\n")
			#here we want to show a notification
			#os.system('notify-send "'+title+'" "'+description+'"')
			#print(cactus.find('div', class_="sc_price_block_title"))
			#print cactus
	
	#if currentCounter > len(totalJob):
		

	time.sleep(180) #wait for 3 min and scrap gumtree again for new job

while True:
	scrapGumtree()



#import re

#my_str = "Hi my name is John and email address is john.doe@somecompany.co.uk and my friend's email is jane_doe124@gmail.com"
#emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str)

#for mail in an email:
#print(mail)
