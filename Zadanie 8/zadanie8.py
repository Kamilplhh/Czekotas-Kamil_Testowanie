import os 
import sqlite3 

 

def create_database(): 

    conn = sqlite3.connect("boisko.db") 

    cursor = conn.cursor() 
 

    cursor.execute("""CREATE TABLE KLUBY (nazwa text,trener text, kraj text,liczba_pilkarzy int,najlepszy_zawodnik text, sponsor_glowny text)  """) 
  

    cursor.execute("INSERT INTO KLUBY VALUES " "('Baza 44', 'Filip Czoch', 'Polska',11, 'Kcamil Grzegorzec', 'GBS')") 
    cursor.execute("INSERT INTO KLUBY VALUES " "('POLSKAA', 'Paulo Sousa', 'Portugalia',52, 'Robert Lewandowski', 'AFTEREK')") 

    conn.commit() 

def select_all(trener): 

    conn = sqlite3.connect("boisko.db") 

    cursor = conn.cursor() 

    sql = "SELECT * FROM KLUBY WHERE  trener=?" 

    cursor.execute(sql, [(trener)]) 

    result = cursor.fetchall() 

    cursor.close() 

    conn.close() 

    return result 

def update_all(liczba_pilkarzy, kraj): 

    conn = sqlite3.connect("boisko.db") 

    cursor = conn.cursor() 

    sql = "UPDATE KLUBY SET liczba_pilkarzy=? WHERE kraj=?" 

    cursor.execute(sql, [(liczba_pilkarzy),(kraj)]) 

    result = cursor.fetchall() 

    conn.commit()

    cursor.close() 

    conn.close() 

    return result 
    
def delete_all(trener): 

    conn = sqlite3.connect("boisko.db") 

    cursor = conn.cursor() 

    sql = "DELETE FROM KLUBY WHERE trener=?" 

    cursor.execute(sql, [(trener)]) 

    result = cursor.fetchall() 

    conn.commit()

    cursor.close() 

    conn.close() 

    return result 

if __name__ == '__main__': 

 

    if not os.path.exists("boisko.db"): 

        create_database() 

    #print(select_all('Filip Czoch')) 
    #print(update_all( 14,'Polska')) 
    #print(delete_all('Paulo Sousa')) 





