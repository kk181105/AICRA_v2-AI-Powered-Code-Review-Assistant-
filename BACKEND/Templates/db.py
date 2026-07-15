import pyodbc

server = r'BUJU\MSSQLSERVER03'
database = 'aicra'

conn = pyodbc.connect(
    f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
)

cursor = conn.cursor()


def save_code(code):

    print("Saving code:", code)   # ← add this line

    cursor.execute(
        "INSERT INTO code(text) VALUES (?)",
        code
    )

def save_review(code, message, context, fragility, prediction):

    print("Saving review...")

    cursor.execute(
        "INSERT INTO review_history(code,message,context_score,fragility_score,prediction) VALUES (?,?,?,?,?)",
        code, message, context, fragility, prediction
    )

    conn.commit()

def get_stats():

    stats = {}

    cursor.execute("SELECT COUNT(*) FROM review_history")
    stats["reviews"] = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(fragility_score) FROM review_history")
    avg = cursor.fetchone()[0]

    if avg is None:
        avg = 0

    stats["fragility"] = int(avg)

    cursor.execute("SELECT TOP 1 prediction FROM review_history ORDER BY id DESC")
    row = cursor.fetchone()

    if row:
        stats["prediction"] = row[0]
    else:
        stats["prediction"] = "None"

    return stats 

    conn.commit()

    