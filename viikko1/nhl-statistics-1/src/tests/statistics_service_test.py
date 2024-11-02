import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
        

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        self.assertIsNotNone(self.stats.search("Semenko"))
        self.assertIsNone(self.stats.search("Laine"))

    def test_team(self):
        self.assertIsNotNone(self.stats.team("EDM"))
        self.assertEqual(self.stats.team("Jokerit"),[])

    def test_top(self):
        self.assertIsNotNone(self.stats.top(4))
