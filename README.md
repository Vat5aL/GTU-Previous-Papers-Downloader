# Live App

Live app is hosted on [GTU Previous Papers Downloader](https://gtu-previous-papers-downloader.streamlit.app/)


# GTU Previous Year Papers Downloader

This Python script and Streamlit web app help download previous year papers from Gujarat Technological University (GTU).

## Functionality

This application allows users to input specific details to generate URLs for previous year papers based on their subject code, course code, and current year. It then validates these URLs to check for the availability of the PDF files. If valid PDF links are found, they are displayed for download.

## How to Use

### Prerequisites

- Python 3.x
- Install required libraries via `pip install -r requirements.txt`

### Running the Application

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/gtu-previous-papers-downloader.git
   ```

2. Navigate to the project directory:

   ```bash
   cd gtu-previous-papers-downloader
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run gtu-paper-downloader-app.py
   ```

4. Access the app in your browser through the provided URL.

### Usage Guide

1. Enter the **Subject Code**, **Course Code**, and **Current Year** in the respective fields.
2. Click on the **DOWNLOAD** button to generate and validate the URLs.
3. Valid PDF links for previous year papers will be displayed. If none are found, a message will indicate that no papers were located. Ensure that the subject and course codes are correct.

## Technologies Used

- Python
- Streamlit
- Requests library

## Contribution

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
