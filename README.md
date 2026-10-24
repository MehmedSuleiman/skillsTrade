# SkillsTrade

SkillsTrade is a Django website for discovering skills, schools, and courses. Browse skills by category, search listings, and view details about the skills taught by schools and courses.

## Features

- Browse and search skills by category
- Create, edit, and delete skill listings
- Browse schools and their courses
- Create, edit, and delete schools and courses
- Upload images for skill badges, school logos, and course logos

## Requirements

- Python 3.12 or newer
- PostgreSQL

Install the Python packages from `requirements.txt`.

## Run locally

1. Clone the repository and enter the project folder.
2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   On macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a PostgreSQL database and copy `.env.example` to `.env`. Set the database values, a secret key, and allowed hosts. Use `DEBUG=True` for local development.
5. Apply database migrations and start the development server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Open <http://127.0.0.1:8000/> in your browser. The admin site is at <http://127.0.0.1:8000/admin/>.

## Optional sample data

After applying migrations, you can add sample skills, schools, and courses for local development (The code for db population is AI Generated):

```bash
python manage.py populate_db
```

This command is implemented in `common/management/commands/populate_db.py`. It creates sample records only when they do not already exist, so it can be run more than once. The sample schools, contact details, and course links use placeholder `example.com` information. The command is optional and is never run automatically; the application can also be used with an empty database, and records can be created through the website.


## Project layout

- `common/` — shared models, forms, and home page
- `skills/` — skill listings
- `schools/` — schools and courses
- `templates/` — HTML templates
- `static/` — CSS and other static files
- `skillsTrade/` — Django project settings and URL configuration

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
