def postgres_connect():
    import psycopg2
    from psycopg2 import sql

    # Database connection parameters
    db_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'postgres',   
        'host': 'localhost',  # or your database host
        'port': '5432'        # default PostgreSQL port
    }

    try:
        # Establish the connection
        conn = psycopg2.connect(**db_params)
        print("Connection to PostgreSQL database successful.")

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a simple SQL query
        cursor.execute("SELECT version();")
        
        # Fetch and print the result
        db_version = cursor.fetchone()
        print("Database version:", db_version)

        # Close the cursor and connection
        cursor.close()
        conn.close()
        print("Connection closed.")
    except Exception as e:
        print("An error occurred while connecting to the database:", e)

