# encoding:utf-8

from mysqldb import MySQL


def registrar_srvs(end_tb):
    """
    获取原始数据
    """
    mysql = MySQL(HOST='172.29.152.249', USER='root', PASSWORD='platform')
    mysql.connect()
    mysql.select_db('domain_whois')

    fp = open('result3.txt','r')
    srvs = fp.readlines()
    for srv in srvs:
        srv = srv.strip()
        print srv
        srv_domains = []
        d_c = 0
        for table_num in xrange(1, end_tb):
            print 'table: ', str(table_num)
            sql = """SELECT domain FROM domain_whois_{n} WHERE  sec_whois_server='{srv}' AND tld='com' LIMIT 10 """.format(n=table_num,srv=srv)
            domains = mysql.execute_sql(sql)[0]
            if not domains:
                continue
            for d in domains[0]:
                # print d
                srv_domains.append(d)
                d_c += 1

            if d_c >= 10:
                break
        save_data(srv_domains)

    fp.close()
    mysql.disconnect()


def save_data(domains):
    fp = open('srv_domains3.txt','a')
    for i in domains:
        fp.write(i+'\n')
    fp.close()


if __name__ == '__main__':
    registrar_srvs(end_tb=101)  # 从数据库中获取所有注册商名称
