from sqlalchemy import create_engine

databas = create_engine("sqlite:///example.db")

with databas.connect() as conn:
    print("OK")