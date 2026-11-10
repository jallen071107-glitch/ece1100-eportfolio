from functools import partial
from html import escape
from pathlib import Path

import streamlit as st

from content import contact
from content.profile import ABOUT, EXPERIENCE, LEADERSHIP, SKILLS
from content.projects import DISCOVERY_PHOTOS, PROJECTS
from content.roadmap import YEARS

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"


def heading(label, title, summary=None):
    st.markdown(f'<div class="eyebrow">{escape(label)}</div>', unsafe_allow_html=True)
    st.title(title)
    if summary:
        st.markdown(summary)


def home():
    introduction, portrait = st.columns([3, 2], gap="large", vertical_alignment="center")
    with introduction:
        heading("GEORGIA TECH  /  ELECTRICAL ENGINEERING", "Hi, I’m Justin.",
                "I’m in my first year at Tech. Here’s what I’m working on and where I’d like to go next.")
        st.page_link(st.Page(projects, url_path="projects"), label="Explore my projects", icon=":material/arrow_forward:")
        st.page_link(st.Page(roadmap, url_path="roadmap"), label="See my five-year roadmap", icon=":material/route:")
    with portrait:
        st.image(str(ASSETS / "portrait.png"), caption="Justin Allen · Georgia Tech")
    st.divider()
    st.header("Featured work")
    project_cards(("discovery", "spider-man"))


def about():
    heading("BACKGROUND", "About Me")
    st.markdown(ABOUT)


def experience():
    st.title("Experience & Leadership")
    for organization, role, image, details in EXPERIENCE:
        with st.container(border=True):
            description = st.container()
            if image:
                photo, description = st.columns([1, 3], gap="medium", vertical_alignment="center")
                photo.image(str(ASSETS / image), width=170)
            with description:
                st.caption(organization)
                st.subheader(role)
                st.markdown(details)
    st.header("Campus and high school leadership")
    st.markdown(LEADERSHIP)


def skills():
    st.title("Skills")
    for start in range(0, len(SKILLS), 2):
        for column, (title, details) in zip(st.columns(2), SKILLS[start:start + 2]):
            with column.container(border=True):
                st.subheader(title)
                st.markdown(details)


def roadmap():
    st.title("Five-Year EE Roadmap")
    st.markdown("Here’s what I’m doing now and what I’d like to try over the next few years.")
    st.image(str(ASSETS / "roadmap.svg"), caption="Five academic years at a glance")
    selection = st.select_slider(
        "Explore an academic year", options=[item[0] for item in YEARS], key="roadmap_year"
    )
    index = next(i for i, year in enumerate(YEARS) if year[0] == selection)
    _, title, details, milestone = YEARS[index]
    st.progress((index + 1) / len(YEARS), text=f"Year {index + 1} of {len(YEARS)}")
    with st.container(border=True):
        st.caption(selection)
        st.subheader(title)
        st.markdown(details)
        st.markdown(milestone)


def project_cards(slugs):
    for start in range(0, len(slugs), 2):
        for column, slug in zip(st.columns(2), slugs[start:start + 2]):
            title, status, summary, _ = PROJECTS[slug]
            with column.container(border=True):
                st.caption(status)
                st.subheader(title)
                st.markdown(summary)
                st.page_link(project_route(slug), label=f"View {title}", icon=":material/arrow_forward:")


def projects():
    st.title("Projects")
    project_cards(tuple(PROJECTS))


def project_page(slug):
    st.page_link(st.Page(projects, url_path="projects"), label="All projects", icon=":material/arrow_back:")
    title, status, summary, details = PROJECTS[slug]
    heading(status, title, summary)
    st.markdown(details)
    screenshot = ASSETS / f"{slug}.png"
    if screenshot.is_file():
        st.image(str(screenshot), caption=f"Screenshot of {title}")
    if slug == "spider-man":
        st.link_button("Open the Spider-Man dashboard",
                       "https://lab2webdevallen-j5byeyazwx6ctmblgbcwut.streamlit.app/")
        st.image(str(ASSETS / "survey-flow.svg"), caption="How survey responses reach the Visuals page")
    if slug == "discovery":
        st.header("Showcase")
        article = (ROOT / "content" / "discovery_showcase.md").read_text(encoding="utf-8")
        if article.strip():
            st.markdown(article)
            for filename, caption in DISCOVERY_PHOTOS:
                st.image(str(ASSETS / "discovery" / filename), caption=caption)
        else:
            with st.container(border=True):
                st.subheader("Project write-up and original photos")
                st.markdown("The build is in progress. I’ll share my setup, testing, and observations here for the Showcase.")


def resume():
    heading("PROFESSIONAL BACKGROUND", "Resume")
    with st.container(border=True):
        pdf = ASSETS / "Justin-Allen-Resume.pdf"
        if pdf.is_file():
            data = pdf.read_bytes()
            st.download_button("Download resume (PDF)", data, pdf.name, "application/pdf")
            st.pdf(data, height=650, alt="Justin Allen’s resume")
        else:
            st.caption("My resume will be available here.")
            st.download_button("Download resume", b"", disabled=True)


def contact_page():
    st.title("Contact")
    st.markdown(f"[{contact.EMAIL}](mailto:{contact.EMAIL})")
    st.link_button("Connect on LinkedIn", contact.LINKEDIN)


def project_route(slug):
    return st.Page(partial(project_page, slug), title=PROJECTS[slug][0],
                   url_path=slug, visibility="hidden")
