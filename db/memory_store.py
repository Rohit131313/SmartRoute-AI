import sqlite3

def init_db():
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_type TEXT,
            intent TEXT,
            routed_agent TEXT,
            extracted_data TEXT
        )
    """)
    conn.commit()
    conn.close()

def store_result(file_type, intent, routed_agent, extracted_data):
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO memory_log (file_type, intent, routed_agent, extracted_data)
        VALUES (?, ?, ?, ?)
    """, (file_type, intent, routed_agent, str(extracted_data)))
    conn.commit()
    conn.close()

