from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    wallet_address = "TPXBvrXhqzUnaU7QjJmTcpYefbiLLtFHnJ"
    balance = 1000000  # Simulated balance
    return render_template("index.html", balance=balance, wallet_address=wallet_address)

if __name__ == '__main__':
    app.run(debug=True)
