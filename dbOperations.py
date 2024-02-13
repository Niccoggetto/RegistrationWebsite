from db_connection import Database

db = Database()


def readparticipants():
    db.connect()
    query = 'SELECT * FROM eventmanager.people;'
    # per sviluppo in locale:
    #query = 'SELECT * FROM events.people;'
    cursor = db.conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.disconnect()
    return results


def update_presence(participant_id, presence):
    db.connect()
    query = 'UPDATE eventmanager.people SET presence = %s WHERE id= %s'
    # per sviluppo in locale
    #query = 'UPDATE events.people SET presence = %s WHERE id= %s'
    cursor = db.conn.cursor()
    cursor.execute(query, (presence, participant_id))
    db.conn.commit()
    db.disconnect()

def countnum(phone):
    db.connect()
    query = "SELECT COUNT(*) FROM eventmanager.people WHERE phone = %s"
    cursor = db.conn.cursor()
    cursor.execute(query, (phone,))
    results = cursor.fetchall()[0][0]
    db.disconnect()
    return results
