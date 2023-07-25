import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
def scrape_google_maps_data(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]/div[2]/div[2]').click()
    time.sleep(2)
    total_number_of_reviews = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div[2]/div[2]').text.split(" ")[0]
    total_number_of_reviews = int(total_number_of_reviews.replace(',', '')) if ',' in total_number_of_reviews else int(total_number_of_reviews)
    rating_element = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]')
    rating = rating_element.text

    return rating, total_number_of_reviews
def main():
  st.title("Google Maps Data Scraping")
  url = st.text_input("Enter the Google Maps URL:") 
  if st.button("Scrape Data"):
    if url:
            # Validate the URL format
        if not url.startswith("https://www.google.com/maps/"):
                st.warning("Please enter a valid Google Maps URL.")
        else:
            try:
                    # Scrape the data using Selenium
                ratings,reviews = scrape_google_maps_data(url)

                st.success(f"Rating: {ratings}")
                st.success(f"Number of Reviews: {reviews}")
            except ValueError as e:
                st.error(str(e))
if __name__ == "__main__":
    main()


