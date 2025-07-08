class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.add_to_cart_btns = page.locator("button.btn_inventory")

    def add_first_product(self):
        self.add_to_cart_btns.nth(0).click()

    def go_to_cart(self):
        self.cart_icon.click()
 
