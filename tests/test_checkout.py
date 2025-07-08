from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_first_product()
    inventory.go_to_cart()

    cart = CartPage(page)
    assert cart.get_cart_items_count() == 1
    cart.click_checkout()

    checkout = CheckoutPage(page)
    checkout.fill_checkout_info("Gautham", "Krishna", "123456")
    checkout.finish_order()

    assert "Thank you for your order!" in checkout.get_confirmation_text()
