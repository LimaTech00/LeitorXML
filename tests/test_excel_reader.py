import unittest
from src.excel_reader import read_excel_file

class TestExcelReader(unittest.TestCase):

    def test_read_excel_file_valid(self):
        # Assuming there's a valid Excel file for testing
        expected = ['file1.xml', 'file2.xml', 'file3.xml']
        result = read_excel_file('tests/test_file.xlsx')  # Replace with actual test file path
        self.assertEqual(result, expected)

    def test_read_excel_file_invalid(self):
        result = read_excel_file('tests/invalid_file.xlsx')  # Replace with an invalid test file path
        self.assertEqual(result, [])

    def test_read_excel_file_empty(self):
        result = read_excel_file('tests/empty_file.xlsx')  # Replace with an empty test file path
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()