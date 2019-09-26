from flask import Flask, render_template,request
import data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',aboutMe=data.aboutMe, aboutArticle=data.aboutArticle)

@app.route('/articles/<dataArticle>')
def func_name(dataArticle):
    return render_template('articles.html',aboutMe=data.aboutMe,param=dataArticle,aboutArticle=data.aboutArticle)

@app.route('/about')
def about():
    return render_template('about.html',aboutMe=data.aboutMe,aboutCV=data.aboutCV,aboutWorking=data.aboutWorking)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 