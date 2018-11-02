from selenium import webdriver

def test_home():
    driver = webdriver.Chrome()
    address = "http://199.116.235.228:8000"

    driver.get(address)
    element = driver.find_element_by_id("name")
    assert element != None
    element = driver.find_element_by_id("about")
    assert element != None
    element = driver.find_element_by_id("education")
    assert element != None
    element = driver.find_element_by_id("skills")
    assert element != None
    element = driver.find_element_by_id("work")
    assert element != None
    element = driver.find_element_by_id("contact")
    assert element != None  
    

test_home()