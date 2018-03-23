import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from pyvirtualdisplay import Display

 
def init_driver():
    #display = Display(visible=0, size=(800, 600))
    #display.start()
    #driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver
 

def lookup(driver, url):

    try:
        timeout = 5
        j=61
        while(j<175):
            driver.get(url)
            url=driver.current_url
            selector = "//div[@class='makers']//ul//li"
            links = driver.find_elements_by_xpath(selector)
            while(len(links)==0):
                links = driver.find_elements_by_xpath(selector)

            for i in range(0,len(links)):
                print i
                links = driver.find_elements_by_xpath(selector)
                while (len(links) == 0):
                    links = driver.find_elements_by_xpath(selector)

                #links = driver.find_elements_by_css_selector(selector)
                #print links.get_attribute("href")
                links[i].click()

                # try:
                #     element_present = EC.presence_of_element_located((By.ID, 'vmXPri col col-3-12'))
                #     WebDriverWait(driver, timeout).until(element_present)
                # except TimeoutException:
                #     print "Timed out waiting for page to load"
                time.sleep(2)
                string=""
                string=driver.page_source
                string=string.encode('utf-8')
                f = open("./gsm/output_" +str(i)+"_"+ str(j)+".html",'w')
                f.write(string)
                f.close()
                # sourcecode.append(string)
                #driver.get(url)
                #driver.switch_to_window(driver.window_handles[0])
                driver.get(url)
                time.sleep(2)

            try:
                driver.find_element_by_xpath("//div[@class='pages-next']").click()
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
    url="https://www.gsmarena.com/motorola-phones-4.php"
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