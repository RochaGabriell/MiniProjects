import psycopg2
import psycopg2.extras

hostname = "localhost"
database = "teste"
username = "postgres"
pwd = "adminadmin"
port_id = 5432

conn = None

try:
    with psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id ) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute("DROP TABLE IF EXISTS employee")

            create_script = """CREATE TABLE IF NOT EXISTS employee (
                                    id INT NOT NULL,
                                    name VARCHAR(40) NOT NULL,
                                    salary INT,
                                    dept_id VARCHAR(30),
                                    PRIMARY KEY (id))"""

            cur.execute(create_script)

            insert_script = "INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)"
            insert_value = [(1, 'Natal', 1200, 'D1'), (2, 'Vegana', 320, 'D1'), (3, 'Amaral', 2303, 'D2')]

            for dados in insert_value:
                cur.execute(insert_script, dados)

            delete_script = "DELETE FROM employee WHERE name = %s"
            delete_record = ('Amaral',)
            cur.execute(delete_script, delete_record)
            
            cur.execute("SELECT * FROM employee")
            for record in cur.fetchall():
                print(record)

except Exception as error:
    print(error)

finally:
    if conn is not None:
        conn.close()