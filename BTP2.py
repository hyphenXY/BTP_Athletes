# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

# def fetch_html_with_selenium(url):
#     """Fetch HTML content from a URL using Selenium and click buttons."""
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run Chrome in headless mode
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     driver = webdriver.Chrome(options=chrome_options)
#     try:
#         # Open the athlete's profile page
#         driver.get(url)

#         # Wait for the "Statistics" button to be clickable and click it
#         stats_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[@value='STATISTICS']"))
#         )
#         # Scroll to the "Statistics" button to ensure it's in view
#         driver.execute_script("arguments[0].scrollIntoView();", stats_button)
#         # Use JavaScript to click the "Statistics" button
#         driver.execute_script("arguments[0].click();", stats_button)

#         # Wait for the "Results" button under "Statistics" to be clickable and click it
#         results_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[@value='Results']"))
#         )
#         # Scroll to the "Results" button
#         driver.execute_script("arguments[0].scrollIntoView();", results_button)
#         # Use JavaScript to click the "Results" button
#         driver.execute_script("arguments[0].click();", results_button)

#         # Allow time for JavaScript to load the results page
#         time.sleep(5)

#         # Extract HTML content after navigating to "Results"
#         html_content = driver.page_source
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         html_content = ""

#     finally:
#         driver.quit()

#     return html_content

# def extract_data_from_html(html_content, driver, url):
#     """Extract data from the HTML content and click each dropdown."""
#     soup = BeautifulSoup(html_content, 'html.parser')


#     # Find all rows with dropdown buttons
#     datas = soup.find_all('div', {'class':'athletesStatisticsTable_athletesStatisticsTable__3Eq1T athletesStatsInfos_itemXL__2SfPY'})
#     d=[]
#     for data in datas:
#       rows=data.find_all('tr',{'role':'button'})
#       for index, row in enumerate(rows):
#           extracted_data = []
#           # Extract text or other data you want from the row
#           extracted_data.append(row.get_text(separator=' '))

#           # Locate all dropdown buttons and click each one by index
#           try:
#                # Re-fetch dropdown elements in case the DOM has changed
#               driver.get(url)
#               stats_button = WebDriverWait(driver, 10).until(
#                   EC.element_to_be_clickable((By.XPATH, "//button[@value='STATISTICS']"))
#               )
#               driver.execute_script("arguments[0].click();", stats_button)

#               results_button = WebDriverWait(driver, 10).until(
#                   EC.element_to_be_clickable((By.XPATH, "//button[@value='Results']"))
#               )
#               driver.execute_script("arguments[0].click();", results_button)

#               dropdown_buttons = WebDriverWait(driver, 10).until(
#                   EC.presence_of_all_elements_located((By.XPATH, "//tr[@role='button']"))
#               )
#               driver.execute_script("arguments[0].scrollIntoView();", dropdown_buttons[index])
#               driver.execute_script("arguments[0].click();", dropdown_buttons[index])

#               # Ensure the element is visible and click it
#               ActionChains(driver).move_to_element(dropdown_buttons[index]).click().perform()

#               # Wait for dropdown content to load after clicking
#               time.sleep(2)

#               # Extract the HTML content again to get updated content
#               html_content = driver.page_source
#               soup = BeautifulSoup(html_content, 'html.parser')

#               # Locate the newly revealed content after dropdown click
#               dropdown_content = soup.find_all('tr', {'class':'profileStatistics_trDropdown__1WwxW'})
#               # Adjust the class or method to find the content within the expanded dropdown<div class="athletesEventsDetails_athletesEventsDetailsContent__37Ko7">flex

#               for i in dropdown_content:
#                 details = i.find_all('div',{'class':'dropdown-item'})

#               for i in details:
#                 if i:
#                   extracted_data.append(i.get_text())
#                 else:
#                   print(f"No additional content found for dropdown at index {index}")

#           except Exception as e:
#               print(f"An error occurred while clicking dropdown: {e}")
#               continue

#           d.append(extracted_data)

#     return d

# def main():
#     # Array of athlete URL segments to replace
#     athlete_segments = []
#     # take the athlete segments from the csv file
#     with open('Players.csv', 'r', errors='ignore') as file:
#         # after 1st line, after 3 commas, take the 1st value
#         athlete_segments = [line.split(',')[3] for line in file.readlines()[1:]]
        
#     # print(athlete_segments)
#     # return
        

#     base_url = ""

#     all_data = ['Discipline, Mark, Date, Country, ResultScore, Competition, Category, Race, Place']

#     # Initialize the Selenium driver once
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")

#     driver = webdriver.Chrome(options=chrome_options)

