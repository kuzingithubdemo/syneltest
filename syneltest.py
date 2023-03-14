from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time



#Устанавливаем путь к драйверу
driver = webdriver.Chrome('Путь к драйверу selenium')
driver.get("https://www.livejournal.com/login.bml")

# Вводим информацию для входа
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='user']")))
username_field.send_keys("Пользователь")
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
password_field.send_keys("Пароль")
password_field.send_keys(Keys.RETURN)


# Переходим на старницу создания поста
max_retries = 10
wait_time = 1
page_loaded = EC.presence_of_element_located((By.XPATH, "//*[@id='editorWrapper']"))
for i in range(max_retries):
    try:
        driver.get("https://www.livejournal.com/update.bml")
        WebDriverWait(driver, wait_time).until(page_loaded)
        break
    except:
        print(f"Page not loaded yet, retrying in {wait_time} second(s)...")
        time.sleep(wait_time)

#Отклонить черновики

cancel_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[7]/div/div/div/div/div/button[1]/span")))
cancel_button.click()

# Находим поля и вводим содержимое
title_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/div/div/div[2]/textarea")))
title_field.send_keys("Имя Фамилия")
body_field= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='editorWrapper']/div[1]/div[2]/div/div/div[2]/div")))
body_field.send_keys("Synel task test post")

# Ищем кнопку Publish
first_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/footer/div/div/div/div[2]/button/span")))
ActionChains(driver).move_to_element(first_element).click().perform()

#Кликаем кнопку Publish
publish_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/footer/div/div/div/div/div/footer/div/button/span")))
publish_button.click()

#Ждем что пост опубликован
post_loaded = EC.visibility_of_element_located((By.XPATH, "//a[contains(@class, 'i-ljuser-profile')]"))
WebDriverWait(driver, 10).until(post_loaded)

#Закрываем сессию
driver.close()
