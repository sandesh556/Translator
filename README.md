**Python - 3.11.2**

# Translation Script README

## Overview

This script facilitates the translation of language files from one language to another using the Google Translate API. It generates translated versions of language files, which can be utilized in projects requiring multilingual support.

## Getting Started

1. **Clone Repository**: Clone this repository to your local machine.

2. **Install Dependencies**: Ensure you have the necessary dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

3. **File Structure**:
    - **`lang` Folder**:
        - Locate the `lang` directory containing language-specific files.
        - Modify `lang.py` to include your language data in a JSON-like format.

4. **Insert Language Data**:
    - Open `lang.py` and insert your language data using the following structure:
        ```python
        {
            "key1": "value1",
            "key2": "value2",
            ...
        }
        ```

5. **Running the Script**:
    - Execute `main.py` to trigger the translation process.

## Usage Instructions

1. **Translation Process**:
    - The script translates the content from `lang.py` into multiple languages specified within the script.
    - Translated files are saved in corresponding language folders.

2. **Folder Structure**:
    - The translated content is saved in PHP format within language-specific folders.
    - Utilize these translated PHP language files within your project.

3. **Notes**:
    - Language codes such as 'bsn' represent Croatian (hr), and 'ko' represents Korean (kr).
    - British English translations require manual adjustments.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the script, feel free to submit a pull request or raise an issue.
