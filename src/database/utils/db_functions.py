from typing import Any, Dict, List, Union
import mysql.connector
from mysql.connector.cursor import MySQLCursor
import pandas
import pydoc
# config.py 또는 main.py 등에서

from dotenv import load_dotenv
import os

# .env 파일을 찾아 환경 변수로 로드
load_dotenv()

# 환경 변수 가져오기
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

print(f"DB 접속 정보: {host=} {user=} {password=} {database=}")

def get_connection(host: str, user: str, password: str, database: str="amrbase") -> mysql.connector.connection.MySQLConnectionAbstract:
    """
        GENERATE DATABASE CONNECTION
        INPUT: 
            host : hots url
            user : database user name
            passwor : database user's password
            database : database to use(defualt = amrbase)
            is_buffered : True/False for cursor's buffered option (default = True)
        OUTPUT : 
            MySQLConnectionAbstract : mysql connection object
    """
    db_connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

    return db_connection


def get_connection_and_cursor(host: str, user: str, password: str, database: str="amrbase", is_buffered: bool=True) -> tuple[mysql.connector.connection.MySQLConnectionAbstract, mysql.connector.connection.MySQLConnectionAbstract.cursor]:
    """
        GENERATE DATABASE CONNECTION AND CUROSR
        INPUT: 
            host : hots url
            user : database user name
            passwor : database user's password
            database : database to use(defualt = amrbase)
            is_buffered : True/False for cursor's buffered option (default = True)
        OUTPUT : 
            MySQLConnectionAbstract : mysql connection object
            MySQLConnectionAbstract.cursor : cursor
    """
    db_connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

    cursor = db_connection.cursor(buffered=is_buffered)

    return db_connection, cursor


def execute_sql(cursor: mysql.connector.connection.MySQLConnectionAbstract.cursor, sql: str) -> List | Any:
    """
        EXECUTE SQL AND PRINT RESULT
        INPUT: 
            cursor : mysql.connector.connection.MySQLConnectionAbstract.cursor
        OUTPUT : 
            List[RowType | Dict[str, RowItemType]] | Any: # type: ignore
    """
    cursor.execute(sql)

    result = cursor.fetchall()
    for row in result:
        print(row)

    return result

def execute_sql_list(
    cursor: MySQLCursor,
    sql: Union[str, List[str]]
) -> Union[List[tuple], None]:
    """
    Execute single or multiple SQL statements and print results if applicable.

    Args:
        cursor (MySQLCursor): Cursor from a MySQL connection
        sql (str or List[str]): A single SQL statement or a list of statements

    Returns:
        List[tuple] if SELECT query, otherwise None
    """
    # 여러 개의 SQL문을 리스트로 처리
    if isinstance(sql, list):
        for query in sql:
            cursor.execute(query)
            if query.strip().lower().startswith("select"):
                result = cursor.fetchall()
                for row in result:
                    print(row)
        return None
    else:
        cursor.execute(sql)
        if sql.strip().lower().startswith("select"):
            result = cursor.fetchall()
            for row in result:
                print(row)
            return result
        return None



def close_conn_and_cursor(connection: mysql.connector.connection.MySQLConnectionAbstract, cursor: mysql.connector.connection.MySQLConnectionAbstract.cursor) -> None:
    """
        CLOSE DATABASE CONNECTION ADN CURSOR
        INPUT: 
            connection: mysql.connector.connection.MySQLConnectionAbstract
            cursor : mysql.connector.connection.MySQLConnectionAbstract.cursor
        OUTPUT : 
            None
    """
    
    cursor.close()
    connection.close()
    print("DATABASE CONNECTION AND CURSOR CLOSED")




print(f"get_connection_and_cursor.__doc__ :\n{get_connection_and_cursor.__doc__}")
# help(get_connection_and_cursor)
print(pydoc.render_doc(get_connection_and_cursor))


# remote = get_connection(host, user, password)

# r_cursor = remote.cursor(buffered=True)

# close_conn_and_cursor(remote, r_cursor)

# remote_conn, cursor = get_connection_and_cursor(host, user, password)


# execute_sql(cursor, "SELECT * FROM crime_status")

# close_conn_and_cursor(remote_conn, cursor)