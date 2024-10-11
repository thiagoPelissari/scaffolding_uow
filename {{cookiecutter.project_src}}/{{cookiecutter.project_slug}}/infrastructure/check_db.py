from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import psycopg2

DATABASE_URL = "postgresql://my_custom_user:secret@127.0.0.1:5433/my_project"

def create_database():
    # Conectar ao banco "postgres", que é o banco de sistema do PostgreSQL
    default_db_url = DATABASE_URL.rsplit("/", 1)[0] + "/postgres"
    engine = create_engine(default_db_url)
    
    with engine.connect() as conn:
        conn.execute("commit")  # Encerrar a transação aberta
        conn.execute(f"CREATE DATABASE my_project")
        print("Banco de dados 'my_project' criado com sucesso.")

def check_and_create_db():
    try:
        # Tentar conectar ao banco de dados principal
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            print(f"Conectado ao banco de dados '{DATABASE_URL.rsplit('/', 1)[1]}' com sucesso.")
    except OperationalError:
        print(f"Banco de dados 'my_project' não encontrado. Criando banco de dados...")
        create_database()

if __name__ == "__main__":
    check_and_create_db()
