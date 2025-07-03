import pandas as pd
from utils.db_functions import get_connection, execute_sql


def pd_to_db(host, user, password, database, table_name:str, raw_file_path:str = "./DATA/서울시 동물병원 인허가 정보.csv", ):
    df = pd.read_csv(raw_file_path, encoding='cp949')

    print(df)

    db_connection = get_connection(host, user, password, database)

    cursor = db_connection.cursor(buffered=True)

    con_check_sql = f"""
SELECT 
    COLUMN_NAME AS field_name,
    COLUMN_TYPE AS type,
    IS_NULLABLE,
    COLUMN_DEFAULT,
    COLUMN_COMMENT AS description
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'eda' AND TABLE_NAME = '{table_name}'
ORDER BY ORDINAL_POSITION;
"""

    schema = execute_sql(cursor, con_check_sql)

# 한글 컬럼 → 영문 필드명 매핑
    desc_to_field = {desc: field for field, _, _, _, desc in schema}
    rename_dict = {col: desc_to_field[col.strip()] for col in df.columns if col.strip() in desc_to_field}
    df.rename(columns=rename_dict, inplace=True)

    insert_statements = []

    for _, row in df.iterrows():
        non_null_fields = row.dropna()
        columns_part = ', '.join(non_null_fields.index)
        values_part = ', '.join(
        f"'{str(v).replace('\'', '\'\'')}'" if isinstance(v, str) else str(int(v)) if isinstance(v, float) and v.is_integer() else str(v)
        for v in non_null_fields.values
    )
        insert_sql = f"INSERT INTO {table_name} ({columns_part}) VALUES ({values_part});"
        insert_statements.append(insert_sql)

# 예시로 상위 3개만 출력
    for stmt in insert_statements[:3]:
        print(stmt)

    for stmt in insert_statements:
        execute_sql(cursor, stmt)

    db_connection.commit()
    return db_connection,cursor