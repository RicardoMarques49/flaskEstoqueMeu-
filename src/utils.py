from pathlib import Path

from flask import Flask




def existe_esquema(app: Flask)-> bool:
# Se estivéssmos com um SGBD, poderíamos consultar os metadados para ver
# se o esquema do banco existe, com algo como (mariaDB)
# SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '<nome>'
# No caso do SQLite, vamos apenas verificar se existe ou não o arquivo no
# sistema de arquivos
    nome_do_arquivo = Path(app.instance_path) / app.config.get('SQLITE_DB')
    if nome_do_arquivo.is_file():
        return True




        return False






