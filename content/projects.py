PROJECTS = {
    "discovery": (
        "Arduino Discovery Project", "ECE 1100 · In progress",
        "An Arduino project exploring how a program interacts with a physical circuit.",
        """
        The Discovery Project is my opportunity to work through a hardware problem
        from the setup through testing. With Arduino, there are two places to look
        when something behaves differently than expected: what the code tells the
        board to do and how the components are connected. I want to document both so
        that someone else can follow the reasoning behind the build.

        The Showcase will explain the problem, my role, the circuit and code, and
        what changed between the first setup and the version I test. I’ll include
        original photos with captions that point out what each image shows.
        """,
    ),
    "cs-portfolio": (
        "CS 1301 Portfolio", "CS 1301 · Web Development Lab 1",
        "My first Streamlit portfolio, with sections for coursework, experience, and leadership.",
        """
        In my first web development lab, I used Streamlit to put my coursework,
        skills, projects, and leadership experience in one place. I kept the
        portfolio information in a separate Python file so that changing a course
        or role did not require rewriting the page. I used a table for coursework
        and expandable sections for details that a visitor might want to read.

        This project gave me a starting point for the ECE portfolio. Here, I’ve
        given the projects their own pages so a reader can go directly to the
        work they’re interested in.
        """,
    ),
    "spider-man": (
        "Spider-Man Quiz & Survey", "CS 1301 · Interactive web apps",
        "Coursework that uses fan prompts and a dashboard to practice input, filtering, and visualization.",
        """
        The Spider-Man fan dashboard brings together game data and an eight-question
        survey. The survey collects responses in a CSV, and the Visuals page lets
        users select a district or a fan group to see how the displayed summaries
        change. I added explanations alongside the charts so that a visitor can tell
        what the values represent and which selection they’re looking at.

        The most useful part of this work was following a value from the input
        through the saved data and into the chart. It gave me practice checking
        whether the interface and the calculation were telling the same story.
        """,
    ),
    "ece-portfolio": (
        "ECE 1100 ePortfolio", "ECE 1100 · Streamlit",
        "This site brings my engineering interests, coursework, leadership, and plans together.",
        """
        I wanted a visitor to be able to find a project quickly and still have
        enough context to understand what I worked on. The gallery gives each
        project a short introduction, and the detail pages make room for design
        decisions, screenshots, and reflections as the work develops.

        The roadmap organizes my goals into five selectable years. I can revise
        the milestones as I get more experience and learn what graduate study
        would involve. The portfolio text and assets are separate from the
        navigation, so adding a photo or updating a project is a small edit.
        """,
    ),
}

# Add (filename, caption) pairs for original photos stored in assets/discovery/.
DISCOVERY_PHOTOS = []
