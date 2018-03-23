import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

 
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver
 

def lookup(driver, url):

    try:
        timeout = 5
        j=0
        while(j<41):
            url=driver.current_url
            driver.get(url)
            selector = "div[class=\"_3wU53n\"]"
            links = driver.find_elements_by_css_selector(selector)
            while (len(links)==0):
                driver.find_element_by_class(selector).click()
                links = driver.find_elements_by_css_selector(selector)
            print links     
            for i in range(0,len(links)):
                links = driver.find_elements_by_css_selector(selector)
                #links = driver.find_elements_by_css_selector(selector)
                #print links.get_attribute("href")
                try:
                    links[i].click()
                except Exception:
                    pass
                time.sleep(1)
                while len(driver.window_handles)==1:
                    driver.get(url)
                    links = driver.find_elements_by_css_selector(selector)
                    links[i].click()
                    print "I'm waiting for the window"
                driver.switch_to_window(driver.window_handles[1])
                # try:
                #     element_present = EC.presence_of_element_located((By.ID, 'vmXPri col col-3-12'))
                #     WebDriverWait(driver, timeout).until(element_present)
                # except TimeoutException:
                #     print "Timed out waiting for page to load"
                time.sleep(5)
                string=""
                string=driver.page_source
                driver.close()
                string=string.encode('utf-8')
                f = open("./flipkart/smartwatches_" +str(i)+"_"+ str(j)+".html",'w')
                f.write(string)
                f.close()
                # sourcecode.append(string)
                #driver.get(url)
                driver.switch_to_window(driver.window_handles[0])
                #driver.execute_script("window.history.go(-1)")

            try:
                driver.find_element_by_xpath("//span[contains(text(), 'Next')]").click()
            except Exception:
                pass

            time.sleep(2)
            url=driver.current_url
            j=j+1
        #return sourcecode
        
    except TimeoutException:
        print("Box or Button not found in flipkart.com")
 
 
if __name__ == "__main__":
    driver = init_driver()
    url="https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page=1&q=smartwatches&viewType=list"
    driver.get(url)
    selector = "div[class=\"_3wU53n\"]"
    links=driver.find_elements_by_css_selector(selector)
    # print links
    # time.sleep(5) 
    #sourcecode=[]
    i=0
    
    lookup(driver,url)  
    # file-output.py
    #print sourcecode
    #f.close()   
    driver.quit()