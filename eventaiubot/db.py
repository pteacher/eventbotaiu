import sqlite3

class BotDB:

    def __init__(self, db_file):
        """Initialize connection with db"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def add_record(self, name, date, time, place):
        """Create a note about event"""
        self.cursor.execute("INSERT INTO `events` (`name`, `date`, `time`,`place`) VALUES (?,?,?,?)",(name,date,time,place,))
            # (self.get_user_id(user_id),
            # operation == '+',
            # value))
        return self.conn.commit()

    def close(self):
        """Close connection with db"""
        self.conn.close()