import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        return cls.all_results

    def setUp(self):
        usein = runner_and_tournament.Runner('Усейн', 10)
        andrei = runner_and_tournament.Runner('Андрей', 9)
        nick = runner_and_tournament.Runner('Ник', 3)

    def tearDown(self):
        print(self.all_results)

    @classmethod
    def tearDownClass(cls):
        return cls.all_results

    def test_1(self):
        usein = runner_and_tournament.Runner('Усейн', 10)
        nick = runner_and_tournament.Runner('Ник', 3)
        tournament = runner_and_tournament.Tournament(90, usein, nick)
        self.all_results = tournament.start()
        max_key = max(self.all_results.keys())
        self.assertTrue(self.all_results[max_key]==nick.name)

    def test_2(self):
        andrei = runner_and_tournament.Runner('Андрей', 9)
        nick = runner_and_tournament.Runner('Ник', 3)
        tournament = runner_and_tournament.Tournament(90, andrei, nick)
        self.all_results = tournament.start()
        max_key = max(self.all_results.keys())
        self.assertTrue(self.all_results[max_key]==nick.name)

    def test_3(self):
        usein = runner_and_tournament.Runner('Усейн', 10)
        andrei = runner_and_tournament.Runner('Андрей', 9)
        nick = runner_and_tournament.Runner('Ник', 3)
        tournament = runner_and_tournament.Tournament(90, usein, andrei, nick)
        self.all_results = tournament.start()
        max_key = max(self.all_results.keys())
        self.assertTrue(self.all_results[max_key]==nick.name)

if __name__== "__main__":
    unittest.main()
