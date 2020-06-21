from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	book = WebDriverWait(browser, 15).until(
		EC.text_to_be_present_in_element((By.ID,"price"),"$100")
		)
	button = browser.find_element(By.ID, "book")
	button.click()

	x_x = browser.find_element_by_id("input_value")
	x = x_x.text
	y = calc(x)

	inp = browser.find_element_by_id("answer")
	inp.send_keys(y)

	button1 = browser.find_element(By.ID, "solve")
	button1.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

