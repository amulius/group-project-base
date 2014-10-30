from django.test import TestCase
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from slides.models import Person
from slides.tests.factories import PersonFactory


class ViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_lecture_page(self):
        response = self.client.get(reverse('lecture'))
        self.assertIn('<p>week_number</p>', response.content)
        self.assertEqual(response.context['lecture'], response.content)
#
#     def test_deck_page(self):
#         response = self.client.get(reverse('deck'))
#         self.assertIn('<p>Suit: spade, Rank: two</p>', response.content)
#         self.assertEqual(response.context['cards'].count(), 52)
#
#     def test_faq_page(self):
#         response = self.client.get(reverse('faq'))
#         self.assertIn('<p>Q: Can I win real money on this website?</p>', response.content)
#
#     def test_filters_page(self):
#         response = self.client.get(reverse('filters'))
#         self.assertIn('We have 52 cards!', response.content)
#         self.assertIn('Uppercased Rank: THREE', response.content)
#         self.assertEqual(response.context['cards'].count(), 52)
#
    def test_register_page(self):
        username = 'new-user'
        data = {
            'username': username,
            'email': 'test@test.com',
            'password1': 'test',
            'password2': 'test'
        }
        response = self.client.post(reverse('register'), data)

        # Check this user was created in the database
        self.assertTrue(Person.objects.filter(username=username).exists())

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('account')))

    def test_login_page(self):
        username = 'new-user'
        password = 'test'
        PersonFactory.create(username=username, password=password)
        data = {
            'username': username,
            'password': password,
        }
        response = self.client.post(reverse('login'), data)
        # print response

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('account')))


    def test_account_page(self):
        # Create user and log them in
        password = 'passsword'
        user = PersonFactory.create(username='test-user', email='test@test.com', password=password)
        self.client.login(username=user.username, password=password)
        response = self.client.get(reverse('account'))
        self.assertInHTML('<p>Your email address is {}</p>'.format(user.email), response.content)
#
#     def test_war_page(self):
#         # Create user and log them in
#         password = 'passsword'
#         user = PlayerFactory.create(username='test-user', email='test@test.com', password=password)
#         self.client.login(username=user.username, password=password)
#
#         # Make the url call and check the html and games queryset length
#         response = self.client.get(reverse('war'))
#
#         self.assertInHTML('<h2>War!</h2>', response.content)
#         self.assertEqual(len(response.context['user_cards']), 1)
#         self.assertEqual(len(response.context['dealer_cards']), 1)
#
#     @patch('cards.utils.requests')
#     def test_home_page(self, mock_requests):
#         mock_comic = {
#             'num': 1433,
#             'year': "2014",
#             'safe_title': "Lightsaber",
#             'alt': "A long time in the future, in a galaxy far, far, away.",
#             'transcript': "An unusual gamma-ray burst originating from somewhere across the universe.",
#             'img': "http://imgs.xkcd.com/comics/lightsaber.png",
#             'title': "Lightsaber",
#         }
#         mock_response = Mock()
#         mock_response.status_code = 200
#         mock_response.json.return_value = mock_comic
#         mock_requests.get.return_value = mock_response
#         response = self.client.get(reverse('home'))
#         self.assertIn('<h3>{} - {}</h3>'.format(mock_comic['safe_title'], mock_comic['year']),
#                       response.content)
#         self.assertIn('<img alt="{}" src="{}">'.format(mock_comic['alt'], mock_comic['img']),
#                       response.content)
#         self.assertIn('<p>{}</p>'.format(mock_comic['transcript']), response.content)
