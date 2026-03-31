from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form.get('text', '')
    language = request.form.get('language', 'english')
    
    language_name = 'Arabic' if language == 'arabic' else 'English'
    message = f'Story submitted in {language_name}! ({len(text)} characters)'
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
