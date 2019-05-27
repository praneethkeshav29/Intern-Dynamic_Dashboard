from sqlalchemy import create_engine
import base64

db_uri = 'mysql://root:@localhost/flat'
engine = create_engine(db_uri, pool_pre_ping=True)


def urlproducts():
    l = []
    sqlq = 'SELECT name FROM role;'
    result = engine.execute(sqlq)
    for _r in result:
        if _r[0] != "superuser":
            l.append(_r[0])
    return l


def getavailableproducts():
    l = []
    sqlq = 'SELECT name FROM role;'
    result = engine.execute(sqlq)
    for _r in result:
        if _r[0] != "superuser":
            l.append(_r[0])
    length = len(l)
    for i in range(length):
        print(l[i])
        s="SELECT count(*) FROM information_schema.TABLES WHERE(TABLE_SCHEMA='flat') AND(TABLE_NAME='"+l[i]+"sources');"
        print(s)
        result = engine.execute(s)
        re=[]
        for r in result:
            if r[0] != "superuser":
                re.append(r[0])
        print(re)
        if re[0]==0:
            s = "CREATE TABLE `" + l[
                i] + "sources` (`id` int(11) NOT NULL,`webapi` varchar(255) NOT NULL, `webapiurl` varchar(255) DEFAULT NULL,`webuser` varchar(255) DEFAULT NULL,`webpass` varchar(255) DEFAULT NULL,`mysql` varchar(255) DEFAULT NULL, `mysqlurl` varchar(255) DEFAULT NULL,  `mysqldb` varchar(255) DEFAULT NULL,  `mysqluser` varchar(255) DEFAULT NULL,  `mysqlpass` varchar(255) DEFAULT NULL, `sqlserver` varchar(255) DEFAULT NULL,  `sqlserverurl` varchar(255) DEFAULT NULL,  `sqlserverdb` varchar(255) DEFAULT NULL,  `sqlserveruser` varchar(255) DEFAULT NULL,  `sqlserverpass` varchar(255) DEFAULT NULL,  PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=latin1"
            result = engine.execute(s)
            print("table created!")
        else:
            print("table exists!")


def getsourceurl(id,num):
    curr = str(id)
    urls=[]
    table = gettable(num)
    if not table:
        return urls
    sql = 'SELECT webapiurl,webuser, webpass FROM '+table+' where id='+curr+';'
    result = engine.execute(sql)
    urls = []
    for _r in result:
        for i in range(0, 3):
            if _r[i] is not None:
                urls.append(_r[i])
    urls = list(filter(None, urls))
    if urls:
        urls[0]=urls[0][2:-1]
        urls[0]=urls[0].encode()
        urls[0]=base64.b64decode(urls[0]).decode('utf-8')
    return urls


def getadminrole(id):
    sqlq = 'SELECT name FROM role where id in(select role_id from roles_users where user_id= ' + str(id) + ');'
    result = engine.execute(sqlq)
    l=[]
    for _r in result:
        if _r[0] == "superuser":
            l.append(_r[0])
    return l


def getroles(id):
    urls = []
    l = []
    curr = str(id)
    sqlq = 'SELECT name FROM role where id in(select role_id from roles_users where user_id= ' + str(id) + ');'
    result = engine.execute(sqlq)
    for _r in result:
        # print(_r)
        if _r[0] != "superuser":
            l.append(_r[0])
    return l


def gettable(num):
    l=urlproducts()
    res=[]
    for i in range(len(l)):
        r = l[i]
        r+='sources'
        res.append(r)
    return res[num]


def geturls(id,num):
    curr = str(id)
    table = gettable(num)
    sql = 'SELECT webapi,mysql, sqlserver FROM '+table +' where id=' + curr + ';'
    result = engine.execute(sql)
    urls = []
    for _r in result:
        for i in range(0, 3):
            if _r[i] is not None:
                urls.append(_r[i])
    urls = list(filter(None, urls))
    return urls


def checkid(id, num):
    table = gettable(num)
    idd = []
    sql = 'SELECT id FROM '+table+' where id=' + id + ';'
    result = engine.execute(sql)
    for _r in result:
        idd.append(_r[0])
    return idd


def createidd(id,num):
    table = gettable(num)
    sql = 'insert into '+ table+'(id) values(' + id + ');'
    engine.execute(sql)


def upwebapi(id,form,num):
    table = gettable(num)
    webapiurl = form['webapiurl']
    webapiurl = str(base64.b64encode(webapiurl.encode('utf-8')))
    webuser = form['webuser']
    webpass = form['webpass']
    sql = 'update '+table+' set webapi = "webapi",webapiurl ="' + webapiurl + '",webuser = "' + webuser + '",webpass = "' + webpass + '" where id =' + id + ';'
    engine.execute(sql)


def upmysql(id,form,num):
    table = gettable(num)
    mysqlurl = form['mysqlurl']
    mysqldb = form['mysqldb']
    mysqluser = form['mysqluser']
    # mysqlpass = hashlib.md5(form['mysqlpass'].encode()).hexdigest()
    mysqlpass =form['mysqlpass']
    mysqlurl = str(base64.b64encode(mysqlurl.encode('utf-8')))
    sql = 'update '+table+' set mysql = "mysql",mysqlurl="' + mysqlurl + '",mysqldb = "' + mysqldb + '",mysqluser = "' + mysqluser + '",mysqlpass = "' + mysqlpass + '" where id =' + id + ';'
    engine.execute(sql)


def upsqlserver(id,form,num):
    table = gettable(num)
    sqlurl = form['sqlserverurl']
    sqldb = form['sqlserverdb']
    sqluser =form['sqlserveruser']
    sqlpass = form['sqlserverpass']
    sqlurl = str(base64.b64encode(sqlurl.encode('utf-8')))
    sql = 'update '+table+' set sqlserver = "sqlserver",sqlserverurl="' + sqlurl + '",sqlserverdb = "' + sqldb + '",sqlserveruser = "' + sqluser + '",sqlserverpass = "' + sqlpass + '" where id =' + id + ';'
    engine.execute(sql)

