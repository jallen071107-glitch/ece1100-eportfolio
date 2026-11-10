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
    "spider-man": (
        "Spider-Man Fan Survey & Dashboard", "CS 1301 · Interactive web apps",
        "An eight-question fan survey and a dashboard for comparing responses and game data.",
        """
        I wanted to see if I could make a survey that was fun to fill out and still
        left me with data I could use. The questions range from favorite actors and
        movies to how familiar someone is with Spider-Man. Each submission goes
        into a CSV file that the dashboard reads back.

        The game data is separate from the survey responses. On the Visuals page,
        you can compare activities across game districts or look at fan answers by
        group. I put the average and median next to the charts so the numbers make
        sense without digging through the raw data.
        """,
    ),
    "ece-portfolio": (
        "Engineering Portfolio", "Streamlit",
        "The site you’re on now, built with Python and Streamlit.",
        """
        I wanted this site to be easy to update as I get further into EE. The
        page layouts are separate from the writing, so I can add a project photo
        or change a description without rebuilding the page. Each project has its
        own link, which makes it easier to share one thing I worked on.

        On the first version, the homepage got crowded with the sidebar open.
        I adjusted the layout so the text and portrait can stack when there’s
        less room. The five-year roadmap is another part I expect to revisit as
        I take more classes and get a better idea of the work I enjoy.
        """,
    ),
}

# Add (filename, caption) pairs for original photos stored in assets/discovery/.
DISCOVERY_PHOTOS = []
