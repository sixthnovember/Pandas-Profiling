import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from data_loader import DataLoader

st.set_page_config(page_title="Pandas Profiling Report", layout="wide")

# Title
st.markdown("# Pandas Profiling Report")

# Sidebar for file upload
with st.sidebar.header('Upload a CSV file'):
    uploaded_file = st.sidebar.file_uploader("Please select a file", type=["csv"])
    use_example = st.sidebar.button('Use Example Dataset')

# Generate Pandas Profiling Report
if uploaded_file is not None:
    df = DataLoader.load_csv(uploaded_file)
    pr = ProfileReport(df, explorative=True)
    st_profile_report(pr)
elif use_example:
    df = DataLoader.load_data()
    pr = ProfileReport(df, explorative=True)
    st_profile_report(pr)
else:
    st.info('Please upload a CSV file or use the example dataset.')