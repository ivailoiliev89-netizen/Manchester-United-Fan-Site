# Manchester United Fan Site

A professional-grade fan platform dedicated to Manchester United.
This project showcases the integration of a Django backend with a highly customized, modular frontend.

## Features

- Fully functional search bar in the Navbar to filter the squad in real-time.
- Integrated "Club Hub" featuring a Head Coach profile and a News system managed via Django Admin.
- Learn More page with club information using Flexbox and CSS Grid.
- Intersection observer API for custom "fade-in" scroll animations.
- Shifted from monolithic CSS to a modular file structure (`layout.css`, `home.css`, `pages.css`, etc.).
- Swiper.js integration for a smooth, responsive gallery with images of the team, stadium, and trophies
- Security settings with dotenv

## Used Techs and Skills
- Django
- HTML
- CSS (Advanced Selectors, Transitions)
- JavaScript (ES6+)
- Swiper.js
- Google Fonts
- FontAwesome

## Instructions to setup

1. Clone or downloadn the repository:
2. ```bash
3. git clone https://github.com/ivailoiliev89-netizen/Manchester-United-Fan-Site.git
4. pip install -r requirements.txt
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver

## What I Learned

- How to organize 500+ lines of code into manageable files without breaking the cascade.
- Querying the database based on user input (GET requests).
- Integrated a touch-responsive slider for the club's gallery.
- How to optimize 300 lines of code of html and css with django models,views and organize the logic into a specific functions.
- Custom-styled navigation bullets and arrows to match the Manchester United identity.
- Integrated a lightweight JavaScript Intersection Observer to trigger CSS transitions, making the site feel more "alive" and interactive.
