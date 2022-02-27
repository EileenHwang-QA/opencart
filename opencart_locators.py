from faker import Faker
fake = Faker(locale='en_CA')
opencart_url = 'https://www.opencart.com/'
register_url = 'https://www.opencart.com/index.php?route=account/register'
success_message_url = 'https://www.opencart.com/index.php?route=account/register/success&member_token=d664941445d45d2579480ebbf886087b'
main_home_url = 'https://www.opencart.com/index.php?route=common/home'
log_in_url = 'https://www.opencart.com/index.php?route=account/login'
set_up_pin_url ='https://www.opencart.com/index.php?route=account/pin&member_token'
account_member_url ='https://www.opencart.com/index.php?route=account/account&member_token'
feature_url = 'https://www.opencart.com/index.php?route=cms/feature'
demo_url = 'https://www.opencart.com/index.php?route=cms/demo'
marketplace_url ='https://www.opencart.com/index.php?route=marketplace/extension'
blog_url ='https://www.opencart.com/blog'
download_url = 'https://www.opencart.com/index.php?route=cms/download'
showcase_url = 'https://www.opencart.com/index.php?route=cms/showcase'
contact_url = 'https://www.opencart.com/index.php?route=support/contact'
partner_url = 'https://www.opencart.com/index.php?route=support/partner'
forum_url = 'https://forum.opencart.com/'
documentation_url = 'http://docs.opencart.com/en-gb/introduction/'
github_url = 'https://github.com/opencart/opencart/issues'
developer_url = 'http://docs.opencart.com/en-gb/developer/module/'
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
country = fake.current_country()
email = fake.email()
pin_number = fake.pyint(1000, 9999)
