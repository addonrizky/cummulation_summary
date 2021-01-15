import scrapy
from scrapy.http import FormRequest
import mysql.connector
from mysql.connector import errorcode
from constant_emiten_url import start_urls

class QuotesSpider(scrapy.Spider):
    name = "cummulationlcrawler"
    start_urls = start_urls

    def parse(self, response):
        #retrieve emiten code
        emiten_url = response.request.url
        kode_saham = emiten_url[77:81]
        print(kode_saham)


        whole_table = response.css("table.table-summary > tfoot > tr > th > div > span.ml5")
        foreign_netval = whole_table[1].css("::text").get()[10:]
        foreign_netval = self.convert_string_amount(foreign_netval)

        #save to db
        connection = mysql.connector.connect(
            host='178.128.208.156',
            database='saham',
            user='rizkyaddon',
            password='Jakarta123!'
        )

        print(foreign_netval)

        cursor = connection.cursor()
        sql = "UPDATE list_saham SET foreign_netval_current = '"+str(foreign_netval)+"' WHERE kode_saham = '"+ kode_saham +"'"

        cursor.execute(sql)
        connection.commit()
        print("done")


    def convert_string_amount(self, amount_string):
        number = 0
        metric = 0
        multiplier = 1

        amount_splitted = amount_string.split(" ")

        if len(amount_splitted) > 0:
            number = float(amount_splitted[0].replace(",", ""))
        if len(amount_splitted) > 1:
            metric = amount_splitted[1]

        if metric == "M" :
            multiplier = float(1000000)
        if metric == "B" : 
            multiplier = float(1000000000)
        if metric == "T" : 
            multiplier = float(1000000000000)

        return number * multiplier
    
    #def __init__(self, **kwargs):
    #    self.cnx = self.mysql_connect()
#
    #def start_requests(self):
    #    conf = {
    #        'host': '178.128.208.156',
    #        'user': 'rizkyaddon',
    #        'password': 'Jakarta123!',
    #        'database': 'saham',
    #        'raise_on_warnings': True
    #    }
#
    #    cursor = self.cnx.cursor()
#
    #    cursor.execute("SELECT * from list_saham")
    #    links = cursor.fetchall()
#
    #    url = "https://www.indopremier.com/programer_script/process_login.php?type=regular&kanal=mainlogin&login_from=newsPagesSearchphp?q="
    #    boday = "frmLoginId=RIDR89&frmPassword=ApGdlGm2&frmCaptchaLogin=&frmCaptchaLoginRandomId=214"
    #    yield scrapy.Request(
    #        url, 
    #        body=boday, 
    #        method='POST', 
    #        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    #    )
    #    
#
    #def after_pin(self, response):
    #    url = "https://www.indopremier.com/ipotmember/transview.php?page=myportfolio"
    #    boday = "type=stockportfolio&custcode=R10000110019&_=1599050601632"
#
    #    yield scrapy.Request(
    #        url, 
    #        method='GET',
    #        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    #        callback=self.after_math
    #    )
#
    #def after_math(self, response):
    #    cek = response.css("div.mt15::text")
    #    print(cek.get())
#
    #def mysql_connect(self):
    #    try:
    #        return mysql.connector.connect(**self.conf)
    #    except mysql.connector.Error as err:
    #        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #            print("Something is wrong with your user name or password")
    #        elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #            print("Database does not exist")
    #        else:
    #            print(err)