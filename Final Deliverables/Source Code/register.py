import ibm_db
import ibm_db_dbi

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32328;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=kvl02892;PWD=mLEEax4Ly59qV8zO",'','')



print(conn) 
print("yyyyyyyyysssssssssssssssss") 

sql="SELECT * FROM car"
stmt = ibm_db.exec_immediate(conn, sql)
dic=ibm_db.fetch_assoc(stmt)
while dic != False:
    #print("the name is :",dic["cname"])
    print("the model is :",dic)
    dic=ibm_db.fetch_assoc(stmt)