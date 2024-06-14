# Django Data Analysis App

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your_github_repo>
   cd myproject
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
    `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/data_analysis/upload/`.
