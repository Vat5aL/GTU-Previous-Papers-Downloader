import streamlit as st
import requests

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
    ], index=20)
    current_year = st.text_input('Enter Current Year', value=str(2024))

    if st.button('DOWNLOAD'):
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

        # Display valid PDF links or message
        st.subheader('Direct Links:')
        if len(all_Valid_PDF_URL) > 0:
            for valid_url in all_Valid_PDF_URL:
                st.write(valid_url)
        else:
            st.warning("No previous papers found. Make sure that subject code and course code are valid!")

if __name__ == '__main__':
    main()
