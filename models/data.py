import pyodbc

class Database:
    
    @staticmethod   
    def get_connection() -> pyodbc.Connection:
        connection_string = 'DRIVER=ODBC Driver 17 for SQL Server;SERVER=DESKTOP-8QBE9Q1;DATABASE=church;UID=Sanda;PWD=DashDashGo2K23!!'
        try: 
            connection = pyodbc.connect(connection_string)
        except Exception as e:
            raise e
        return connection