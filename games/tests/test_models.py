from django.test import TestCase

from games.models import GameTitle, Game
from consoles.models import Platform

class GameModelTests(TestCase):
	"""Tests the Game model class methods."""

	def setUp(self):
		# create platform
		platform = Platform.objects.create(
			name="Nintendo 64",
			slug="n64",
		)

		# create game title
		gametitle = GameTitle.objects.create(
			name="Super Mario 64",
			url="https://www.igdb.com/games/super-mario-64",
			summary="Mario is invited by Princess Peach to her castle, but" +
			" once he arrives he finds out that Bowser has kidnapped her." +
			" Mario has to overcome many challenges and collect Power Stars" +
			" hidden in the castle's paintings and walls to defeat Bowser and" +
			" rescue Peach in this seminal 3D platformer."
		)

		# create game
		Game.objects.create(
			gametitle=gametitle,
			platform=platform,
			asin="B00000F1GM",
			epid="1535"
		)

	def test_string representation(self):
		game = Game.objects.filter(epid="1535")[0]
		self.assertEqual(game.__str__(), "Super Mario 64")

	def test_absolute_url(self):
		game = Game.objects.filter(epid="1535")[0]
