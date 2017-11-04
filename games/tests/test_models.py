import datetime, uuid

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

from games.models import Game, GameListing
from consoles.models import Platform
from sales.models import GameSale

class GameModelTests(TestCase):
	"""Tests the Game model class methods."""

	def setUp(self):
		# create platform
		platform = Platform.objects.create(
			id=1,
			name="Nintendo 64",
			slug="n64",
		)

		# create game
		game = Game.objects.create(
			id=1,
			name="Super Mario 64",
			slug=platform.slug + '-' + slugify("Super Mario 64"),
			url="https://www.igdb.com/games/super-mario-64",
			summary="Mario is invited by Princess Peach to her castle, but" +
			" once he arrives he finds out that Bowser has kidnapped her." +
			" Mario has to overcome many challenges and collect Power Stars" +
			" hidden in the castle's paintings and walls to defeat Bowser and" +
			" rescue Peach in this seminal 3D platformer.",
			platform=platform,
			asin="B00000F1GM",
			epid="1535"
		)

	def test_string_representation(self):
		game = Game.objects.get(id=1)
		self.assertEqual(game.__str__(), "Super Mario 64")

	def test_absolute_url(self):
		game = Game.objects.get(id=1)
		self.assertEqual(game.get_absolute_url(), reverse('games-detail', kwargs={'platform_slug': game.platform.slug,'game_slug': game.slug}))

	def test_admin_url(self):
		game = Game.objects.get(id=1)
		self.assertEqual(game.get_admin_url(), reverse('games-admin:games-detail', kwargs={'game_pk': game.pk}))

	def test_get_price(self):
		game = Game.objects.get(id=1)

		# test no sales
		self.assertIsNone(game.get_price())

		# test one sale
		GameSale.objects.create(
			game=game,
			title="sale test",
			country="US",
			location="East Lansing",
			url="http://dev.ravedave.co/gameboyz",
			condition="Very Good",
			price=20.53,
			sold=datetime.datetime.now()
		)
		self.assertEqual(20.53, game.get_price())

		# test multiple sales
		GameSale.objects.create(
			game=game,
			title="sale test 2",
			country="US",
			location="East Lansing",
			url="http://dev.ravedave.co/gameboyz/1",
			condition="Very Good",
			price=24.53,
			sold=datetime.datetime.now()
		)
		self.assertEqual(22.53, game.get_price())

class GameListingModelTests(TestCase):
	"""Tests the Game Listing model class methods"""

	def setUp(self):
		# create platform
		platform = Platform.objects.create(
			id=1,
			name="Nintendo 64",
			slug="n64",
		)

		# create game
		game = Game.objects.create(
			id=1,
			name="Super Mario 64",
			slug=platform.slug + '-' + slugify("Super Mario 64"),
			url="https://www.igdb.com/games/super-mario-64",
			summary="Mario is invited by Princess Peach to her castle, but" +
			" once he arrives he finds out that Bowser has kidnapped her." +
			" Mario has to overcome many challenges and collect Power Stars" +
			" hidden in the castle's paintings and walls to defeat Bowser and" +
			" rescue Peach in this seminal 3D platformer.",
			platform=platform,
			asin="B00000F1GM",
			epid="1535"
		)

		# create game listing
		gamelisting = GameListing.objects.create(
			game=game,
			user=User.objects.create_user(username='testuser', password='12345'),
			price=20.12,
			condition="new"
		)

	def test_absolute_url(self):
		gamelisting = GameListing.objects.all().first()
		self.assertEqual(gamelisting.get_absolute_url(), reverse('gamelistings-detail', kwargs={'platform_slug': gamelisting.game.platform.slug, 'game_slug': gamelisting.game.slug, 'gamelisting_id': str(gamelisting.id)}))





