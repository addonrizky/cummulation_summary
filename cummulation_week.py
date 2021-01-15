import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='178.128.208.156',
                                         database='saham',
                                         user='rizkyaddon',
                                         password='Jakarta123!')

    sql_select_Query = "select * from list_saham"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in saham is: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    for row in records:
        kode_saham = row[1] + ""
        netval_1day_ago = row[47]
        netval_2day_ago = row[48]
        netval_3day_ago = row[49]
        netval_4day_ago = row[50]
        netval_5day_ago = row[51]
        netval_6day_ago = row[52]
        netval_7day_ago = row[53]
        netval_8day_ago = row[54]
        netval_9day_ago = row[55]
        netval_10day_ago = row[56]
        netval_11day_ago = row[57]
        netval_12day_ago = row[58]
        netval_13day_ago = row[59]
        netval_14day_ago = row[60]
        netval_15day_ago = row[61]
        netval_16day_ago = row[62]
        netval_17day_ago = row[63]
        netval_18day_ago = row[64]
        netval_19day_ago = row[65]
        netval_20day_ago = row[66]

        foreign_netval_total5 = netval_1day_ago + netval_2day_ago + netval_3day_ago + netval_4day_ago + netval_5day_ago

        foreign_netval_total10 = netval_1day_ago + netval_2day_ago + netval_3day_ago + netval_4day_ago + netval_5day_ago + netval_6day_ago + netval_7day_ago + netval_8day_ago + netval_9day_ago + netval_10day_ago

        foreign_netval_total15 = netval_1day_ago + netval_2day_ago + netval_3day_ago + netval_4day_ago + netval_5day_ago + netval_6day_ago + netval_7day_ago + netval_8day_ago + netval_9day_ago + netval_10day_ago + netval_11day_ago + netval_12day_ago + netval_13day_ago + netval_14day_ago + netval_15day_ago
        
        foreign_netval_total = netval_1day_ago + netval_2day_ago + netval_3day_ago + netval_4day_ago + netval_5day_ago + netval_6day_ago + netval_7day_ago + netval_8day_ago + netval_9day_ago + netval_10day_ago + netval_11day_ago + netval_12day_ago + netval_13day_ago + netval_14day_ago + netval_15day_ago + netval_16day_ago + netval_17day_ago + netval_18day_ago + netval_19day_ago + netval_20day_ago
       
        sql = "UPDATE list_saham SET foreign_netval_total5 = '"+str(foreign_netval_total5)+"', foreign_netval_total10 = '"+str(foreign_netval_total10)+"', foreign_netval_total15 = '"+str(foreign_netval_total15)+"', foreign_netval_total = '"+str(foreign_netval_total)+"' WHERE kode_saham = '"+ kode_saham +"'"
#
        print(sql)
        cursor.execute(sql)
        connection.commit()
        #print(mycursor.rowcount, "record(s) affected")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")