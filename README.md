# Django CRUD with Datatables

This repository demonstrates a **Django CRUD** (Create, Read, Update, Delete) application with **DataTables** integration. The project leverages Django models, forms, templates, and static files to provide an interactive interface for managing student and sales data.

---

## Features
- **CRUD Operations**: Add, edit, delete, and view records for students and sales data.
- **DataTables Integration**: Enhanced user experience with table sorting, filtering, and pagination.
- **Custom Validation**: Password validation logic for student records.
- **Modular App Structure**: Organized into `crudop`, `enroll`, and `sales` apps.
- **Reusable Templates**: Base templates with Jinja templating for dynamic rendering.

---

## Project Structure
```
├── yash211-django-crud-datatables/
    ├── README.md
    ├── db.sqlite3
    ├── manage.py
    ├── crudop/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── __pycache__/
    ├── enroll/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── __pycache__/
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_remove_student_studid.py
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   ├── static/
    │   │   └── enroll/
    │   │       └── js/
    │   │           └── datatable.js
    │   └── templates/
    │       └── enroll/
    │           ├── addstudent.html
    │           ├── base.html
    │           └── updateInfo.html
    └── sales/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── signals.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        ├── __pycache__/
        ├── migrations/
        │   ├── 0001_initial.py
        │   ├── __init__.py
        │   └── __pycache__/
        ├── static/
        │   └── sales/
        │       ├── css/
        │       │   ├── bootstrap.css
        │       │   ├── core.css
        │       │   ├── dtable.css
        │       │   └── fa.css
        │       ├── images/
        │       └── js/
        │           ├── bootstrap.js
        │           ├── core.js
        │           ├── fa.js
        │           ├── jquery.js
        │           └── popper.js
        └── templates/
            └── sales/
                ├── base.html
                ├── datatable.html
                ├── new_records.html
                └── salesinfo.html
```

---

## Prerequisites
1. **Python 3.8+**
2. **Django 4.x**
3. **SQLite** (default database)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yash211/Django-CRUD-Datatables.git
   cd Django-CRUD-Datatables
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Usage
### CRUD Operations
- **Add Student**: Navigate to `/enroll/add` to add a new student.
- **Edit Student**: Click on the update button in the DataTable.
- **Delete Student**: Click on the delete button in the DataTable.
- **View Sales Records**: Navigate to `/sales/` to explore sales data.

### Validation
- Custom password validation ensures that the password field adheres to predefined constraints.

---

## Learning Highlights
- Used Django's model-view-template (MVT) architecture.
- Explored integration with DataTables for dynamic table rendering.
- Applied Jinja templating to create reusable and efficient templates.
- Hands-on experience with migrations and static file management in Django.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Author
[**Yash211**](https://github.com/yash211)

