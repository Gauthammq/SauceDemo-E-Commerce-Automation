from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_adding_a_product_to_cart(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_first_product()
    inventory.go_to_cart()
    
    assert "cart" in page.url
