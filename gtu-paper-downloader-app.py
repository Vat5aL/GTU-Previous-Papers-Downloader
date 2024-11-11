import streamlit as st
import requests
import datetime
import zipfile
import io

# Function to check if URL is valid
def check_url(url):
    try:
        response = requests.head(url)
        return response.status_code == 200  # Valid if status code is 200 OK
    except requests.ConnectionError:
        return False  # URL is invalid if there's a connection error

# Function to generate PDF URLs
def generate_urls(subject_code, course_code, current_year):
    urls = []
    for year in range(2017, current_year + 1):
        for term in ['S', 'W']:
            url = f"https://www.gtu.ac.in/uploads/{term}{year}/{course_code}/{subject_code}.pdf"
            urls.append(url)
    return urls

# Function to download PDFs and add them to ZIP
def create_zip(subject_code, course_code, valid_urls):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for url in valid_urls:
            response = requests.get(url)
            if response.status_code == 200:
                # Generate the filename for the PDF inside the ZIP
                filename = f"{url.split('/')[-3]}_{url.split('/')[-2]}_{url.split('/')[-1]}"
                zip_file.writestr(filename, response.content)
    zip_buffer.seek(0)
    return zip_buffer

# Streamlit app
def main():
    st.title('Download - Previous Year GTU Papers')

    # Input fields
    subject_code = st.text_input('Enter Subject Code')
    course_code = st.selectbox('Select Course Code', [
        "AF", "BA", "BB", "BC", "BD", "BE", "BESP", "BH", "BI", "BL", "BM", "BN", "BP", "BPSP",
        "BT", "BV", "CS", "DA", "DB", "DH", "DI", "DISP", "DM", "DP", "DS", "DV", "EP", "FD",
        "HM", "IB", "IC", "IM", "MA", "MB", "MC", "MCSP", "MD", "ME", "MH", "ML", "MN", "MP",
        "MR", "MS", "MT", "MV", "PB", "PD", "PH", "PM", "PP", "PR", "TE"
    ], index=5)
    current_year = datetime.datetime.now().year

    # Initialize all_Valid_PDF_URL to an empty list
    all_Valid_PDF_URL = []

    # Layout for 'Fetch Papers' and "DOWNLOAD ALL ZIP" buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button('Fetch Papers'):
            # Check if inputs are empty
            if not subject_code or not course_code or not current_year:
                st.error("Please fill in all the fields.")
                return

            # Show loader
            with st.spinner('Fetching PDF Links...'):
                # Generate URLs
                all_PDF_URL = generate_urls(subject_code, course_code, int(current_year))

                # Check URL validity
                all_Valid_PDF_URL = [url for url in all_PDF_URL if check_url(url)]
                # Reverse the list of valid PDF URLs
                all_Valid_PDF_URL.reverse()

            # Display valid PDF links or message
            st.subheader('Direct Links:')
            if len(all_Valid_PDF_URL) > 0:
                for valid_url in all_Valid_PDF_URL:
                    # Generate formatted name for each PDF
                    formatted_name = f"{valid_url.split('/')[-3]}_{valid_url.split('/')[-2]}_{valid_url.split('/')[-1]}"
                    st.write(f"{formatted_name} : [Download]({valid_url})")
            else:
                st.warning("No previous papers found. Make sure that subject code and course code are valid!")

    # "DOWNLOAD ALL ZIP" button
    with col2:
        if subject_code and course_code and len(all_Valid_PDF_URL) > 0:
            zip_file = create_zip(subject_code, course_code, all_Valid_PDF_URL)
            zip_filename = f"{subject_code}_{course_code}_GTU_papers.zip"
            st.download_button(
                label="DOWNLOAD ALL ZIP",
                data=zip_file,
                file_name=zip_filename,
                mime="application/zip"
            )

if __name__ == '__main__':
    main()
