from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page ('/')
@app.route('/')
def home():
    """
    This function is triggered when the user accesses the root URL (http://127.0.0.1:5000/).
    It renders the 'index.html' template located in the 'templates' folder.
    """
    print("Home route accessed")  # Debugging print statement to check if the route is triggered
    return render_template('index.html')  # Render the HTML template

# Check if this is the main module being run and start the Flask app
if __name__ == "__main__":
    # Run the application in debug mode. This helps track and display errors in the browser.
    app.run(debug=True)
