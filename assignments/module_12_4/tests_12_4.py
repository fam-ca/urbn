# copied from module_12_1
import unittest
import rt_with_exceptions as runner

class RunnerTest(unittest.TestCase):
    is_frozen = False
    # def setUp(self):
    #     print('setup')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = runner.Runner('runner 1')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = runner.Runner('runner 2')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = runner.Runner('runner 1')
        runner_2 = runner.Runner('runner 2')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

if __name__ == "__main__":
    unittest.main()