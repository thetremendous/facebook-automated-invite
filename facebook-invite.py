#----------------------------
#							              |
# Facebook - invite to group|
#https://github.com/thetremendous/facebook-automated-invite
# UPDATE: 18.08.2021	    	|
#----------------------------

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import string


browser = webdriver.Chrome(executable_path= r"C:\PATH_TO_CHROMEDRIVER_FOLDER\chromedriver.exe")  
browser.get(('https://www.facebook.com/groups/#NAME_OF_YOUR_GROUP_OR_ID'))

sleep(2) 


def start():
    acceptCookies = browser.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]');
    acceptCookies.click();
    sleep(4);
	#browser.implicitly_wait(3)  #this is another wait function.If you would like to run the script faster, change all sleep() to this
    username = browser.find_element_by_name('email')
    username.send_keys('YOUR_USERNAME') # <- INSERT YOUR USERNAME HERE -------------------------------------------------------------------------------------------------------------------------
    password = browser.find_element_by_name('pass')
    password.send_keys('YOUR_PASSWORD') # <- INSERT YOUR PASSWORD HERE -----------------------------------------------------------------------------------------------------------------------
    nextButton = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/form[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]')  # <--- Clicking on login button
    nextButton.click()
	#browser.quit()
    sleep(4)


	
	
#Start the programm
start()


    
#start the invite
def invite():
    for x in range(1,1000):
        invite = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]') #<--- Clicking on Invite button first 
        invite.click()
        sleep(3)
        mark_user = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/i[1]') 	#<---- Then we select the checkbox for the first user in the list 
        mark_user.click()
        sleep(1)
        send_user_invite = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]')
        send_user_invite.click()  #<---- And we send t he invite
        sleep(3)
    

#invite repeat
invite()
