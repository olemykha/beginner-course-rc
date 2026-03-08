def test_login_success(page, ui_base_url):
    page.goto(f"{ui_base_url}/login")

    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    flash = page.locator("#flash")
    assert flash.is_visible()
    assert "You logged into a secure area!" in flash.inner_text()


def test_login_failure(page, ui_base_url):
    page.goto(f"{ui_base_url}/login")

    page.fill("#username", "wrong")
    page.fill("#password", "wrong")
    page.click("button[type='submit']")

    assert "Your username is invalid!" in page.locator("#flash").inner_text()
