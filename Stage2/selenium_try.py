import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 
 
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
 

def lookup(driver, url):
    
    try:
        
        j=0
        while(j<4):
            # driver.get(url)
            url=driver.current_url
            selector = "div[class=\"_3wU53n\"]"
            links = driver.find_elements_by_css_selector(selector)    
            print links     
            for i in range(0,5):
                tempdriver = init_driver()
                #links = driver.find_elements_by_css_selector(selector)
                #print links.get_attribute("href")
                links[i].click()
                url1=driver.current_url
                tempdriver.get(url1)
                time.sleep(1)
                string=""
                string=tempdriver.page_source
                string=string.encode('utf-8')
                f = open("output_%i.txt" %i,'w')
                f.write(string)
                f.close()
                # sourcecode.append(string)
                #driver.get(url)
                driver.execute_script("window.history.go(-1)")
                tempdriver.quit()
                
            driver.find_element_by_xpath("//span[contains(text(), 'Next')]").click()
            time.sleep(2)
            url=driver.current_url
            j=j+1
        #return sourcecode
        
    except TimeoutException:
        print("Box or Button not found in flipkart.com")
 
 
if __name__ == "__main__":
    driver = init_driver()
    url="https://www.flipkart.com/search?q=cellphone&otracker=start&as-show=on&as=off"
    driver.get(url)
    # selector = "div[class=\"_3wU53n\"]"
    # links=driver.find_elements_by_css_selector(selector)
    # print links
    # time.sleep(5) 
    #sourcecode=[]
    i=0
    
    lookup(driver,url)  
    # file-output.py
    #print sourcecode
    #f.close()   
    driver.quit()