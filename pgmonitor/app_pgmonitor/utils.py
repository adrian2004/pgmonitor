from django.db import connections

#BASE 1
def get_usuarios1():
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT pid,usename,datname,to_char(backend_start, 'DD-MM-YYYY HH24:MI:SS') FROM pg_stat_activity WHERE datname='monitored_db';")
        result = cursor.fetchall()
    return result

def get_usuarios_total1():
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT count(*) FROM pg_stat_activity WHERE datname='monitored_db';")
        result = cursor.fetchone()
    return result[0] if result else 0

def get_base_tamanho1():
    with connections['default'].cursor() as cursor:
        cursor.execute("select pg_size_pretty(pg_database_size(t1.datname)) from pg_database t1 where t1.datname = 'monitored_db';")
        result = cursor.fetchone()
    return result[0] if result else 0

#BASE 2
def get_usuarios2():
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT pid,usename,datname,to_char(backend_start, 'DD-MM-YYYY HH24:MI:SS') FROM pg_stat_activity WHERE datname='monitored_db2';")
        result = cursor.fetchall()
    return result

def get_usuarios_total2():
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT count(*) FROM pg_stat_activity WHERE datname='monitored_db2';")
        result = cursor.fetchone()
    return result[0] if result else 0

def get_base_tamanho2():
    with connections['default'].cursor() as cursor:
        cursor.execute("select pg_size_pretty(pg_database_size(t1.datname)) from pg_database t1 where t1.datname = 'monitored_db2';")
        result = cursor.fetchone()
    return result[0] if result else 0