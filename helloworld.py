from selenium import webdriver  

  
driver = webdriver.Firefox()  
driver.get('http://www.python.org')  
assert 'python' in driver.title  
elem = driver.find_element_by_name('q')  
elem.send_keys('pycon')

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
