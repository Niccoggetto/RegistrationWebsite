from db_connection import Database
from flask import Flask, render_template, request, jsonify
from cocktails import Cocktail, cocktails_list

db = Database()
db.connect()

app = Flask(__name__, template_folder='templates')


@app.route('/')
def form():
    return render_template('registration.html', cocktails_list=cocktails_list)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    print(request.form)
    name = request.form['name']
    surname = request.form['surname']
    phone = request.form['phone']
    paymentchoice = request.form['paymentchoice']

    for c in cocktails_list:
        '''cocktail_count = request.form[f'quantity_{c.nome}']
        print(cocktail_count)'''         #problema quiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
        cocktail_name = f'quantity_{c.nome}'
        print(f"Checking {cocktail_name}:", request.form.get(cocktail_name))
        cocktail_count = request.form.get(cocktail_name)
        if cocktail_count is not None:
            cocktail_count = int(cocktail_count)
            insert_cocktail_query = f"UPDATE alcohol SET quantity = quantity + %s WHERE name = '{c.nome}'"
            db.query(insert_cocktail_query, (cocktail_count,))
            print("done")

    insert_data_query = "INSERT INTO people (name, surname, phone, payment) VALUES (%s, %s, %s, %s)"
    people_data = (name, surname, str(phone), paymentchoice)
    db.query(insert_data_query, people_data)

    return render_template('thanku.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
