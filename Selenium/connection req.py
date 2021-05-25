import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
# linkedin connection acceptor
 
links = ["https://www.linkedin.com/mynetwork/"]

#step 2 : run code , check if you are logged in (if not, then login) then enter "DONE" in console
#step 3 : the code shoud take care of the rest
 
 
 
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
 
driver.get("https://linkedin.com")
# delete this after every month
 
while "DONE" != input("ENTER 'DONE', ONCE YOU'VE LOGGED IN': "):
    pass

for link in links:
    try:
        print("ACCESSING LINK", link)
        driver.get(link)
        sleep(2)
        el = driver.find_elements_by_class_name("invitation-card__action-btn")
        for element in el:
        # driver.find_element_by_id("ember53").click()
            if element:    
                element.click()
                print("ACCEPTING CONNECTION REQUEST")
                
                print("CONNCETION REQUEST ACCEPTED !!!")
                sleep(1)
            else:
                print("NO MORE CONNECTION REQUESTS")
        
        
    except Exception as e:
        print("ERROR PROCESSING LINK \nLINK : ", link, "\nERROR",  e)
 
driver.close()