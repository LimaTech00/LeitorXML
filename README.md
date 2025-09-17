# XML Comparer

This project is designed to compare XML files in a specified directory against a list of expected XML file names derived from an Excel file. It helps ensure that all expected XML files are present in the directory.

## Project Structure

```
LEITORXML
├── src
│   ├── main.py          # Entry point of the application
│   ├── xml_reader.py    # Module for reading XML files
│   ├── excel_reader.py  # Module for reading Excel files
│   └── comparer.py      # Module for comparing file lists
├── tests
│   ├── test_xml_reader.py    # Unit tests for XML reading functionality
│   ├── test_excel_reader.py  # Unit tests for Excel reading functionality
│   └── test_comparer.py      # Unit tests for comparison functionality
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd LeitorXML
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```bash
python src/main.py <directory_path> <excel_file_path>
```

Replace `<directory_path>` with the path to the directory containing the XML files and `<excel_file_path>` with the path to the Excel file containing the expected XML file names.

## Testing

To run the tests, use the following command:

```bash
pytest tests/
```

This will execute all unit tests to ensure the functionality of the XML reading, Excel reading, and comparison modules.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.