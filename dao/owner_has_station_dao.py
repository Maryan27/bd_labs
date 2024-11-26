from models.owner_has_station import OwnerHasStation
from models.solar_station import SolarStation

class OwnerHasStationDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_owners_stations(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM owner_has_station")
        owners_stations = cur.fetchall()
        cur.close()
        return [OwnerHasStation(owner_id=row[0], station_id=row[1]) for row in owners_stations]

    def insert_owner_station(self, owner_station):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO owner_has_station (owner_id, station_id) VALUES (%s, %s)", 
                    (owner_station['owner_id'], owner_station['station_id']))
        self.mysql.connection.commit()
        cur.close()

    def delete_owner_station(self, owner_id, station_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM owner_has_station WHERE owner_id = %s AND station_id = %s", (owner_id, station_id))
        self.mysql.connection.commit()
        cur.close()

    def get_stations_for_owner(self, owner_id):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT 
                o.id AS owner_id, o.name AS owner_name, o.email AS owner_email,
                s.id AS station_id, s.household_id, s.installation_date
            FROM owner o
            JOIN owner_has_station ohs ON o.id = ohs.owner_id
            JOIN solar_station s ON ohs.station_id = s.id
            WHERE o.id = %s
        """, (owner_id,))
        rows = cur.fetchall()
        cur.close()

        result = []
        for row in rows:
            result.append({
                "owner": {
                    "id": row[0],
                    "name": row[1],
                    "email": row[2]
                },
                "solar_station": {
                    "id": row[3],
                    "household_id": row[4],
                    "installation_date": row[5].isoformat() if row[5] else None
                }
            })
        return result

          # Виклик збереженої процедури insert_owner_station_link
    def call_insert_owner_station_procedure(self, owner_name, owner_email, installation_date):
        cur = self.mysql.connection.cursor()
        cur.callproc('insert_owner_station_link', [owner_name, owner_email, installation_date])
        self.mysql.connection.commit()
        cur.close()