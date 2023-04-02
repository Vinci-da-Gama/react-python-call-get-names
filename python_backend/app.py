from flask import Flask, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS
CORS(app)


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
    response = jsonify(names=names)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run()
