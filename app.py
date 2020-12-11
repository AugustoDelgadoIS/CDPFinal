from flask import Flask, render_template, request, json
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# MySQL configurations
db = pymysql.connect("141.136.33.245", "fundoame", "Compuclinica123@", "fundoame_DBtienda")
cursor = db.cursor()


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    try:
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        if _email and _password:
            sql = "INSERT INTO user_registration(id, email,password) \
               VALUES (NULL,'{0}','{1}')".format('inputEmail', 'inputPassword')
            data = cursor.execute(sql)

            db.commit()

            if len(data) == 0:
                print(" ")
                return json.dumps({'message': 'usuario creado con exito'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span> complete todas las cajas de texto </span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    app.run()
