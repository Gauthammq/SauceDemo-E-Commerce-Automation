class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_btn = page.locator("#checkout")
        self.cart_items = page.locator(".cart_item")

    def click_checkout(self):
        self.checkout_btn.click()

    def get_cart_items_count(self):
        return self.cart_items.count()
