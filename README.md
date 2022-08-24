# Letters to Cities
A Django web app which lets you post letters to the German cities you love. The
idea came from an exhibition visit which had a visitors' book, which made for an
amusing read.

## Tech
- Django for the backend, bootstrap for the frontend UI
- pipenv as the development tool
- HTML, CSS & Python as the principal programming / markup languages

## Directory structure & project architecture
- `letters2cities` contains the main source tree, with subfolders `cities` containing the main app for the city webpages.
- The project's `manage.py` specifies the main settings, and templates, views, models are available in `cities`.
- This project is architected as a standard Django web app.

## Future extensions with minimal effort
- Make it possible to "follow" city pages, with notifications (RSS/email) for new letter posts.

## Build & run
```bash
git clone https://github.com/busywhistling/letters_to_cities
cd letters_to_cities/letters2cities

# populate the database and provide secret

python manage.py runserver 8000 # to run the dev server
```