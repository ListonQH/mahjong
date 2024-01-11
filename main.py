from flask import Flask, render_template

app=Flask(__name__)

@app.route('/createRoom')
def create_room():
    return 'Create Room!'


@app.route('/')
def index():
    msg="my name is caojianhua, China up!"
    return render_template("index.html", data=msg)  #加入变量传递

if __name__=="__main__":
    app.run(port=2024,host="127.0.0.1",debug=True)   #调用run方法，设定端口号，启动服务