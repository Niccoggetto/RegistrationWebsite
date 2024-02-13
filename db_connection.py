import mysql.connector


class Database:
    conn = None

    def __init__(self):
        self.user = 'remote'
        self.password = 'Palleggio5'
        self.host = '192.168.1.120'
        self.port = 3306
        self.database = 'eventmanager'

    '''def __init__(self):
        self.user = 'root'
        self.password = ''
        self.host = '127.0.0.1'
        self.port = 3306
        self.database = 'events' '''

    def connect(self):
        if not Database.conn or not Database.conn.is_connected():
            config = {
                'user': self.user,
                'password': self.password,
                'host': self.host,
                'database': self.database,
                'raise_on_warnings': True
            }
            try:
                Database.conn = mysql.connector.connect(**config)
            except mysql.connector.Error as err:
                print(f'Errore: {err}')

    def disconnect(self):
        if Database.conn and Database.conn.is_connected():
            Database.conn.close()

    def query(self, query, parameters=None):
        try:
            if not Database.conn or not Database.conn.is_connected():
                self.connect()

            cursor = Database.conn.cursor()

            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)

            Database.conn.commit()
        except mysql.connector.Error as err:
            print(f'Errore durante l\'esecuzione della query: {err}')
            return False
        finally:
            if cursor:
                cursor.close()

        return True
