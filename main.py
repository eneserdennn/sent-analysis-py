import json
from flask import Flask, redirect, url_for, request
from flask_restful import Resource, Api
from transformers import pipeline


classifier = pipeline("text-classification",model='nlptown/bert-base-multilingual-uncased-sentiment', return_all_scores=True)

app = Flask(__name__)


@app.route('/sent',methods = ['POST', 'GET'])
def analyze():
   if request.method == 'POST':
      data = request.form['text']
      prediction = classifier(data)
      return json.dumps(prediction)
   else:
      data = request.args.get('text')
      return redirect(url_for('success',form = data))

if __name__ == '__main__':
   app.run(host="127.0.0.1", port=8080, debug=True)
