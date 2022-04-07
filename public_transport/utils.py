import psycopg2


def stops_by_distance_query(long, lat, relevant_distance):
    """
    Function returning up to 5 closest stops based on given coordinates and radius

    Args:
        data (dict): data received in request
        relevant_distance (int): acceptable distance from nearest stop measured in kilometers
    """
    
    conn = psycopg2.connect(user="postgres",
                            password="postgres",
                            host="db",
                            port="5432",
                            database="postgres")
    cur = conn.cursor()

    psql_query = f"""
    SELECT * 
    FROM public_transport_stop 
    WHERE (point(longitude,latitude) <@> point({long},{lat})) < {relevant_distance*0.62137}
    ORDER BY (point(longitude,latitude) <@> point({long},{lat}))
    ASC LIMIT 5"""
    
    cur.execute(psql_query)
    return cur.fetchall()

def get_distance_between_coords(long1, lat1, long2, lat2):
    conn = psycopg2.connect(user="postgres",
                            password="postgres",
                            host="db",
                            port="5432",
                            database="postgres")
    cur = conn.cursor()

    psql_query = f"""
    SELECT (point({long1},{lat1}) <@> point({long2},{lat2})) as distance"""
    
    cur.execute(psql_query)
    return cur.fetchall() 