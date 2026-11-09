# Justin Allen | ECE 1100 ePortfolio

A Streamlit portfolio with Georgia Tech navy and gold styling, a five-year EE
roadmap, and four project detail pages.

## Run in VS Code

Open this folder in VS Code. In the terminal, run:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Edit the content

- **About, experience, and skills** live in `content/profile.py`.
- **Roadmap years** live in `content/roadmap.py`. Keep `assets/roadmap.svg`
  in sync if the year labels or themes change.
- **Project descriptions** live in `content/projects.py`. Add genuine app
  screenshots as `assets/cs-portfolio.png`, `assets/spider-man.png`, or
  `assets/ece-portfolio.png` to display them on the matching pages.
- **Resume** displays and downloads `assets/Justin-Allen-Resume.pdf` when present.
  Use a public-facing copy with private contact details removed.
- **Contact** reads public email, LinkedIn, and GitHub values from
  `content/contact.py`.
- **Showcase** reads the original 400+ word feature from
  `content/discovery_showcase.md`. Cover the goal, your role, the circuit and
  code, tests and observations, what changed, and your reflection. Put original
  photos in `assets/discovery/` and add their filenames and captions to
  `DISCOVERY_PHOTOS` in `content/projects.py`.

The draft exceeds 1,000 words across the public pages, including the five
selectable roadmap years. Its visuals are the supplied portrait, two program
photos from the CS 1301 portfolio, and two original diagrams. If the rubric
requires five photographs or screenshots specifically, add two real project
screenshots or original photos. Review all images and first-person reflections
before sharing the site.

## Publish by November 10, 2026

Push this folder to a new GitHub repository and select `app.py` as the entry
point in Streamlit Community Cloud. The app needs no secrets or database.
After deploying, open the public URL in a signed-out browser and check the
sidebar, the gallery links, the roadmap, and the public resume and contact
details before submitting the link.
