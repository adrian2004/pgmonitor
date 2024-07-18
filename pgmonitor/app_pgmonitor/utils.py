from django.db import connection

def get_logged_in_users_count():
    with connection.cursor() as cursor:
        cursor.execute("SELECT pid,usename,datname,to_char(backend_start, 'DD-MM-YYYY HH24:MI:SS') FROM pg_stat_activity WHERE datname='monitored_db';")
        result = cursor.fetchall()
    return result

def get_usuarios_total():
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM pg_stat_activity WHERE datname='monitored_db';")
        result = cursor.fetchone()
    return result[0] if result else 0