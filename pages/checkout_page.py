class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_btn = page.locator("#continue")
        self.finish_btn = page.locator("#finish")
        self.confirm_msg = page.locator(".complete-header")

    def fill_checkout_info(self, fname, lname, zip_code):
        self.first_name_input.fill(fname)
        self.last_name_input.fill(lname)
        self.postal_code_input.fill(zip_code)
        self.continue_btn.click()

    def finish_order(self):
        self.finish_btn.click()

    def get_confirmation_text(self):
        return self.confirm_msg.text_content()
