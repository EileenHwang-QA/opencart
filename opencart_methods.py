import datetime
import opencart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
s = Service(executable_path='./chromedriver.exe')

driver = webdriver.Chrome(service=s)

# Fixture method - to open web browser


def setUp():
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser respond in general
    driver.implicitly_wait(10)

    # navigating to Moodle app website
    driver.get(locators.opencart_url)

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.opencart_url and driver.title == 'OpenCart - Open Source Shopping Cart Solution':
        print(f'we are at opencart homepage --{driver.current_url}')
        print(f'we\'re seeing title message -- {driver.title}')
        sleep(0.5)

    else:
        print(f'we\'re not at the opencart homepage, Check your code!')
        driver.close()
        driver.quit()
        sleep(0.25)


def register_new_user():
    driver.find_element(By.LINK_TEXT, 'REGISTER').click()
    if driver.current_url == locators.register_url:
        assert driver.current_url == locators.register_url
        assert driver.find_element(By.XPATH, '//h3[contains(.,"Register for OpenCart account")]').is_displayed()

        # Enter fake data into username open field
        driver.find_element(By.CSS_SELECTOR, "input#input-username").send_keys(locators.new_username)
        sleep(0.25)
        # Enter fake data into firstname open field
        driver.find_element(By.CSS_SELECTOR, "input#input-firstname").send_keys(locators.first_name)
        sleep(0.25)
        # Enter fake data into lastname open field
        driver.find_element(By.CSS_SELECTOR, "input#input-lastname").send_keys(locators.last_name)
        sleep(0.25)
        # Enter fake data into email open field
        driver.find_element(By.CSS_SELECTOR, "input#input-email").send_keys(locators.email)
        sleep(0.25)
        # Select country open field
        Select(driver.find_element(By.ID, 'input-country')).select_by_visible_text('Canada')
        sleep(0.25)
        # Enter fake data into password open field
        driver.find_element(By.CSS_SELECTOR, "input#input-password").send_keys(locators.new_password)
        sleep(10)

        driver.find_element(By.XPATH, '//button[contains(.,"Register")]').click()
        if driver.current_url == locators.success_message_url:
            assert driver.find_element(By.XPATH, '//h2[contains(.,"Welcome to OpenCart, your account has been created")]').is_displayed()
        print(f'Test ----- create new user: "{locators.new_username}", password: "{locators.new_password}", \n'
              f'email: "{locators.email}".----- passed .')
        sleep(0.25)


def log_out():
    driver.find_element(By.LINK_TEXT, 'LOGOUT').click()
    print(f'Test ----logout ----passed.')
    sleep(0.25)


def log_in():
    if driver.current_url == locators.main_home_url:
        driver.find_element(By.LINK_TEXT, 'LOGIN').click()
        sleep(0.25)
        if driver.current_url == locators.log_in_url:
            driver.find_element(By.XPATH, '//h1[text()="Log in to your OpenCart account"]').is_displayed()
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, "input#input-email").send_keys(locators.email)
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, "input#input-password").send_keys(locators.new_password)
            sleep(0.25)
            driver.find_element(By.XPATH, '//button[contains(.,"Login")]').click()
            print(f'Test-----log_in with email:"{locators.email}", password: "{locators.new_password}".-------passed')


def set_up_pin():
    if driver.current_url == locators.set_up_pin_url:
        driver.find_element(By.XPATH, '//h3[text()="Setup PIN for your account"]').is_displayed()
        sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#input-pin").click()
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#input-pin").send_keys(locators.pin_number)
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"Submit")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//p[contains(.,"Welcome to OpenCart!")]').is_displayed()
    sleep(0.25)
    print(f'Test -----  pin created.---------passed')


