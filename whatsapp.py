from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
name = "name"
msg = "message"
count = 1000 #no of time to send the message
while True:
    try:
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
        break
    except:
        pass

print("\n\n\n ",user,'\n\n\n')
driver.implicitly_wait(3)
msg_box = driver.find_element_by_class_name('_3u328.copyable-text.selectable-text')
for i in range(count):
    print(i)
    msg_box.send_keys(str(i) +'. ' + msg)
    msg_box.send_keys(Keys.RETURN)
