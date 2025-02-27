import unittest


def multiplies_of_3_or_5(natural_numbers):
    record = []
    for number in natural_numbers:
        m_by_3_result = number * 3
        m_by_5_result = number * 5
        if m_by_3_result not in record and m_by_3_result < 1000:
            record.append(m_by_3_result)
        if m_by_5_result not in record and m_by_5_result < 1000:
            record.append(m_by_5_result)
    return sum(record)


class TestProblem1(unittest.TestCase):
    sample = [i for i in range(1, 1001)]

    def test(self):
        self.assertEqual(multiplies_of_3_or_5(
            self.sample), 233168, "Hasil salah.")


if __name__ == "__main__":
    unittest.main()
