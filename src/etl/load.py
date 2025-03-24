from utils.logger import init_logger
from config import settings
import mysql.connector
from mysql.connector import Error

logger = init_logger(__name__)

def load(data_to_insert):

    try:
        with mysql.connector.connect(**settings.DB_CONFIG, connection_timeout=30) as db:

            cursor = db.cursor()
            
            cursor.execute("""
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_SCHEMA = DATABASE()
            AND TABLE_NAME = 'wp_cqc_data'
            AND COLUMN_NAME NOT IN ('id', 'last_updated');
            """)
            
            column_names = [row[0] for row in cursor]


            insert_query = f""" 
            INSERT INTO wp_cqc_data ({', '.join(column_names)})
            VALUES ({', '.join('%(' + col + ')s' for col in column_names)})
            """

            # rows_to_insert = []
            # for item in transformation:
                # row = tuple(item[col] for col in columns)
                # rows_to_insert.append(row)
           
            cursor.executemany(insert_query, data_to_insert)

            db.commit()

            logger.info(f"Inserted {cursor.rowcount} rows into wp_cqc_data")

    except Error as e:
        logger.error(f"MySQL Error: {e}")
        try:
            db.rollback()
        except:
            logger.warning("Rollback failed or no active transaction")




