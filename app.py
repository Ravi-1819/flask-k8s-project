from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Welcome</title>
<style>
body{
    margin:0;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
    background:linear-gradient(135deg,#0f172a,#1e3a8a);
    overflow:hidden;
    font-family:Arial,sans-serif;
}

.container{
    text-align:center;
}

.robot{
    position:relative;
    width:180px;
    height:250px;
    margin:auto;
    animation:float 3s ease-in-out infinite;
}

.head{
    width:120px;
    height:100px;
    background:#dfe6e9;
    border-radius:20px;
    margin:auto;
    position:relative;
    box-shadow:0 10px 20px rgba(0,0,0,.4);
}

.eye{
    position:absolute;
    width:18px;
    height:18px;
    background:#00e5ff;
    border-radius:50%;
    top:35px;
    box-shadow:0 0 15px #00e5ff;
    animation:blink 4s infinite;
}

.left{left:28px;}
.right{right:28px;}

.mouth{
    position:absolute;
    width:40px;
    height:6px;
    background:#555;
    bottom:22px;
    left:40px;
    border-radius:10px;
}

.antenna{
    width:6px;
    height:28px;
    background:white;
    position:absolute;
    top:-28px;
    left:57px;
}

.ball{
    width:14px;
    height:14px;
    background:red;
    border-radius:50%;
    position:absolute;
    top:-38px;
    left:53px;
    animation:glow 1s infinite alternate;
}

.body{
    width:150px;
    height:120px;
    background:#ecf0f1;
    margin:10px auto;
    border-radius:20px;
    box-shadow:0 10px 20px rgba(0,0,0,.4);
    position:relative;
}

.logo{
    position:absolute;
    top:35px;
    left:35px;
    width:80px;
    height:40px;
    line-height:40px;
    background:#2563eb;
    color:white;
    border-radius:10px;
    font-weight:bold;
}

.arm{
    width:20px;
    height:90px;
    background:#dfe6e9;
    position:absolute;
    top:110px;
}

.left-arm{
    left:-10px;
    transform:rotate(25deg);
}

.right-arm{
    right:-10px;
    transform:rotate(-25deg);
}

.leg{
    width:22px;
    height:70px;
    background:#dfe6e9;
    position:absolute;
    bottom:-70px;
}

.left-leg{
    left:40px;
}

.right-leg{
    right:40px;
}

h1{
    color:white;
    margin-top:40px;
    font-size:40px;
}

p{
    color:#ddd;
    font-size:22px;
}

@keyframes float{
0%,100%{transform:translateY(0);}
50%{transform:translateY(-20px);}
}

@keyframes glow{
from{box-shadow:0 0 5px red;}
to{box-shadow:0 0 20px red;}
}

@keyframes blink{
0%,45%,100%{height:18px;}
50%{height:3px;}
}
</style>
</head>

<body>

<div class="container">

<div class="robot">

<div class="head">
<div class="antenna"></div>
<div class="ball"></div>
<div class="eye left"></div>
<div class="eye right"></div>
<div class="mouth"></div>
</div>

<div class="body">
<div class="logo">K8S</div>
</div>

<div class="arm left-arm"></div>
<div class="arm right-arm"></div>

<div class="leg left-leg"></div>
<div class="leg right-leg"></div>

</div>

<h1>🤖 Welcome!</h1>

<p>
Running Successfully on<br>
Kubernetes + Docker + Kind
</p>

</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

