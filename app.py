from pathlib import Path

import streamlit as st

import portfolio
from content.projects import PROJECTS

st.set_page_config(
    page_title="Justin Allen | Engineering Portfolio",
    page_icon=":material/electrical_services:",
    layout="wide",
)

st.html(Path(__file__).with_name("style.css"))
st.sidebar.markdown("### Justin Allen")
st.sidebar.caption("Georgia Tech · Electrical Engineering")

pages = {
    "Portfolio": [
        st.Page(portfolio.home, title="Home", default=True),
        st.Page(portfolio.about, title="About Me", url_path="about"),
        st.Page(portfolio.experience, title="Experience & Leadership", url_path="experience"),
        st.Page(portfolio.skills, title="Skills", url_path="skills"),
        st.Page(portfolio.roadmap, title="Five-Year Roadmap", url_path="roadmap"),
        st.Page(portfolio.projects, title="Projects", url_path="projects"),
        st.Page(portfolio.resume, title="Resume", url_path="resume"),
        st.Page(portfolio.contact_page, title="Contact", url_path="contact"),
    ],
    "Project pages": [
        portfolio.project_route(slug) for slug in PROJECTS
    ],
}
st.navigation(pages).run()
st.divider()
st.caption("JUSTIN ALLEN  /  GEORGIA TECH  /  ECE 1100")
