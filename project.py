import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Project",
    layout="wide"
)

st.title("Data Science Job Salaries Insights")
menu = ["Home", "Python Charts", "Power BI file and dashboard"]
choice = st.sidebar.selectbox("Select chart type", menu)

if choice == "Home":
    st.subheader("Home")
    st.write("Welcome to My Project on data analysis of data science salaries")

elif choice == "Python Charts":
    st.title("You Selected Python Charts")

    st.subheader("Salary Growth Over Time")
    image1 = Image.open("line_chart_salary_vs_year.png")
    st.image(image1, caption="Salary Growth Over Time", width=600)

    st.subheader("Distribution of Experience Level")
    image2 = Image.open("histogram_experience_level.png")
    st.image(image2, caption="Distribution of Experience Level", width=600)

    st.subheader("Correlation Between Numerical Columns")
    image3 = Image.open("heatmap_for_numerical_columns.png")
    st.image(image3, caption="Correlation Between Numerical Columns", width=600)

    st.subheader("Box Plot Showing Salary vs. Remote Ratio")
    image4 = Image.open("box_plot_salary_vs_remote_ratio.png")
    st.image(image4, caption="Box Plot Showing Salary vs. Remote Ratio", width=600)

    st.subheader("Other Box Plots")
    image5 = Image.open("box_plots.png")
    st.image(image5, caption="Other Box Plots", width=600)

elif choice == "Power BI file and dashboard":
    st.title("Power BI file and dashboard")
    st.subheader("Sample Dashboard")

    # Correcting filename typo
    image6 = Image.open("data_science_BI_dashboard.png")  # Fixed filename
    st.image(image6, caption="Sample Dashboard", width=600)

    st.subheader("Download Power BI pbix File")
    with open("data_science_salaries_project.pbix", "rb") as f:
        btn = st.download_button(
            label="Download Power BI File",
            data=f,
            file_name="data_science_salaries_project.pbix",
            mime="application/octet-stream"
        )

