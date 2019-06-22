from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)

input_first_name = browser.find_element_by_tag_name("input")
input_last_name = browser.find_element_by_name("last_name")
input_city = browser.find_element_by_class_name("city")
input_country = browser.find_element_by_id("country")
button_submit = browser.find_element_by_css_selector("button.btn")

input_first_name.send_keys("Ivan")
input_last_name.send_keys("Petrov")
input_city.send_keys("Smolensk")
input_country.send_keys("Russia")

button_submit.click()
