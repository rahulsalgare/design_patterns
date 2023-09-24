import threading


class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                cls._instance = super(Database, cls).__new__(cls)

        return cls._instance

    def query(self, sql):
        print('executing, ', sql)


if __name__ == '__main__':
    db1 = Database()
    db1.query("SELECT * FROM ...")

    db2 = Database()
    print(id(db1) == id(db2))
