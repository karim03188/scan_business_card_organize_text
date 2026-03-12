# Scan Business Card & Organize Text

This project automates the extraction and organization of information from business card images. It uses OCR (Optical Character Recognition) and NLP (Natural Language Processing) techniques to convert scanned business cards into structured, searchable text data.

## Features
- Extracts text from business card images using Pytesseract
- Cleans and preprocesses extracted text
- Organizes information (names, emails, phone numbers, companies, etc.)
- Supports batch processing of multiple cards
- Saves results in CSV and TXT formats
- Trains and applies custom NER (Named Entity Recognition) models

## Project Structure
- `Selected/`: Contains business card images (.jpeg)
- `data/`: Stores processed data files (pickle)
- `output/`: Contains trained models and results
- `scan_doc.py`: Main script for scanning and organizing text
- `requirements.txt`: Python dependencies
- Jupyter notebooks for OCR, preprocessing, and data preparation

## Usage
1. Place business card images in the `Selected/` folder.
2. Run the main script or use the notebooks to process images.
3. Review and export organized data from CSV/TXT files.

## Requirements
- Python 3.x
- Pytesseract
- SpaCy
- Pandas
- Other dependencies listed in `requirements.txt`

## Example Workflow
1. Scan cards and save images to `Selected/`.
2. Run OCR and extract text.
3. Preprocess and clean the text.
4. Apply NER to identify key fields.
5. Export structured data for further use.

## License
This project is for educational and personal use.

## Windows Long Path Support
If you encounter errors during package installation due to long file paths, enable Windows Long Path support:

1. Open PowerShell as Administrator.
2. Run:
	Set-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Control\\FileSystem' -Name 'LongPathsEnabled' -Value 1
3. Restart your computer.

This allows Python and pip to handle long file paths required by some packages.