#     # create a csv file to store the data
#     with open('Data.csv', 'w') as file:
#         file.write('Discipline, Mark, Date, Country, ResultScore, Competition, Category,Race,Place\n')
       
    
#     for segment in athlete_segments:
#         if segment[0]!='h':
#             continue
#         url = base_url + segment
#         print(f"Fetching data from URL: {url}")

#         # Fetch the HTML content of the page
#         html_content = fetch_html_with_selenium(url)

#         if html_content:
#             # Extract data from HTML content
#             data = extract_data_from_html(html_content, driver, url)
#             # Parse the raw text into structured format
#             #structured_data = parse_data(data)
#             all_data.extend(data)

#         else:
#             print(f"Failed to retrieve page content for URL: {url}")

#     driver.quit()

#     # Write the structured data to a CSV file
#     with open('Data.csv', 'a') as file:
#         for data in all_data:
#             file.write(f"{data}\n")

# if __name__ == "__main__":
#     main()

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
from selenium.webdriver.common.keys import Keys

def fetch_html_with_selenium(driver, url):
    """Fetch HTML content from a URL using Selenium and click buttons."""
    try:
        # Open the athlete's profile page
        driver.get(url)

        # Wait for the "Statistics" button to be clickable and click it
        stats_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@value='STATISTICS']"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", stats_button)
        driver.execute_script("arguments[0].click();", stats_button)

        # Wait for the "Results" button under "Statistics" to be clickable and click it
        results_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@value='Results']"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", results_button)
        driver.execute_script("arguments[0].click();", results_button)
        
        # press tab 3 times
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
        
        # enter 2 0 1 9
        ActionChains(driver).send_keys('2').perform()
        ActionChains(driver).send_keys('0').perform()
        ActionChains(driver).send_keys('1').perform()
        ActionChains(driver).send_keys('9').perform()
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        
        


        # Allow time for JavaScript to load the results page
        time.sleep(5)

        # Extract HTML content after navigating to "Results"
        html_content = driver.page_source
    except Exception as e:
        print(f"An error occurred: {e}")
        html_content = ""

    return html_content

def extract_data_from_html(html_content, driver):
    """Extract data from the HTML content and click each dropdown."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all rows with dropdown buttons
    datas = soup.find_all('div', {'class':'athletesStatisticsTable_athletesStatisticsTable__3Eq1T athletesStatsInfos_itemXL__2SfPY'})
    all_data = []
    for data in datas:
        rows = data.find_all('tr', {'role':'button'})
        for index, row in enumerate(rows):
            extracted_data = [row.get_text(separator=' $ ')]

            try:
                # Click the dropdown button using JavaScript
                dropdown_buttons = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//tr[@role='button']"))
                )
                driver.execute_script("arguments[0].scrollIntoView();", dropdown_buttons[index])
                driver.execute_script("arguments[0].click();", dropdown_buttons[index])

                # Wait for dropdown content to load
                time.sleep(2)

                # Extract updated HTML content and find the revealed content
                html_content = driver.page_source
                soup = BeautifulSoup(html_content, 'html.parser')

                # Locate the newly revealed content
                dropdown_content = soup.find_all('tr', {'class': 'profileStatistics_trDropdown__1WwxW'})
                for i in dropdown_content:
                    details = i.find_all('div', {'class': 'dropdown-item'})
                    for detail in details:
                        extracted_data.append(detail.get_text())
            except Exception as e:
                print(f"An error occurred while clicking dropdown: {e}")
                continue

            all_data.append(extracted_data)

    return all_data

def main():
    athlete_segments = []
    # take the athlete segments from the csv file
    with open('Players.csv', 'r', errors='ignore') as file:
        # after 1st line, after 3 commas, take the 1st value
        athlete_segments = [line.split(',')[3] for line in file.readlines()[1:]]
    # Base URL of the athlete
    # base_url = "https://worldathletics.org/athletes/ethiopia/tamirat-tola-14589459"
    
    with open('Data.csv', 'w') as file:
        file.write('Discipline, Mark, Date, Country, ResultScore, Competition, Category, Race, Place\n')

    # Initialize the Selenium driver once
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)

    # Fetch the HTML content of the page
    for segment in athlete_segments:
        if segment[0]!='h':
            continue
        html_content = fetch_html_with_selenium(driver, segment)

        if html_content:
            # Extract data from HTML content
            data = extract_data_from_html(html_content, driver)
            with open('Data.csv', 'a') as file:
                for d in data:
                    file.write(f"{d}\n")   
        else:
            print("Failed to retrieve page content.")

    driver.quit()

if __name__ == "__main__":
    main()