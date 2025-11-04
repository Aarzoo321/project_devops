from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>DevOps CI/CD Demo "showcase-1" 🚀</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg,#e3f2fd,#fff);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
    }
    #box {
        background: white;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        text-align: center;
        width: 380px;
    }
    h1 { color:#004d99; }
    p { font-size: 18px; color:#333; }
    button {
        padding: 12px 20px;
        background:#007BFF;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        margin-top: 15px;
        font-size: 16px;
    }
    button:hover { background:#0056b3; }
    #message {
        margin-top: 15px;
        font-size: 20px;
        color: #008000;
        font-weight: bold;
    }
</style>
<script>
function showMessage() {
    document.getElementById("message").innerHTML = 
        "✅ CI/CD Triggered Successfully!";
}

function showTime() {
    const now = new Date();
    document.getElementById("time").innerHTML = 
        "⏰ Current Time: " + now.toLocaleTimeString();
}
setInterval(showTime, 1000);
</script>
</head>
<body>
    <div id="box">
        <h1>Welcome to DevOps CI/CD Pipeline 🚀</h1>
        <p>Your pipeline is running smoothly</p>
        <p>Docker + Jenkins + GitHub ✅</p>

        <p id="time"></p>

        <button onclick="showMessage()">Run CI/CD Action</button>
        <p id="message"></p>
    </div>
</body>
</html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
