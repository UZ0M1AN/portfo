from flask import Flask, render_template, url_for, request, redirect
import csv

# /////////////////////////////////////////////////////////////////////////
# //////////  FUNCTIONS  ///////////////////////////////////////
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# ///////////////////////////////////////////////////////////////////////////////

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again!'




# ///////////////////////////////////////////////////////////
# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     # print(url_for('static', filename='favicon.ico')) # better than just hardcoding the name, as in, /static/favicon.ico
#     return render_template('./index.html', name=username, post_id=post_id) # doesn't work bc the fxn tries to look in a 'templates' folder but index.html is currently not in there, so let's create it and put our 'index.html' in there, and any other future html files we may have

# @app.route("/blog")
# def blog():
#     return "These are my thoughts on blogs"
# won't be executed bc once it sees a route, it ignores the rest of the code and exec the fxn of that route
# //////////////////////////////////////////////////////////