# from time import sleep
# from django.core.urlresolvers import reverse
# from django.test import LiveServerTestCase
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.webdriver import WebDriver
# from ..models import Player
#
#
# class SeleniumTests(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         print 'SeleniumTests'
#         cls.selenium = WebDriver()
#         super(SeleniumTests, cls).setUpClass()
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super(SeleniumTests, cls).tearDownClass()
#
#     def admin_login(self):
#         # Create a superuser
#         Player.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')
#
#         # let's open the admin login page
#         self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))
#
#         # let's fill out the form with our superuser's username and password
#         self.selenium.find_element_by_name('username').send_keys('superuser')
#         password_input = self.selenium.find_element_by_name('password')
#         password_input.send_keys('mypassword')
#
#         # Submit the form
#         password_input.send_keys(Keys.RETURN)
#
#     def test_admin_login(self):
#         self.admin_login()
#
#         # sleep for half a second to let the page load
#         sleep(.5)
#
#         # We check to see if 'Site administration' is now on the page, this means we logged in successfully
#         body = self.selenium.find_element_by_tag_name('body')
#         self.assertIn('Site administration', body.text)
#
#     def test_admin_create_card(self):
#         self.admin_login()
#         sleep(.5)
#         # We can check that our Card model is registered with the admin and we can click on it
#         # Get the 2nd one, since the first is the header
#         self.selenium.find_elements_by_link_text('Cards')[1].click()
#         sleep(.5)
#         # Let's click to add a new card
#         self.selenium.find_element_by_link_text('Add card').click()
#         sleep(.5)
#         # Let's fill out the card form
#         self.selenium.find_element_by_name('rank').send_keys("ace")
#         sleep(.5)
#         suit_dropdown = self.selenium.find_element_by_name('suit')
#         sleep(.5)
#         for option in suit_dropdown.find_elements_by_tag_name('option'):
#             if option.text == "heart":
#                 option.click()
#         sleep(.5)
#         # Click save to create the new card
#         self.selenium.find_element_by_css_selector("input[value='Save']").click()
#
#         sleep(.5)
#
#         # Check to see we get the card was added success message
#         body = self.selenium.find_element_by_tag_name('body')
#         self.assertIn('The card "ace of hearts" was added successfully', body.text)
#
#     def test_login(self):
#         username = 'user'
#         password = 'pass'
#         Player.objects.create_user(username, 'user@test.com', password)
#
#         self.selenium.get("{}{}".format(self.live_server_url, reverse('home')))
#         # print self.selenium.find_elements_by_link_text('Login')
#         self.selenium.find_elements_by_link_text('Login')[0].click()
#         sleep(0.5)
#         # # let's fill out the form with our superuser's username and password
#         self.selenium.find_element_by_name('username').send_keys(username)
#         password_input = self.selenium.find_element_by_name('password')
#         password_input.send_keys(password)
#         sleep(0.5)
#         # Submit the form
#         password_input.send_keys(Keys.RETURN)
#
#         body = self.selenium.find_element_by_tag_name('body')
#         self.assertIn('Hi {},'.format(username), body.text)
#
#     def test_admin_create_user(self):
#         self.admin_login()
#         sleep(.5)
#         # We can check that our Card model is registered with the admin and we can click on it
#         # Get the 2nd one, since the first is the header
#         self.selenium.find_elements_by_link_text('Users')[0].click()
#         sleep(.5)
#         # Let's click to add a new card
#         self.selenium.find_element_by_link_text('Add user').click()
#         sleep(.5)
#         # Let's fill out the card form
#         self.selenium.find_element_by_name('password').send_keys('password')
#         self.selenium.find_element_by_name('username').send_keys('TestUser')
#         self.selenium.find_element_by_name('phone').send_keys('555-555-5555')
#         sleep(.5)
#         self.selenium.find_element_by_css_selector("input[value='Save']").click()
#         sleep(.5)
#         # Check to see we get the card was added success message
#         body = self.selenium.find_element_by_tag_name('body')
#         self.assertIn('was added successfully', body.text)
