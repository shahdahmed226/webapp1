from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Shahd App</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #667eea, #764ba2);
                font-family: Arial, sans-serif;
            }

            .card {
                background: white;
                padding: 60px;
                border-radius: 20px;
                box-shadow: 0 15px 40px rgba(0,0,0,0.2);
                text-align: center;
            }

            h1 {
                font-size: 60px;
                margin: 0;
                color: #333;
            }

            p {
                font-size: 28px;
                margin-top: 20px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello 👋</h1>
            <p>My Name is Shahd Hussein</p>
        </div>
    </body>
    </html>
    """

