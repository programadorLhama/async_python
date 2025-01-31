from databases import Database

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///./schema.db"
        self.__database = Database(self.__connection_string)

    async def connect_to_db(self):
        await self.__database.connect()

    async def disconnect_to_db(self):
        await self.__database.disconnect()

    def get_db_conn(self):
        return self.__database


db_connection_handler = DBConnectionHandler()
