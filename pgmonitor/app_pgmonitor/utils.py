from django.db import connections
from .constants import bases

functions = {}

for i, base in enumerate(bases):
    def get_usuarios(base=base, i=i):
        with connections[f'db_{i}'].cursor() as cursor:
            query = """
            SELECT pid, usename, datname, to_char(backend_start, 'DD-MM-YYYY HH24:MI:SS')
            FROM pg_stat_activity
            WHERE datname = %s;
            """
            cursor.execute(query, [base])
            result = cursor.fetchall()
        return result
    
    def get_usuarios_total(base=base, i=i):
        with connections[f'db_{i}'].cursor() as cursor:
            query = """
            SELECT count(*) FROM pg_stat_activity WHERE datname = %s;
            """
            cursor.execute(query, [base])
            result = cursor.fetchone()
        return result[0] if result else 0

    def get_base_tamanho_tabelas(base=base, i=i):
        with connections[f'db_{i}'].cursor() as cursor:
            query = """
            SELECT esquema, tabela,
        pg_size_pretty(pg_relation_size(esq_tab)) AS tamanho,
        pg_size_pretty(pg_total_relation_size(esq_tab)) AS tamanho_total
    FROM (SELECT tablename AS tabela,
                schemaname AS esquema,
                schemaname||'.'||tablename AS esq_tab
            FROM pg_catalog.pg_tables
            WHERE schemaname NOT
                IN ('pg_catalog', 'information_schema', 'pg_toast') ) AS x
    ORDER BY pg_total_relation_size(esq_tab) DESC;
            """
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def get_base_tamanho(base=base, i=i):
        with connections[f'db_{i}'].cursor() as cursor:
            query = """
            SELECT pg_size_pretty(pg_database_size(t1.datname)) FROM pg_database t1 WHERE t1.datname = %s;
            """
            cursor.execute(query, [base])
            result = cursor.fetchone()
        return result[0] if result else 0
    
    functions[f'get_usuarios_{i}'] = get_usuarios
    functions[f'get_usuarios_total_{i}'] = get_usuarios_total
    functions[f'get_base_tamanho_tabelas_{i}'] = get_base_tamanho_tabelas
    functions[f'get_base_tamanho_{i}'] = get_base_tamanho
    
for i in range(len(bases)):
    connections[f'db_{i}'].close()