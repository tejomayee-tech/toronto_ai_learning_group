#pip install psycopg2-binary
import psycopg2
import json

connection = psycopg2.connect( 
                host = "localhost",
                port = 5432,
                dbname = "postgres",
                user = "postgres",
                password = "Admin@123"
                    )

cur = connection.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS public.car (
    id SERIAL PRIMARY KEY,
    name TEXT,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT now()
);
""")

connection.commit()


car_json = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2024,
    "features": ["ABS", "Airbags", "Hybrid"],
    "engine": {
        "type": "Hybrid",
        "hp": 138

    }
}

car_json = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2024,
    "features": ["ABS", "Airbags", "Hybrid"],
    "engine": {
        "type": "Hybrid",
        "hp": 138

    }
}

cur.execute("""
        INSERT INTO public.car (name,metadata)
            VALUES (%s, %s);
            """, ( "vijay'car", json.dumps(car_json)) 
)

connection.commit()

cur.execute("""
            SELECT * FROM public.car
    ORDER BY id ASC 
            """)

data = cur.fetchall()
print(data)



cur.close()

connection.close()