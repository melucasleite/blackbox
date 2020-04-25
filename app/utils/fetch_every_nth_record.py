# encoding = utf-8


def fetch_every_nth_record(table, n, db, where=None):
    query = create_query_every_nth_record(table, n, where)
    records = db_perform_query(db, query)
    return records


def create_query_every_nth_record(table: str, n: int, where: str):
    query = create_query_every_nth_record_MYSQL(table, n, where)
    return query


def db_perform_query(db, query: str):
    result = db_perform_query_SQLalchemy(db, query)
    return result


def create_query_every_nth_record_MYSQL(table: str, n: int, where: str) -> str:
    if where:
        where = " " + where
    else:
        where = ""
    query = f"""
    SELECT {table}.* FROM {table} INNER JOIN (
        SELECT id FROM (
            SELECT @row:=@row+1 AS rownum, id FROM (
                SELECT id FROM {table}{where} ORDER BY id desc 
            ) AS sorted
        ) as ranked WHERE rownum mod {n} = 0
    ) AS subset ON subset.id = {table}.id LIMIT 50
    """
    return query


def db_perform_query_SQLalchemy(db, query):
    query = " ".join(query.split())
    db.engine.execute("set @row:=-1;")
    result = db.engine.execute(query)
    return result