def open_links():
    # click feature link
    driver.find_element(By.LINK_TEXT, 'Features').click()
    sleep(0.25)
    if driver.current_url == locators.feature_url:
        assert driver.current_url == locators.feature_url
        print(f'Test----navigate to feature link, title is "{driver.title}"------passed.')
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, "Unlimited everything").click()
        sleep(0.25)

    # click Demo link
    driver.find_element(By.LINK_TEXT, 'Demo').click()
    if driver.current_url == locators.demo_url:
        assert driver.current_url == locators.demo_url
        print(f'Test----navigate to demo link, title is "{driver.title}"------passed.')
        sleep(0.25)

    # click Marketplace link
    driver.find_element(By.LINK_TEXT, 'Marketplace').click()
    if driver.current_url == locators.marketplace_url:
        assert driver.current_url == locators.marketplace_url
        print(f'Test----navigate to Marketplace link, title is "{driver.title}"------passed.')
        sleep(0.25)

    # click BLOG link
    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    if driver.current_url == locators.blog_url:
        assert driver.current_url == locators.blog_url
        print(f'Test----navigate to Blog link, title is "{driver.title}"------passed.')
        sleep(0.25)

    # click  Download link
    driver.find_element(By.LINK_TEXT, 'Download').click()
    if driver.current_url == locators.download_url:
        assert driver.current_url == locators.download_url
        print(f'Test----navigate to Download link, title is "{driver.title}"------passed.')
        sleep(0.25)

    # click Resources link ,Select dropdown menu
    driver.find_element(By.LINK_TEXT, 'RESOURCES').click()
    sleep(0.25)

    # click Showcase link
    driver.find_element(By.LINK_TEXT, 'SHOWCASE').click()
    if driver.current_url == locators.showcase_url:
        assert driver.current_url == locators.showcase_url
    print(f'Test----navigate to showcase, title is {driver.title}')
    sleep(0.25)

    # click CONTACT US link
    driver.find_element(By.LINK_TEXT, 'RESOURCES').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    sleep(0.25)
    if driver.current_url == locators.contact_url:
        assert driver.current_url == locators.contact_url
    print(f'Test----navigate to CONTACT US, title is {driver.title}')
    sleep(0.25)

    # click OpenCart Partners link
    driver.find_element(By.LINK_TEXT, 'RESOURCES').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'OpenCart Partners').click()
    sleep(0.25)
    if driver.current_url == locators.partner_url:
        assert driver.current_url == locators.partner_url
    print(f'Test----navigate to OpenCart Partners, title is {driver.title}')
    sleep(0.25)

    # click Community Forums link
    driver.find_element(By.LINK_TEXT, 'RESOURCES').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'COMMUNITY FORUMS').click()
    sleep(0.25)
    if driver.current_url == locators.forum_url:
        assert driver.current_url == locators.forum_url
    print(f'Test----navigate to Community Forums, title is {driver.title}')
    sleep(0.25)

    # click OpenCart Documentation link
    driver.find_element(By.LINK_TEXT, 'RESOURCES').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'OPENCART DOCUMENTATION').click()
    sleep(0.25)
    if driver.current_url == locators.documentation_url:
        assert driver.current_url == locators.documentation_url
    print(f'Test----navigate to OpenCart Documentation, title is {driver.title}')
    sleep(0.25)

    # click OpenCart Books link
    driver.find_element(By.LINK_TEXT, 'RESOURCES').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'OpenCart Books').click()
    sleep(0.25)
    if driver.current_url == locators.documentation_url:
        assert driver.current_url == locators.documentation_url
    print(f'Test----navigate to OpenCart Books, title is {driver.title}')
    sleep(0.25)

    # click Developer link
    driver.find_element(By.LINK_TEXT, 'RESOURCES').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Developer').click()
    sleep(0.25)
    if driver.current_url == locators.developer_url:
        assert driver.current_url == locators.developer_url
    print(f'Test----navigate to Developer, title is {driver.title}')
    sleep(0.25)

    # click GitHub Bug Tracker link
    driver.find_element(By.LINK_TEXT, 'RESOURCES').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'GitHub Bug Tracker').click()
    sleep(0.25)
    if driver.current_url == locators.github_url:
        assert driver.current_url == locators.github_url
    print(f'Test----navigate to GitHub Bug Tracker, title is {driver.title}')
    sleep(0.25)
    print(' ------ All test completed!!-----------------------')


def tearDown():
    if driver is not None:
        print(f'------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


setUp()
register_new_user()
log_out()
log_in()
set_up_pin()
open_links()
tearDown()
