from db_connection import Database

db = Database()


def readparticipants():
    db.connect()
    query = 'SELECT * FROM eventmanager.people;'
    cursor = db.conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.disconnect()
    return results


def update_presence(participant_id, presence):
    db.connect()
    query = 'UPDATE eventmanager.people SET presence = %s WHERE id= %s'
    cursor = db.conn.cursor()
    cursor.execute(query, (presence, participant_id))
    db.conn.commit()
    db.disconnect()

