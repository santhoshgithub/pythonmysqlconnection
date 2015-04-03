#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
con1= mdb.connect('localhost', 'root','root','ravi');
with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM emp")
    for i in range(cur.rowcount):
        
       row = cur.fetchone()
       print row[0], row[1]


with con1:

    cur = con1.cursor()
    cur.execute("SELECT * FROM site_status")
    for i in range(cur.rowcount):
        
       row = cur.fetchone()
       print row[0], row[1]











#try:
#    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
#    cur1 = con.cursor()
#    cur1.execute("select * from emp") 
#    ver1 = cur1.fetchall()
#    print "Employee Details"
#    for i in ver1:
#        print ("===================================================")
#        print "Emp.id=%d||Emp.Name=%s" % i
#        raw_input("Press Enter button ......... to get next employee list")
        

#    print "Sorry it is over and no list in database"
#    print "bye"

#except mdb.Error, e:
  
#    print "Error %d: %s" % (e.args[0],e.args[1])
#    sys.exit(1)
    
#finally:    
#        
#    if con:    
#        con.close()


