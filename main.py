from flask import Flask, render_template, request, redirect, session, jsonify, url_for

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "user" and password == "1234":
            session["user"] = username
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid Login")

    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html")


# ---------------- CREDIT SCORE PAGE ----------------
@app.route("/credit-score")
def credit_score():
    if "user" not in session:
        return redirect("/login")
    return render_template("credit_score.html")


# ---------------- CHATBOT PAGE ----------------
@app.route("/chat")
def chat():
    if "user" not in session:
        return redirect("/login")
    return render_template("index.html")


# ---------------- CHATBOT API ----------------
@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_msg = request.json.get("message").lower()

    if "balance" in user_msg:
        reply = "💰 Your account balance is ₹25,000"
    elif "loan" in user_msg:
        reply = "🏦 You have an active loan of ₹1,50,000"
    elif "emi" in user_msg:
        reply = "📅 Your EMI is ₹5,000 per month"
    elif "transaction" in user_msg:
        reply = "📊 You can view transactions in dashboard"
    else:
        reply = "🤖 Sorry, I didn't understand. Try Balance / Loan / EMI"

    return jsonify({"reply": reply})


# ---------------- TRANSACTIONS ----------------
@app.route("/transactions")
def transactions():
    if "user" not in session:
        return redirect("/login")
    return render_template("transactions.html")


# ---------------- LOANS ----------------
@app.route("/loans")
def loans():
    if "user" not in session:
        return redirect("/login")
    return render_template("loans.html")


# ---------------- INVESTMENTS PAGE ----------------
@app.route("/investments")
def investments():
    if "user" not in session:
        return redirect("/login")
    return render_template("investments.html")


# ---------------- TRADE SIMULATION ----------------
@app.route("/trade", methods=["POST"])
def trade():
    if "user" not in session:
        return jsonify({"error": "Not logged in"})

    data = request.json
    action = data.get("action")
    quantity = int(data.get("quantity"))
    price = float(data.get("price"))

    if "wallet" not in session:
        session["wallet"] = 100000

    if "portfolio" not in session:
        session["portfolio"] = 0

    total = quantity * price

    if action == "buy":
        if session["wallet"] >= total:
            session["wallet"] -= total
            session["portfolio"] += quantity
            message = "Stock Purchased Successfully"
        else:
            message = "Insufficient Balance"

    elif action == "sell":
        if session["portfolio"] >= quantity:
            session["wallet"] += total
            session["portfolio"] -= quantity
            message = "Stock Sold Successfully"
        else:
            message = "Not Enough Stocks"

    session.modified = True

    return jsonify({
        "message": message,
        "wallet": session["wallet"],
        "portfolio": session["portfolio"]
    })


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

