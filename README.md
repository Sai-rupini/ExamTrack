# 🎓 **OnlineExamProject** - Online Exam Registration System

Welcome to **OnlineExamProject**, a Django-based platform that simplifies online exam management for **students**, **teachers**, and **administrators**.

---

## 📁 **Project Structure**

The project follows a well-organized structure to keep all files manageable and maintainable:

- `docs/`: Contains project-related documentation (e.g., design decisions, user guides, etc.)
- `OnlineExamProject/`: Main project directory with Django settings and app configurations.
- `OnlineExamProject/apps/`: Contains the core app for managing exams, users, and results.
- `static/`: Contains static files like CSS, JavaScript, and images.
- `templates/`: Contains HTML templates for rendering the UI.

---

## 🛠️ **Technologies Used**

- **Django**: Web framework for building the project.
- **SQLite**: Default database for the application (can be changed to PostgreSQL or MySQL).
- **HTML/CSS/JS**: Frontend technologies for the user interface.
- **Bootstrap**: Frontend framework for responsive design.

---

## 🚀 **Setup and Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/Sai-rupini/ExamTrack.git
   Navigate to the project directory:

'''bash
cd ExamTrack
2. Set Up a Virtual Environment (Optional but recommended)
A virtual environment helps manage dependencies for your project separately from your system’s Python installation.

Create a Virtual Environment
'''bash
python -m venv env
Activate the Virtual Environment
On Windows:

'''bash
env\Scripts\activate
On macOS/Linux:

'''bash
source env/bin/activate
3. Install Project Dependencies
With the virtual environment activated, install all necessary Python packages:

'''bash
pip install -r requirements.txt
4. Apply Database Migrations
Next, set up the database by applying Django migrations. This will create the necessary tables in the SQLite database.

'''bash
python manage.py migrate
5. Create a Superuser (Optional)
To access the Django admin interface, create a superuser account:

'''bash
python manage.py createsuperuser
Follow the prompts to set the username, email, and password for the superuser.

6. Run the Development Server
Start the Django development server to view the project locally:

'''bash
python manage.py runserver
7. Access the Application
Once the server is running, open your browser and go to:

http://localhost:8000

You can log in as a regular user (student, teacher, or admin) or use the superuser credentials to access the admin dashboard at:

http://localhost:8000/admin


