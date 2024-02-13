from dbOperations import *
from flask import Flask, render_template, request
from cocktails import Cocktail, cocktails_list

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def form():
    return render_template('registration.html', cocktails_list=cocktails_list)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    name = request.form['name']
    surname = request.form['surname']
    phone = request.form['phone']
    paymentchoice = request.form['paymentchoice']

    count = countnum(phone)

    if count == 0:

        insert_data_query = "INSERT INTO people (name, surname, phone, payment) VALUES (%s, %s, %s, %s)"
        people_data = (name, surname, str(phone), paymentchoice)
        db.query(insert_data_query, people_data)

    else:
        err = 'Questo numero è già stato inserito, ricontrolla. Se non hai sbagliato contatta gli organizzatori.'
        return render_template('registration.html', errorr_message=err, cocktails_list=cocktails_list)

    for c in cocktails_list:

        cocktail_count = int(request.form[f"{c.nome}"])
        if cocktail_count is not None and cocktail_count != 0:
            cocktail_count = int(cocktail_count)
            insert_cocktail_query = f"UPDATE cocktails SET quantity = quantity + %s WHERE name = '{c.nome}'"
            db.query(insert_cocktail_query, (cocktail_count,))

    return render_template('thanku.html', paymentchoice=paymentchoice)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
