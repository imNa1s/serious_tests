from selenium.webdriver.common.by import By


class LoginLocators:
    email_id = (By.CSS_SELECTOR, '#loginform-username')
    password_id = (By.CSS_SELECTOR, '#loginform-password')
    captcha_id = (By.XPATH, '//*[@id="recaptcha-anchor"]')
    button_submit = (By.CSS_SELECTOR, '[name="login-button"]')


class StatsLocators:
    statistic_button = (By.CSS_SELECTOR, '#main-menu > li:nth-child(2)')
    main_statistic = (By.CSS_SELECTOR, '#main-menu > li.active > ul > li:nth-child(1) > a > span')


class PartnerLocators:
    test_authorization = (By.CSS_SELECTOR, 'div.p-l.p-r.p-t.p-b-0.white.user-panel > ul > li:nth-child(7) > a')
    test_partner = (By.CSS_SELECTOR, 'tr[data-key="2"] > td[data-col-seq="1"] > div')
    partner_button = (By.CSS_SELECTOR, '#main-menu > li:nth-child(3)')
    partner_settings = (By.CSS_SELECTOR, '#aside > div > div.hide-scroll > nav > ul > li:nth-child(10)')
    partner_id = (By.CSS_SELECTOR, 'div.col-md-6 > div > div > div:nth-child(1) > small > strong')
    partner_stream = (By.CSS_SELECTOR, '#aside > div > div.hide-scroll > nav > ul > li:nth-child(2)')
    create_stream = (By.CSS_SELECTOR, 'button.btn.btn-sm.primary.pull-right')
    type_stream_select = (By.CSS_SELECTOR, '#type_id')
    stream_name = (By.CSS_SELECTOR, '#name')
    stream_url = (By.CSS_SELECTOR, '#url')
    create_stream_button = (By.CSS_SELECTOR, 'button.btn.primary.p-x-md')

