import unittest
import test_tourmament
import test_runner
test_suite = unittest.TestSuite()

test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_tourmament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)