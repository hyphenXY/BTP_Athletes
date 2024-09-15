from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def fetch_html_with_selenium(url):
    """Fetch HTML content from a URL using Selenium and click buttons."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        # Open the athlete's profile page
        driver.get(url)

        # Wait for the "Statistics" button to be clickable and click it
        stats_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@value='STATISTICS']"))
        )
        # Scroll to the "Statistics" button to ensure it's in view
        driver.execute_script("arguments[0].scrollIntoView();", stats_button)
        # Use JavaScript to click the "Statistics" button
        driver.execute_script("arguments[0].click();", stats_button)

        # Wait for the "Results" button under "Statistics" to be clickable and click it
        results_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@value='Results']"))
        )
        # Scroll to the "Results" button
        driver.execute_script("arguments[0].scrollIntoView();", results_button)
        # Use JavaScript to click the "Results" button
        driver.execute_script("arguments[0].click();", results_button)

        # Allow time for JavaScript to load the results page
        time.sleep(5)

        # Extract HTML content after navigating to "Results"
        html_content = driver.page_source
    except Exception as e:
        print(f"An error occurred: {e}")
        html_content = ""

    finally:
        driver.quit()

    return html_content

def extract_data_from_html(html_content, driver, url):
    """Extract data from the HTML content and click each dropdown."""
    soup = BeautifulSoup(html_content, 'html.parser')


    # Find all rows with dropdown buttons
    datas = soup.find_all('div', {'class':'athletesStatisticsTable_athletesStatisticsTable__3Eq1T athletesStatsInfos_itemXL__2SfPY'})
    d=[]
    for data in datas:
      rows=data.find_all('tr',{'role':'button'})
      for index, row in enumerate(rows):
          extracted_data = []
          # Extract text or other data you want from the row
          extracted_data.append(row.get_text(separator=' '))

          # Locate all dropdown buttons and click each one by index
          try:
               # Re-fetch dropdown elements in case the DOM has changed
              driver.get(url)
              stats_button = WebDriverWait(driver, 10).until(
                  EC.element_to_be_clickable((By.XPATH, "//button[@value='STATISTICS']"))
              )
              driver.execute_script("arguments[0].click();", stats_button)

              results_button = WebDriverWait(driver, 10).until(
                  EC.element_to_be_clickable((By.XPATH, "//button[@value='Results']"))
              )
              driver.execute_script("arguments[0].click();", results_button)

              dropdown_buttons = WebDriverWait(driver, 10).until(
                  EC.presence_of_all_elements_located((By.XPATH, "//tr[@role='button']"))
              )
              driver.execute_script("arguments[0].scrollIntoView();", dropdown_buttons[index])
              driver.execute_script("arguments[0].click();", dropdown_buttons[index])

              # Ensure the element is visible and click it
              ActionChains(driver).move_to_element(dropdown_buttons[index]).click().perform()

              # Wait for dropdown content to load after clicking
              time.sleep(2)

              # Extract the HTML content again to get updated content
              html_content = driver.page_source
              soup = BeautifulSoup(html_content, 'html.parser')

              # Locate the newly revealed content after dropdown click
              dropdown_content = soup.find_all('tr', {'class':'profileStatistics_trDropdown__1WwxW'})
              # Adjust the class or method to find the content within the expanded dropdown<div class="athletesEventsDetails_athletesEventsDetailsContent__37Ko7">flex

              for i in dropdown_content:
                details = i.find_all('div',{'class':'dropdown-item'})

              for i in details:
                if i:
                  extracted_data.append(i.get_text())
                else:
                  print(f"No additional content found for dropdown at index {index}")

          except Exception as e:
              print(f"An error occurred while clicking dropdown: {e}")
              continue

          d.append(extracted_data)

    return d

def main():
    # Array of athlete URL segments to replace
    athlete_segments = ["ethiopia/tamirat-tola-14589459"]

    base_url = "https://worldathletics.org/athletes/"

    all_data = ['Discipline, Mark, Date, Country, ResultScore, Competition, Category, Race, Place']

    # Initialize the Selenium driver once
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    for segment in athlete_segments:
        url = base_url + segment
        print(f"Fetching data from URL: {url}")

        # Fetch the HTML content of the page
        html_content = fetch_html_with_selenium(url)

        if html_content:
            # Extract data from HTML content
            data = extract_data_from_html(html_content, driver, url)
            # Parse the raw text into structured format
            #structured_data = parse_data(data)
            all_data.extend(data)

        else:
            print(f"Failed to retrieve page content for URL: {url}")

    driver.quit()

    # Process or save all_data as needed
    for entry in all_data:
        print(entry)

if __name__ == "__main__":
    main()