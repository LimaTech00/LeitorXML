import os
import unittest
from xml_reader import read_xml_files

class TestXMLReader(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = 'test_xml_files'
        os.makedirs(self.test_dir, exist_ok=True)

        # Create some test XML files
        with open(os.path.join(self.test_dir, 'file1.xml'), 'w') as f:
            f.write('<root></root>')
        with open(os.path.join(self.test_dir, 'file2.xml'), 'w') as f:
            f.write('<root></root>')
        with open(os.path.join(self.test_dir, 'not_an_xml.txt'), 'w') as f:
            f.write('This is not an XML file.')

    def tearDown(self):
        # Remove the temporary directory and its contents
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_read_xml_files(self):
        expected_files = ['file1.xml', 'file2.xml']
        xml_files = read_xml_files(self.test_dir)
        self.assertCountEqual(xml_files, expected_files)

    def test_no_xml_files(self):
        os.rmdir(self.test_dir)  # Remove the test directory
        os.makedirs(self.test_dir)  # Create it again to ensure it's empty
        xml_files = read_xml_files(self.test_dir)
        self.assertEqual(xml_files, [])

if __name__ == '__main__':
    unittest.main()