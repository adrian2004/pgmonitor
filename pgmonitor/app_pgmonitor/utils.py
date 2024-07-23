from django.db import connections
from . import constants

base_1 = constants.BASE_1

#BASE 1
def get_usuarios():
    with connections['default'].cursor() as cursor:
        query = """
        SELECT pid, usename, datname, to_char(backend_start, 'DD-MM-YYYY HH24:MI:SS')
        FROM pg_stat_activity
        WHERE datname = %s;
        """
        cursor.execute(query, [base_1])
        result = cursor.fetchall()
    return result

def get_usuarios_total():
    with connections['default'].cursor() as cursor:
        query = """
        SELECT count(*) FROM pg_stat_activity WHERE datname = %s;
        """
        cursor.execute(query, [base_1])
        result = cursor.fetchone()
    return result[0] if result else 0

def get_base_tamanho():
    with connections['default'].cursor() as cursor:
        query = """
        SELECT pg_size_pretty(pg_database_size(t1.datname)) FROM pg_database t1 WHERE t1.datname = %s;
        """
        cursor.execute(query, [base_1])
        result = cursor.fetchone()
    return result[0] if result else 0

#Colocar mais bases ajustando o connections['CONEXÃO']