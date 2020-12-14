# External packages
import unittest
# Internal packages
from challenge_3 import MyTable


class TestMyTableClass(unittest.TestCase):
    """This class tests the MyTable class."""
    def setUp(self):
        self.table_data = [
            {'id': 1, 'url': 'somwulr.com', 'date': '19-06-2020', 'rating': 9.5},
            {'id': 2, 'url': 'somwulr2.com', 'date': '15-02-2019', 'rating': 8.4},
        ]
        for data in self.table_data:
            MyTable(**data)

    def test_filtering_id_is_iqual_1(self):
        search1 = [md.id for md in MyTable.objects.filter(id__eq=1)]
        self.assertEqual(search1, [1])

    def test_with_no_exist_data(self):
        search1 = [md.id for md in MyTable.objects.filter(id__gt=5)]
        self.assertEqual(search1, [])


if __name__ == '__main__':
    unittest.main()
