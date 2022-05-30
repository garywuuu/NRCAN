from flask import Flask, render_template, redirect, url_for, request
import os


app = Flask(__name__,
    static_url_path='',static_folder='web/static',template_folder='web/templates'
)

port = int(os.environ.get("PORT", 5000))

@app.route('/')
def hello_world():
    return render_template('index.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        print(request.form)
        print("^ This is the request form.")
        # return redirect(url_for('success', name=user, _external=True))
        return redirect(f"https://nrcan.herokuapp.com/success/{user}")
    # else:
    #     user = request.args.get('nm')
    #     return redirect(url_for('success', name=user))
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(host='0.0.0.0', port=port)