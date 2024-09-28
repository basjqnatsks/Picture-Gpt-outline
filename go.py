from PIL import ImageGrab
# from time import sleep
# from chrome import chrome

# c = chrome()
# c.get('https://chatgpt.com')
# sleep(199)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from chrome import chrome
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from time import sleep
# Initialize the undetected ChromeDriver

chrome_options = uc.ChromeOptions()
# chrome_options.add_argument("--user-data-dir=C:\\Users\\Public\\temp")


driver = chrome(userdata='C:\\Users\\Public\\UserData')
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Now navigate to your target website
sleep(1)
driver.get("https://chatgpt.com/")

try:
    # Wait until the login button is present and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@data-testid='login-button']"))
    )

    login_button.click()
except:
    pass
else:
    # Wait until the email input is present and type the email
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "email-input"))
    )
    email_input.send_keys('')

    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "continue-btn"))
    )
    login_button.click()

    # Wait until the email input is present and type the email
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.send_keys('')

    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "action"))
    )
    login_button.click()


file_input = driver.find_element(By.XPATH, "//input[@type='file']")
# screenshot = ImageGrab.grab()
# screenshot.save('screenshot.png')
file_path = r'C:\Users\Fast-User\Desktop\screenshot.png'
file_input.send_keys(file_path)

sleep(3)



password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@data-placeholder='Message ChatGPT']"))
)
password_input.send_keys('give me just the answer in xpath that searches for the text')

login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@data-testid='send-button']"))
)

login_button.click()

sleep(4)
element_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='!whitespace-pre hljs language-xpath']"))
)

print(element_text.text)


# C:\Users\Public\Temp

sleep(1000)