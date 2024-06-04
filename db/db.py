import logging
import sqlite3
from contextlib import contextmanager

connection = sqlite3.connect('db/doctor_office_db.db', check_same_thread=False)
class DBService:

    @classmethod
    def update(cls, sql, qryparams):
        cursor = connection.cursor()
        try:
            logging.debug(u'Executing sql: [{0}]'.format(sql.strip()))
            cursor.execute(sql, qryparams)
        finally:
            cursor.close()
            connection.commit()

    @classmethod
    def query(cls, sql, qryparams):
        cursor = connection.cursor()
        try:
            logging.debug(u'Executing sql: [{0}]'.format(sql.strip()))
            cursor.execute(sql, qryparams)

            return cursor.fetchall()
        finally:
            cursor.close()
            connection.commit()

    @classmethod
    def query_single(cls, sql, qryparams):
        cursor = connection.cursor()
        try:
            logging.debug(u'Executing sql: [{0}]'.format(sql.strip()))
            cursor.execute(sql, qryparams)

            return cursor.fetchone()
        finally:
            cursor.close()
            connection.commit()

