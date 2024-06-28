from flask import Flask, render_template, request
app = Flask(__name__)

kinoko_count = 3
takenoko_count = 5
messages = ['kinoko is wonderhul!', 'Takenoko is awesome!']

@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    global kinoko_count, takenoko_count, messages
    if request.form.get("item") == 'kinoko':
        kinoko_count += 1
    elif request.form.get("item") == 'takenoko':
        takenoko_count += 1
    messages.append(request.form.get("message"))
    if len(messages) > 3:
        messages = messages[-3:]
    print(request.form)
    kinoko_percent = kinoko_count / (kinoko_count + takenoko_count) * 100
    takenoko_percent = takenoko_count / (kinoko_count + takenoko_count) * 100
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
