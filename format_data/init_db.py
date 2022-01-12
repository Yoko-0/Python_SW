from utils.db import Database

def init_table():

    db = Database()

    db.cur.execute('''CREATE TABLE FORMAT_DATA
        (
            id SERIAL PRIMARY KEY,
            connection INTEGER,
            name VARCHAR(255) NOT NULL,
            description VARCHAR(255),
            config json,
            type VARCHAR(50),
            infra_type VARCHAR(50),
            port_channel_id INTEGER,
            max_frame_size INTEGER
        );''')

    print("Table created successfully")
    db.con.commit()
    db.con.close()
    
    return True
