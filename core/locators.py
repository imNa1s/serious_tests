from selenium.webdriver.common.by import By


class LoginLocators:
    email_id = (By.CSS_SELECTOR, '#loginform-username')
    password_id = (By.CSS_SELECTOR, '#loginform-password')
    captcha_id = (By.XPATH, '//*[@id="recaptcha-anchor"]')
    button_submit = (By.CSS_SELECTOR, '[name="login-button"]')


class StatsLocators:
    statistic_button = (By.CSS_SELECTOR, '#main-menu > li:nth-child(2)')
    main_statistic = (By.CSS_SELECTOR, '#main-menu > li:nth-child(2) > ul > li:nth-child(1) > a > span')
    sub_statistic = (By.CSS_SELECTOR, '#w18 > li:nth-child(2)')


class PartnerLocators:
    partner_button = (By.CSS_SELECTOR, '#main-menu > li:nth-child(3)')
    test_authorization = (By.CSS_SELECTOR, 'div.p-l.p-r.p-t.p-b-0.white.user-panel > ul > li:nth-child(7) > a')
    test_settings = (By.CSS_SELECTOR, '#view > div > div.p-l.p-r.p-t.p-b-0.white.user-panel > ul > li:nth-child(6)')
    test_partner = (By.CSS_SELECTOR, 'tr[data-key="2"] > td[data-col-seq="1"] > div')
    partner_settings = (By.CSS_SELECTOR, '#aside > div > div.hide-scroll > nav > ul > li:nth-child(10)')
    partner_id = (By.CSS_SELECTOR, 'div.col-md-6 > div > div > div:nth-child(1) > small > strong')
    partner_source = (By.CSS_SELECTOR, '#aside > div > div.hide-scroll > nav > ul > li:nth-child(2)')
    partner_tickets = (By.CSS_SELECTOR, '#aside > div > div.hide-scroll > nav > ul > li:nth-child(11)')
    create_source = (By.CSS_SELECTOR, 'button.btn.btn-sm.primary.pull-right')
    type_source_select = (By.CSS_SELECTOR, '#type_id')
    source_name = (By.CSS_SELECTOR, '#name')
    source_url = (By.CSS_SELECTOR, '#url')
    create_source_button = (By.CSS_SELECTOR, 'button.btn.primary.p-x-md')
    partner_alert_button = (By.CSS_SELECTOR, 'div.navbar.ng-scope > ul > li.nav-item.pos-stc-xs > a')
    partner_alert = (By.CSS_SELECTOR, 'ul > li.nav-item.pos-stc-xs > a > span')


class StreamLocators:
    partner_stream = (By.CSS_SELECTOR, '#aside > div > div.hide-scroll > nav > ul > li:nth-child(3)')
    create_stream = (By.CSS_SELECTOR, 'a.btn.btn-sm.primary.pull-right')
    stream_name = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(1) > div > input')
    stream_source = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(2) > div > select')
    traffback_url = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(3) > div > input')
    postback_url = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(4) > div > input')
    postback_check_sub = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(5) > div > label:nth-child(1)')
    postback_check_rebill = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(5) > div > label:nth-child(2)')
    postback_check_unsub = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(5) > div > label:nth-child(3)')
    postback_check_buyout = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(5) > div > label:nth-child(4)')
    redirect_type_simple = (By.CSS_SELECTOR, '[value="redirect"]')
    redirect_type_click_in = (By.CSS_SELECTOR, '[value="clickunder"]')
    redirect_type_click_new = (By.CSS_SELECTOR, '[value="clickunder_newTab"]')
    redirect_type_click_new_inactive = (By.CSS_SELECTOR, '[value="clickunder_newTabInactive"]')
    redirect_type_popup = (By.CSS_SELECTOR, '[value="popup"]')
    redirect_type_push = (By.CSS_SELECTOR, '[value="push"]')
    auto_buyout = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(7) > div > label > input')
    view_land_round = (By.CSS_SELECTOR, 'div:nth-child(8) > div > div:nth-child(1) > label')
    view_land_split = (By.CSS_SELECTOR, 'div:nth-child(8) > div > div:nth-child(2) > label')
    view_land_one_round = (By.CSS_SELECTOR, 'div:nth-child(8) > div > div:nth-child(3) > label')
    ban_ya_redirect = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(9) > div > label > input')
    redirect_limit = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(10) > div > input')
    unic_code_work = (By.CSS_SELECTOR, 'div.col-xl-10 > div:nth-child(11) > div > input')
    landing_mts = (By.CSS_SELECTOR, 'div:nth-child(1) > div.row.m-t-sm > div:nth-child(1) > div > a')
    landing_iplayer = (By.CSS_SELECTOR, 'div:nth-child(3) > label > div.p-a-xs > label > input')
    add_lending_btn = (By.CSS_SELECTOR, 'div.modal-footer.ng-scope > button.btn.primary.p-x-md')
    create_stream_btn = (By.CSS_SELECTOR, 'div.box-footer > button')


class TicketLocators:
    create_button_ticket = (By.CSS_SELECTOR, '#view > div > div > div.box-header > h3 > button')
    ticket_type_select = (By.CSS_SELECTOR, '#type_id')
    ticket_message_type = (By.CSS_SELECTOR, '#topic')
    ticket_message = (By.CSS_SELECTOR, '#message')
    btn_send_ticket = (By.CSS_SELECTOR, 'div.modal-footer > button.btn.primary.p-x-md')
    alert_adm_ticket_icon = (By.CSS_SELECTOR, '#main-menu > li:nth-child(6) > a > i > b')
    adm_send_ticket_btn = (By.CSS_SELECTOR, 'li.nav-item.dropdown.open > div > a:nth-child(4)')
    adm_type_ticket = (By.CSS_SELECTOR, '#supporttickets-type_id:nth-child(2)')
    adm_message_theme = (By.CSS_SELECTOR, '#supporttickets-topic:nth-child(2)')
    adm_message_ticket = (By.CSS_SELECTOR, '#supporttickets-message:nth-child(2)')
    adm_send_message = (By.CSS_SELECTOR, '#supportTicketsForm > div:nth-child(6) > button')
    ticket_header = (By.CSS_SELECTOR, 'div:nth-child(1) > div > div.text-sm.ng-binding > b')

class OperatorLocators:
    operator = (By.CSS_SELECTOR, '#main-menu > li:nth-child(7) > ul > li:nth-child(3)')
    operator_create = (By.CSS_SELECTOR, '#view > div > div.m-b > a:nth-child(1)')
    operator_name = (By.CSS_SELECTOR, '#operators-name:nth-child(2)')
    operator_subnet = (By.CSS_SELECTOR, '#operators-subnet:nth-child(2)')
    opeartor_denied_devices = (By.CSS_SELECTOR, '#operators-deny_devices:nth-child(2)')
    operator_country = (By.CSS_SELECTOR, '#operators-country_id:nth-child(2)')
    operator_on = (By.CSS_SELECTOR, '#operators-status:nth-child(2)')
    operator_create_button = (By.CSS_SELECTOR, '#operatorForm > div:nth-child(8) > button')
