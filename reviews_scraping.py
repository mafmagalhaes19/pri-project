import csv #This package lets us save data to a csv file
from selenium import webdriver #The Selenium package we'll need
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time #This package lets us pause execution for a bit
from selenium.webdriver.common.by import By

path_to_file = "reviews.csv"

pages_to_scrape = 1

url = "https://www.tripadvisor.com/Restaurant_Review-g188590-d11752080-Reviews-Martine_of_Martine_s_Table-Amsterdam_North_Holland_Province.html"

# import the webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

# open the file to save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)

# change the value inside the range to save the number of reviews we're going to grab
for i in range(0, pages_to_scrape):

    # give the DOM time to load
    time.sleep(2) 

    # Click the "expand review" link to reveal the entire review.
    buttons = driver.find_elements(By.XPATH, "//*[@class='reviewSelector']/div/div[2]/div[2]/div/p/span[2]")

    for k in range (len(buttons)):
        time.sleep(2) 
        button = buttons[k]
        time.sleep(2) 
        driver.execute_script("arguments[0].click();", button)
    
    #driver.find_element_by_xpath(".//div[contains(@data-test-target, 'expand-review')]").click()


    # Now we'll ask Selenium to look for elements in the page and save them to a variable. First lets define a  container that will hold all the reviews on the page. In a moment we'll parse these and save them:
    time.sleep(2) 
    container = driver.find_elements(By.XPATH, "//*[@class='reviewSelector']")

    
    # Next we'll grab the date of the review:
    time.sleep(2) 
    dates = driver.find_elements(By.XPATH, "//div[contains(@data-prwidget-name, 'reviews_stay_date_hsx')]")

    # Grab the titles of all fo the reviews from the current page
    time.sleep(2) 
    titles = driver.find_elements(By.XPATH, "//*[@class='noQuotes']")

    time.sleep(2) 
    
   # Now we'll look at the reviews in the container and parse them out
    for j in range(len(container)): # A loop defined by the number of reviews

        # Grab the title
        time.sleep(2) 
        title = titles[j].text

        # Grab the rating
        time.sleep(2) 
        rating = container[j].find_element(By.XPATH, ".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split(" ")[1].split("_")[1]

        #Grab the review
        time.sleep(2) 
        review = container[j].find_element(By.XPATH, ".//p[@class='partial_entry']").text.replace("\n", "  ")


        #Grab the data
        time.sleep(2) 
        date = " ".join(dates[j].text.split(" ")[-2:])

        
        #Save that data in the csv and then continue to process the next review
        time.sleep(2) 
        csvWriter.writerow([date, rating, title, review]) 
        
    # When all the reviews in the container have been processed, change the page and repeat            
    #driver.find_element_by_xpath('.//a[@class="ui_button nav next primary "]').click()

# When all pages have been processed, quit the driver
driver.quit()
