from selenium.webdriver.common.by import By


class LoginLocators:
    email_id = (By.CSS_SELECTOR, '#loginform-username')
    password_id = (By.CSS_SELECTOR, '#loginform-password')
    captcha_id = (By.XPATH, '//*[@id="recaptcha-anchor"]')
    button_submit = (By.CSS_SELECTOR, '[name="login-button"]')


class StatsLocators:
    statistic_button = (By.CSS_SELECTOR, '#main-menu > li:nth-child(2)')
    main_statistic = (By.CSS_SELECTOR, '#main-menu > li.active > ul > li:nth-child(1) > a > span')
