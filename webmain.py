from db_connection import Database
from flask import Flask, render_template, request
from cocktails import Cocktail, cocktails_list

db = Database()
db.connect()

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('registration.html', cocktails_list=cocktails_list)


@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    surname = request.form['surname']
    phone = request.form['phone']
    paymentchoice = request.form['paymentchoice']

    for c in cocktails_list:
        cocktail_count = request.form.get(f'{c.nome}Count')
        print(cocktail_count)
        if cocktail_count != 0:
            insert_cocktail_query = f"UPDATE alcohol SET quantity = quantity + %s WHERE name = {c.nome}"
            db.query(insert_cocktail_query, (cocktail_count,))

    insert_data_query = "INSERT INTO people (name, surname, phone, payment) VALUES (%s, %s, %s, %s)"
    people_data = (name, surname, str(phone), paymentchoice)
    db.query(insert_data_query, people_data)

    return render_template('thanku.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
