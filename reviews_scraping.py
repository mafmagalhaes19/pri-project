import csv #This package lets us save data to a csv file
from selenium import webdriver #The Selenium package we'll need
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time #This package lets us pause execution for a bit
from selenium.webdriver.common.by import By

path_to_file = "reviews.csv"

def get_restaurant_reviews(restaurant_id, restaurant_url):
    # import the webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(restaurant_url)

    # open the file to save the review
    csvFile = open(path_to_file, 'a', encoding="utf-8")
    csvWriter = csv.writer(csvFile)

    # give the DOM time to load
    time.sleep(2) 

    # Click the "expand review" link to reveal the entire review.
    buttons = driver.find_elements(By.XPATH, "//*[@class='reviewSelector']/div/div[2]/div[2]/div/p/span[2]")

    for k in range (len(buttons)):
        try:
                time.sleep(2) 
                button = buttons[k]
                driver.execute_script("arguments[0].click();", button)
        except:
                pass

    # Now we'll ask Selenium to look for elements in the page and save them to a variable. First lets define a  container that will hold all the reviews on the page. In a moment we'll parse these and save them:
    container = driver.find_elements(By.XPATH, "//*[@class='reviewSelector']")
    
    # Next we'll grab the date of the review:
    dates = driver.find_elements(By.XPATH, "//div[contains(@data-prwidget-name, 'reviews_stay_date_hsx')]")

    # Grab the titles of all fo the reviews from the current page
    titles = driver.find_elements(By.XPATH, "//*[@class='noQuotes']")

    time.sleep(2) 
    
    # Now we'll look at the reviews in the container and parse them out
    for j in range(len(container)): # A loop defined by the number of reviews

        # Grab the title
        title = titles[j].text

        # Grab the rating
        rating = container[j].find_element(By.XPATH, ".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split(" ")[1].split("_")[1]

        #Grab the review
        review = container[j].find_element(By.XPATH, ".//p[@class='partial_entry']").text.replace("\n", "  ")

        #Grab the data
        date = " ".join(dates[j].text.split(" ")[-2:])
        
        #Save that data in the csv and then continue to process the next review
        csvWriter.writerow([restaurant_id, date, rating, title, review]) 

    # When all pages have been processed, quit the driver
    driver.quit()
