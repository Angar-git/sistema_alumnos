from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "flash message"

#CONFIGURACIONES DE MYSQL
app.config['MYSQL_HOST']='192.168.0.124'
app.config['MYSQL_USER']='myuser'
app.config['MYSQL_PASSWORD']='myuser'
app.config['MYSQL_DB']='Dalumnos'

mysql = MySQL(app)

#ENRUTAMIENTO
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tAlumnos")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', alumnos = data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        try:
            flash("Se agregó correctamente")
            boleta = request.form['inputBoleta']
            aPat = request.form['inputAPat']
            aMat = request.form['inputAMat']
            nombre = request.form['inputNombre']
            curp = request.form['inputCurp']

            cur = mysql.connection.cursor()
            cur.execute("""
                INSERT INTO tAlumnos(boleta, nombre, aPaterno, aMaterno, CURP, activo) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (boleta, aPat, aMat, nombre, curp, 1))
            mysql.connection.commit()

            return redirect(url_for('Index'))
        except:
            flash("No se peude agregar boleta o CURP existentes")
            return redirect(url_for('Index'))


@app.route('/update', methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        try:
            flash("Se actualizó correctamente")
            id_data = request.form['id']
            boleta = request.form['inputBoleta']
            aPat = request.form['inputAPat']
            aMat = request.form['inputAMat']
            nombre = request.form['inputNombre']
            curp = request.form['inputCurp']

            cur = mysql.connection.cursor()
            cur.execute("""
                UPDATE tAlumnos
                SET boleta = %s, nombre = %s, aPaterno = %s, aMaterno = %s, CURP = %s
                WHERE id=%s
            """, (boleta, aPat, aMat, nombre, curp, id_data))
            mysql.connection.commit()
            return redirect(url_for('Index'))
        except:
            flash("No se puede actualizar boleta o CURP existentes")
            return redirect(url_for('Index'))

@app.route('/desactivar', methods = ['POST', 'GET'])
def desactivar():
    if request.method == 'POST':
        flash("Se desactivó correctamente")
        id_data = request.form['id']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE tAlumnos
            SET activo=%s
            WHERE id=%s
        """, (0, id_data))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/activar', methods = ['POST', 'GET'])
def activar():
    if request.method == 'POST':
        flash("Se activó correctamente")
        id_data = request.form['id']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE tAlumnos
            SET activo=%s
            WHERE id=%s
        """, (1, id_data))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete', methods = ['POST', 'GET'])
def delete():
    if request.method == 'POST':
        flash("Se dió de baja correctamente")
        id_data = request.form['id']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE tAlumnos
            SET activo=%s
            WHERE id=%s
        """, (2, id_data))
        mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.debug=True
    app.run(host='192.168.0.184')