from flask import Flask, render_template, request, redirect
from utils import add_transaction, save_to_csv,view_summary

app= Flask(__name__)
DATA_FILE = "data/budget.csv"


@app.route('/')
def index():
     return render_template('index.html')

@app.route('/cashflow',methods=['POST'])
def cashflow():
    date = request.form['date']
    item = request.form['item']
    category = request.form['category']
    amount = request.form['amount']
    type_=request.form['type']

    data = add_transaction(date, item, category, amount,type_ )
    save_to_csv(data, DATA_FILE)

    return redirect('/summary')

@app.route('/summary',methods=['GET'])
def summary():
    result = view_summary(DATA_FILE)
    return render_template('summary.html', summary=result)


if __name__ == '__main__':
    app.run(debug=True)

