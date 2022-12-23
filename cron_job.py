import sqlite3

def update_expired_dates():
    '''
    it updates requester status to expired when it is not flexible timing and time is expired
    '''
    conn = sqlite3.connect("C:/NxtWave_Assessment/Let's_Ride/app/blog.db")
    query = """UPDATE transport_requests 
               SET status = 'retired' 
               WHERE date_time < DATETIME() 
               AND 
               DATETIME(date_time) != DATETIME('0001-01-01 00:00:00.000000')"""
    conn.execute(query)
    conn.commit()
    conn.close()
    
