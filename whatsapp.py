from selenium import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = "./chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.get("https://web.whatsapp.com/") 
name = "Image"
msg = """
test
"""
while True:
    try:
        user = driver.find_element_by_xpath(
            '//span[@title = "{}"]'.format(name))
        user.click()
        break
    except:
        pass

print("\n\n\n ", user, '\n\n\n')
driver.implicitly_wait(3)
msg_box = driver.find_elements_by_class_name(
    '_1awRl.copyable-text.selectable-text')[1]
for i in range(1):
    print(i)
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.RETURN)
