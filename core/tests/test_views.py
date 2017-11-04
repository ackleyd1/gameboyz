from django.test import TestCase
from django.utils.text import slugify

from games.models import Game
from consoles.models import Platform

class HomeViewTest(TestCase):

	def setUp(self):
		# create platform
		self.platform = Platform.objects.create(
			id=1,
			name="Nintendo 64",
			slug="n64",
		)

		# create game
		self.game = Game.objects.create(
			id=1,
			name="Super Mario 64",
			slug=self.platform.slug + '-' + slugify("Super Mario 64"),
			url="https://www.igdb.com/games/super-mario-64",
			summary="Mario is invited by Princess Peach to her castle, but" +
			" once he arrives he finds out that Bowser has kidnapped her." +
			" Mario has to overcome many challenges and collect Power Stars" +
			" hidden in the castle's paintings and walls to defeat Bowser and" +
			" rescue Peach in this seminal 3D platformer.",
			platform=self.platform,
			asin="B00000F1GM",
			epid="1535"
		)

	def test_template(self):
		resp = self.client.get('/')
		self.assertTemplateUsed(resp, 'core/base.html')
		self.assertTemplateUsed(resp, 'core/navbar.html')
		self.assertTemplateUsed(resp, 'core/footer.html')
		self.assertTemplateUsed(resp, 'core/home.html')

	def test_no_query(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_query_no_response(self):
		response = self.client.get('/?q=pokemon')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No games found")

	def test_query_with_response(self):
		response = self.client.get('/?q=mario')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.game)
