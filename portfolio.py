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
                "I’m exploring circuits, embedded systems, and industrial automation.")
        st.markdown(
            "I’m an electrical engineering student at Georgia Tech. This portfolio "
            "follows what I’m building in ECE 1100 and CS 1301 and how those projects "
            "are shaping what I want to work on next."
        )
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
    heading("PEOPLE & RESPONSIBILITY", "Experience & Leadership")
    for organization, role, image, details in EXPERIENCE:
        with st.container(border=True):
            description = st.container()
            if image:
                photo, description = st.columns([1, 3], gap="medium", vertical_alignment="center")
                photo.image(str(ASSETS / image), width=170, caption=organization)
            with description:
                st.caption(organization)
                st.subheader(role)
                st.markdown(details)
    st.header("Campus and high school leadership")
    st.markdown(LEADERSHIP)


def skills():
    heading("TECHNICAL TOOLKIT", "Skills")
    for title, stage, details in SKILLS:
        with st.container(border=True):
            st.caption(stage)
            st.subheader(title)
            st.markdown(details)


def roadmap():
    heading("CAREER GOALS", "Five-Year EE Roadmap",
            "My working plan for exploring industrial automation through electrical engineering.")
    st.caption("Aspirational BS/MS path. Milestones depend on coursework, advising, and admission.")
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
        st.markdown(f"**Milestone to aim for**\n\n{milestone}")


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
    heading("SELECTED WORK", "Projects",
            "A closer look at the software I’ve built and the hardware I’m learning to work with.")
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
    st.markdown("**Justin Allen** · Electrical Engineering · Georgia Tech")
    with st.container(border=True):
        st.subheader("Resume preview")
        pdf = ASSETS / "Justin-Allen-Resume.pdf"
        if pdf.is_file():
            st.pdf(pdf, height=620)
            st.download_button("Download resume", pdf.read_bytes(), pdf.name, "application/pdf")
        else:
            st.caption("My resume will be available here.")
            st.download_button("Download resume", b"", disabled=True)


def contact_page():
    heading("GET IN TOUCH", "Contact")
    channels = [
        ("Email", f"mailto:{contact.EMAIL}" if contact.EMAIL else ""),
        ("LinkedIn", contact.LINKEDIN),
        ("GitHub", contact.GITHUB),
    ]
    for column, (name, url) in zip(st.columns(3), channels):
        with column.container(border=True):
            st.subheader(name)
            if url:
                st.link_button(f"Open {name}", url)
            else:
                st.caption("Coming soon")


def project_route(slug):
    return st.Page(partial(project_page, slug), title=PROJECTS[slug][0], url_path=slug)
