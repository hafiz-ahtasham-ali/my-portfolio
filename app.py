from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="assets", template_folder=".")

# Route for serving the main index.html
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Route for other static HTML files
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)

if __name__ == "__main__":
    app.run(debug=True)