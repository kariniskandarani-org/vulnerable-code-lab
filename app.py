import flask
import jwt

app = flask.Flask(__name__)

# 🚨 Hardcoded secret key (will be flagged)
SECRET_KEY = "sk_test_51H8L23FKEC9zFakeSecret"

@app.route("/jwt")
def generate_token():
    payload = {"user": "admin"}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# 🚨 SQL Injection risk
@app.route("/login")
def login():
    username = flask.request.args.get("username")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return f"Running query: {query}"

if __name__ == "__main__":
    app.run(debug=True)
