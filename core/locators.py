from selenium.webdriver.common.by import By


class LoginLocators:
    email_id = (By.CSS_SELECTOR, '#loginform-username')
    password_id = (By.CSS_SELECTOR, '#loginform-password')
    captcha_id = (By.XPATH, '//*[@id="recaptcha-anchor"]')
    button_submit = (By.CSS_SELECTOR, '#w0 > button')
