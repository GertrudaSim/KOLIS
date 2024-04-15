#ATSISKAITYMAS
from flask import Flask, render_template, request

app = Flask(__name__)

# Laikinas duomenų saugojimas
tasks = []

# Maršrutas pagrindiniam puslapiui
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Maršrutas užduoties registravimui
@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        status = request.form.get('status')
        user = request.form.get('user')
        task = {'name': name, 'description': description, 'status': status, 'user': user}
        tasks.append(task)
    return render_template('add_task.html')

# Maršrutas užduoties modifikavimui
@app.route('/modify_task', methods=['GET', 'POST'])
def modify_task():
    if request.method == 'POST':
        # Čia užduoties modifikavimas
        pass
    return render_template('modify_task.html')

# Maršrutas užduoties statuso keitimui
@app.route('/change_status', methods=['GET', 'POST'])
def change_status():
    if request.method == 'POST':
        # Čia užduoties statuso keitimas
        pass
    return render_template('change_status.html')

# Maršrutas vartotojo priskyrimui užduočiai
@app.route('/assign_user', methods=['GET', 'POST'])
def assign_user():
    if request.method == 'POST':
        # Čia vartotojo priskyrimas užduočiai
        pass
    return render_template('assign_user.html')

if __name__ == '__main__':
    app.run(debug=True)
