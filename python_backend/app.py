from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/names')
def get_names():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="boamia",
        password=""
    )
    # Create a cursor object
    cur = conn.cursor()
    cur.execute("SELECT value FROM names")
    # Fetch the results
    rows = cur.fetchall()
    names = [row[0] for row in rows]

    # Close the cursor and connection
    cur.close()
    conn.close()
    return jsonify(names=names)

if __name__ == '__main__':
    app.run()
