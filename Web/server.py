from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import os

app = Flask(__name__)

W = tf.Variable(tf.random.normal([4, 1], dtype=tf.float32), name="weight")
b = tf.Variable(tf.random.normal([1], dtype=tf.float32), name="bias") # 가중치와 편향 초기화

def hypothesis(X): 
    return tf.matmul(X, W) + b # 가설 설정

ckpt = tf.train.Checkpoint(W=W, b=b)
checkpoint_path = os.path.join(os.getcwd(), 'model/saved.ckpt-1')  
ckpt.restore(checkpoint_path).expect_partial() # 불러오기  

@app.route('/', methods=['GET', 'POST'])
def predict():
    price = None
    if request.method == 'POST':
        try:
            avg_temp = float(request.form['avg_temp'])
            min_temp = float(request.form['min_temp'])
            max_temp = float(request.form['max_temp'])
            rain_fall = float(request.form['rain_fall']) # 입력값 받기

            data = np.array([[avg_temp, min_temp, max_temp, rain_fall]], dtype=np.float32) # 데이터를 배열로 변환

            prediction = hypothesis(data).numpy() # 예측 값 계산
            price = prediction[0][0]  

        except Exception as e:
            print(f"Error occurred: {e}")

    return render_template('index.html', price=price)

if __name__ == "__main__":
    app.run(debug=True)
