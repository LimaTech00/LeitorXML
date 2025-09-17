import unittest
from unittest.mock import patch
from io import StringIO
from src.comparer import compare_files

class TestComparer(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_compare_files_found(self, mock_stdout):
        xml_files = ['file1.xml', 'file2.xml', 'file3.xml']
        excel_names = ['file1.xml', 'file2.xml', 'file3.xml']
        
        compare_files(xml_files, excel_names)
        
        output = mock_stdout.getvalue().strip().split('\n')
        expected_output = [
            'file1.xml found.',
            'file2.xml found.',
            'file3.xml found.'
        ]
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_compare_files_not_found(self, mock_stdout):
        xml_files = ['file1.xml', 'file3.xml']
        excel_names = ['file1.xml', 'file2.xml', 'file3.xml']
        
        compare_files(xml_files, excel_names)
        
        output = mock_stdout.getvalue().strip().split('\n')
        expected_output = [
            'file1.xml found.',
            'file2.xml not found.',
            'file3.xml found.'
        ]
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_compare_files_empty(self, mock_stdout):
        xml_files = []
        excel_names = ['file1.xml', 'file2.xml']
        
        compare_files(xml_files, excel_names)
        
        output = mock_stdout.getvalue().strip().split('\n')
        expected_output = [
            'file1.xml not found.',
            'file2.xml not found.'
        ]
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()