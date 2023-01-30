link =  "http://selenium1py.pythonanywhere.com/"

def goust_should_be_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")