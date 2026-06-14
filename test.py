import unittest

from main import calculate_actual_pay


class TestPayroll(unittest.TestCase):

    def test_active_player_salary(self):

        player = {
            "salary": 5000.0,
            "status": "Active"
        }

        self.assertEqual(
            calculate_actual_pay(player),
            5000.0
        )

    def test_benched_player_salary(self):

        player = {
            "salary": 6000.0,
            "status": "Benched"
        }

        self.assertEqual(
            calculate_actual_pay(player),
            3000.0
        )


if __name__ == "__main__":
    unittest.main()
