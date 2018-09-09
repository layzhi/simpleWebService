from flask import Flask, render_template
import re

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi, to get a specific line of the file, please send a request to http://localhost:5000/GET/(line you wish to get.)'


@app.route('/GET/<line>')
def GET(line):
    line = checkIndex(line)
    return render_template('index.html', line=line)

def checkIndex(lineIndex):
    numCheck = re.match('^[+]?[0-9]+$', lineIndex)
    if (numCheck): 
        return parseFile(lineIndex)
    else: 
        return 'line is not a valid number'

def parseFile(index):
    i = int(index) - 1
    inputFile = open('test.txt')
    lines = inputFile.readlines()
    return lines[i]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')