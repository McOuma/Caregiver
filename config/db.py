from sqlalchemy import create_engine
database_uri = "sqlite:///care_database.db"
engine = create_engine(database_uri)

def database_connection():
    connection = None
    try:
        with engine.connect() as connection:
            print("Database Connected")
    except Exception as error:
        print(error)
    return connection
