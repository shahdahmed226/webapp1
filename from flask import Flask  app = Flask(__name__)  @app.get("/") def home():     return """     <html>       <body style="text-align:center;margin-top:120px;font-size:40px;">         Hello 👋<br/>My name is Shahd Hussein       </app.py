from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <html>
      <body style="text-align:center;margin-top:120px;font-size:40px;">
        Hello 👋<br/>My name is Shahd Hussein
      </body>
    </html>
    """
