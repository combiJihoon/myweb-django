import sys
import logging
import mysql.connector
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
port = os.environ.get("DB_PORT")

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Command(BaseCommand):
    help = "Creates the initial database"

    def handle(self, *args, **options):
        print("Starting db creation")
        try:
            db = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                db="mysql",
                connect_timeout=5,
            )
            c = db.cursor()
            print("connected to db server")
            c.execute(
                f"""CREATE DATABASE {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"""
            )
            c.execute(f"""GRANT ALL ON {db_name}.* TO {user}@'%'""")
            c.close()
            print("closed db connection")
        except mysql.connector.Error as err:
            logger.error("Something went wrong: {}".format(err))
            sys.exit()
