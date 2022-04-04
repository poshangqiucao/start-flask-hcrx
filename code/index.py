from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='/static', # 配置静态文件的访问 url 前缀
            static_folder='static',    # 配置静态文件的文件夹
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
