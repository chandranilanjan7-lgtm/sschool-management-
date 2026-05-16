from flask import Flask, request

app = Flask(__name__)

# ---------------- HOME PAGE ----------------

@app.route("/")
def home():

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>My School Website</title>

        <style>

            body{
                background:#f0f0f0;
                text-align:center;
                font-family:Arial;
                padding-top:50px;
            }

            h1{
                color:blue;
            }

            button{
                padding:12px;
                font-size:18px;
                margin:10px;
                border:none;
                background:green;
                color:white;
                border-radius:10px;
            }

        </style>

    </head>

    <body>

        <h1>WELCOME TO MY SCHOOL</h1>

        <p>AI School Website Made In Pydroid 3</p>

        <a href='/login'>
            <button>Student Login</button>
        </a>

        <br>

        <a href='/chatbot'>
            <button>AI Teacher Bot</button>
        </a>

    </body>

    </html>
    """

# ---------------- LOGIN PAGE ----------------

@app.route("/login")
def login():

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>Login</title>

        <style>

            body{
                background:#e8f5e9;
                text-align:center;
                font-family:Arial;
                padding-top:50px;
            }

            input{
                padding:10px;
                width:250px;
                margin:10px;
                font-size:18px;
            }

            button{
                padding:10px;
                width:150px;
                background:blue;
                color:white;
                border:none;
                border-radius:10px;
                font-size:18px;
            }

        </style>

    </head>

    <body>

        <h1>Student Login</h1>

        <input type='text' placeholder='Username'>

        <br>

        <input type='password' placeholder='Password'>

        <br>

        <button>Login</button>

        <br><br>

        <a href='/'>Back To Home</a>

    </body>

    </html>
    """

# ---------------- CHATBOT PAGE ----------------

@app.route("/chatbot")
def chatbot():

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>AI Teacher Bot</title>

        <style>

            body{
                background:#fff3e0;
                text-align:center;
                font-family:Arial;
                padding-top:50px;
            }

            input{
                padding:12px;
                width:300px;
                font-size:18px;
            }

            button{
                padding:12px;
                background:green;
                color:white;
                border:none;
                border-radius:10px;
                font-size:18px;
            }

            #answer{
                margin-top:20px;
                font-size:22px;
                color:blue;
            }

        </style>

    </head>

    <body>

        <h1>School AI Teacher Bot</h1>

        <input id='q' placeholder='Ask your question'>

        <button onclick='askBot()'>Ask</button>

        <p id='answer'></p>

        <br>

        <a href='/'>Back To Home</a>

        <script>

        async function askBot(){

            let question =
            document.getElementById('q').value;

            let response =
            await fetch('/ask', {

                method:'POST',

                headers:{
                    'Content-Type':
                    'application/x-www-form-urlencoded'
                },

                body:'question=' + question

            });

            let data = await response.json();

            document.getElementById('answer').innerHTML =
            data.answer;

        }

        </script>

    </body>

    </html>
    """

# ---------------- AI ANSWER SYSTEM ----------------

@app.route("/ask", methods=["POST"])
def ask():

    question = request.form["question"].lower()

    if "science" in question:
        answer = "Science is the study of nature and experiments."

    elif "math" in question:
        answer = "Math is the study of numbers and calculations."

    elif "history" in question:
        answer = "History teaches us about the past."

    elif "computer" in question:
        answer = "A computer is an electronic machine."

    elif "python" in question:
        answer = "Python is a programming language."

    elif "earth" in question:
        answer = "Earth is the planet where humans live."

    elif "biology" in question:
        answer = "Biology studies living organisms."

    elif "physics" in question:
        answer = "Physics studies force and energy."

    elif "chemistry" in question:
        answer = "Chemistry studies chemicals and reactions."

    elif "english" in question:
        answer = "English is an international language."

    elif "geography" in question:
        answer = "Geography studies places and countries."

    elif "what is ai" in question:
        answer = "AI means Artificial Intelligence."

    elif "hello" in question:
        answer = "Hello student!"

    else:
        answer = "I do not know this answer yet."

    return {"answer": answer}

# ---------------- RUN WEBSITE ----------------

app.run(host="0.0.0.0", port=5000)