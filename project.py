import streamlit as st
import pandas as pd

# Placeholder data for schools
schools_data = pd.DataFrame({
    'School Name': ['Dubai International School', 'GEMS Modern Academy', 'American School of Dubai'],
    'Location': ['Al Barsha', 'Nad Al Sheba', 'Al Barsha'],
    'Curriculum': ['British', 'Indian', 'American'],
    'Tuition Fees': [50000, 45000, 60000],
    'KHDA Rating': ['Outstanding', 'Very Good', 'Good'],
    'Student-Teacher Ratio': [12, 15, 10],
    'Extracurricular Activities': ['Sports, Music', 'Science Clubs, Arts', 'Drama, Coding'],
    'Facilities': ['Pool, Labs, Library', 'Labs, Arts Studio', 'Auditorium, Gym']
})

# Placeholder data for universities
universities_data = pd.DataFrame({
    'University Name': ['University of Dubai', 'American University of Sharjah', 'NYU Abu Dhabi'],
    'Location': ['Dubai', 'Sharjah', 'Abu Dhabi'],
    'Admission Criteria': ['IELTS 6.5', 'SAT 1200', 'High GPA + Interview'],
    'Scholarships': ['Merit-Based', 'Need-Based', 'Merit & Need-Based'],
    'Application Deadline': ['30 May 2025', '15 June 2025', '1 July 2025'],
    'Programs Offered': ['Business, IT, Engineering', 'Arts, Sciences, Engineering', 'Global Studies, AI']
})

# Improved layout with dropdown navigation
menu_options = {
    "🏠 Home": "Home",
    "📄 Online Attestation": "Online Attestation",
    "🎓 School Search": "School Search",
    "🏫 University Search": "University Search",
    "💬 Parent-Teacher Communication": "Parent-Teacher Communication",
    "📚 Student Services": "Student Services",
    "🚌 Transportation Management": "Transportation Management",
    "💳 Payment Gateway": "Payment Gateway",
    "📅 Events & Announcements": "Events & Announcements",
    "📁 Student Records": "Student Records",
    "🤖 AI-Powered Guidance": "AI-Powered Guidance"
}

# Sidebar dropdown
selected_tab = st.sidebar.selectbox("Navigate to:", list(menu_options.keys()))

# Tab routing
if menu_options[selected_tab] == "Home":
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/45/Flag_of_Dubai.svg", use_column_width=True)
    st.title("Welcome to Dubai Schools & Universities Hub")
    st.write("""
    This app is your comprehensive platform for managing educational services and exploring schools 
    and universities in Dubai. Use the sidebar to navigate.
    """)

elif menu_options[selected_tab] == "Online Attestation":
    st.title("Online Attestation Service")
    st.write("Upload documents for attestation (e.g., birth certificates, diplomas).")
    uploaded_files = st.file_uploader("Upload files:", accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            st.success(f"Uploaded: {file.name}")
        st.info("Your documents are being processed. Expect updates within 24-48 hours.")

elif menu_options[selected_tab] == "School Search":
    st.title("School Search")
    st.write("Search for schools based on criteria or by name.")
    search_query = st.text_input("Enter school name or keyword:")
    if search_query:
        results = schools_data[schools_data.apply(
            lambda row: search_query.lower() in row.to_string().lower(), axis=1)]
        if not results.empty:
            st.write("Search Results:")
            st.table(results)
        else:
            st.warning("No matching schools found.")

elif menu_options[selected_tab] == "University Search":
    st.title("University Search")
    st.write("Find universities based on criteria or search by name.")
    search_query = st.text_input("Enter university name or keyword:")
    if search_query:
        results = universities_data[universities_data.apply(
            lambda row: search_query.lower() in row.to_string().lower(), axis=1)]
        if not results.empty:
            st.write("Search Results:")
            st.table(results)
        else:
            st.warning("No matching universities found.")

elif menu_options[selected_tab] == "Parent-Teacher Communication":
    st.title("Parent-Teacher Communication")
    message = st.text_area("Send a message to the teacher or school admin:")
    if st.button("Send Message"):
        st.success("Your message has been sent successfully!")

elif menu_options[selected_tab] == "Student Services":
    st.title("Student Services Hub")
    st.write("Access resources such as e-textbooks, grades, and exam materials.")
    st.button("Download E-Textbooks")
    st.button("View Grades")

elif menu_options[selected_tab] == "Transportation Management":
    st.title("Transportation Management")
    st.write("Track buses in real-time or manage payment and routes.")
    st.button("Track My Bus")
    st.button("Manage Routes")

elif menu_options[selected_tab] == "Payment Gateway":
    st.title("Payment Gateway")
    st.write("Pay school and university fees securely.")
    payment_amount = st.number_input("Enter payment amount:")
    if st.button("Proceed to Payment"):
        st.success(f"Payment of {payment_amount} AED processed successfully!")

elif menu_options[selected_tab] == "Events & Announcements":
    st.title("Events & Announcements")
    st.write("""
    - **Parent-Teacher Meeting:** 25 January 2025  
    - **Sports Day:** 10 February 2025  
    """)

elif menu_options[selected_tab] == "Student Records":
    st.title("Student Records")
    st.write("Download student transcripts and certificates.")
    st.button("Download Transcript")

elif menu_options[selected_tab] == "AI-Powered Guidance":
    st.title("AI-Powered Career Guidance")
    field = st.selectbox("Choose your field of interest:", ["STEM", "Arts", "Business", "Sports"])
    st.button(f"Get Guidance for {field}")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 Dubai Schools & Universities Hub")
