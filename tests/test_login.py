from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"
    page.wait_for_timeout(3000) 

