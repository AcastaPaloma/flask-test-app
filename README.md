

# 🌟 Flask Web App 🌟

Welcome to the **Flask Web App**! This is a simple project that demonstrates how to build a small web application using Python's Flask framework, HTML for structure, and CSS for styling.

## 🚀 Project Overview

This web app displays a homepage with a welcoming message. The structure is written in HTML, styled with CSS, and served using Flask, a lightweight and powerful web framework for Python.

## 💻 Technologies Used

- **Flask**: A micro web framework for Python to handle server-side logic.
- **HTML**: To structure the content on the web page.
- **CSS**: To style the web page and make it look pretty.
- **Python**: Handles the backend and routing for the web app.

---

## 🛠️ Installation Guide

Follow these steps to run the app locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-app.git
cd flask-app
```

### 2. Install Flask

First, ensure you have Python installed (you can download it from [here](https://www.python.org/downloads/)).

Then, install Flask via pip:

```bash
pip install flask
```

### 3. Run the Flask App

Now, you're ready to run the application!

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000/` to view the app.

---

## 🔍 What is Flask?

Flask is a lightweight web framework for Python. It's called a "micro" framework because it provides the basic tools to create web apps but doesn’t require complex libraries or tools like some other frameworks.

In this project, Flask is used to:

- **Route requests**: Direct the user to the correct web page.
- **Render HTML templates**: Display dynamic content using Python and HTML.

---

## 📁 Project Structure

```
flask_app/
    ├── static/
    │   └── styles.css       # Your CSS file for styling the HTML
    ├── templates/
    │   └── index.html       # The HTML template that Flask renders
    └── app.py               # The Flask server handling everything
```

### How It All Connects:

1. **HTML**: The structure of the webpage (found in `templates/index.html`).
2. **CSS**: The styles that make the page look nice (found in `static/styles.css`).
3. **Python (Flask)**: Flask handles the server-side operations, routes the URL requests, and renders the HTML page. When you navigate to the root URL (`/`), the `app.py` file tells Flask to serve the `index.html` file.

---

## 🎨 Features

- Displays a welcoming message on the homepage.
- Clean and minimal styling with custom CSS.
- Simple yet effective demonstration of how Flask works.

---

## 🤝 Contributing

Feel free to submit pull requests or suggest changes to improve this project!

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

Hope you enjoy exploring Flask! ✨

