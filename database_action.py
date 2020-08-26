# import psycopg2

# def RasaDatabase(name,address,number):
#     conn = psycopg2.connect(
#         database="Rasa", user = "postgres", password = "post123", host = "localhost", port = "5432"
#         ) 
#     cur = conn.cursor()
#     sql_table = """CREATE TABLE corona_table (
#                    NAME TEXT NOT NULL,
#                    ADDRESS TEXT NOT NULL,
#                    NUMBER TEXT NOT NULL);"""
#     sql_insert = f""" INSERT INTO corona_table (NAME,ADDRESS,NUMBER) VALUES ({name},{address},{number});"""
#     cur.execute(sql_table)
#     cur.execute(sql_insert)
#     print("Complete")
#     conn.commit()
#     conn.close()

# if __name__=='__main__':
#     RasaDatabase("Madan","damak","98134786")