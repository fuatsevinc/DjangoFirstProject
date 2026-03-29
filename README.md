# DjangoFirstProject – First Django Web Application

> A beginner-level Django web application demonstrating the basics of Django project structure and setup.

---

## About the Project

DjangoFirstProject is a foundational Django application built while learning the Django web framework. It includes a HelloWorld app and a main configuration app, demonstrating Django's project structure, URL routing, views, and settings configuration.

---

## Features

- Basic Django project structure with app separation
- HelloWorld app with simple views
- Django URL routing and view rendering
- Django admin panel access
- requirements.txt for dependency management

---

## Technologies Used

| Technology | Version |
|---|---|
| Python | 3.10 |
| Django | 4.0 |

---

## Project Structure

```
DjangoFirstProject/
├── helloworld/     # Hello World demo app
├── main/           # Core Django app (settings, urls)
├── manage.py
└── requirements.txt
```

---

## Getting Started

Follow these steps to run the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/fuatsevinc/DjangoFirstProject
   cd DjangoFirstProject
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit: `http://127.0.0.1:8000/`

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

Developed by [fuatsevinc](https://github.com/fuatsevinc) · [www.fuatsevinc.com](https://www.fuatsevinc.com)
