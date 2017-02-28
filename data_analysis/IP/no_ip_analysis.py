# encoding: utf-8

"""
分析服务器whois.no-ip.com的IP情况
1. 长期关闭
2. 长期开放
3. 不稳定IP，有时开放有时关闭

@作者：程亚楠
@创建时间：2017.2.28

"""

from db_manage import get_col


def analysis_no_ip():
    """
    获取各类状态的ip列表和数量
    :returns
        long_term_up_ips，长期开放ip
        instability_ips，不稳定ip
    """

    # 得到whois.no-ip.com的所有解析IP
    col = get_col('com_svr')
    ips = col.find({'domain': 'whois.no-ip.com'},{'_id': 0, 'ips': 1})
    ips = ips[0]['ips']

    # 获取所有ip的状态扫描结果
    down_ips = set()
    up_ips = set()
    col = get_col('ip_scan_result1')
    for ip in ips:
        scan_info = col.find({'ip': ip})
        for i in scan_info:
            if i['state'] == 'down':
                down_ips.add(i['ip'])
            else:
                up_ips.add(i['ip'])

    # ip各状态统计
    instability_ips = list(down_ips & up_ips)  # 不稳定ip集合
    print instability_ips
    print len(instability_ips)

    long_term_down_ips = list(down_ips - set(instability_ips))  #  长期关闭ip集合
    print long_term_down_ips
    print len(long_term_down_ips)

    long_term_up_ips = list(up_ips - set(instability_ips))   # 长期开放ip集合
    print long_term_up_ips
    print len(long_term_up_ips)

    return long_term_up_ips, instability_ips


def ip_state_details(ips):

    col = get_col('ip_scan_result1')

    for ip in ips:
        scan_info = col.find({'ip':ip})
        for i in scan_info:
            print i


if __name__ == '__main__':

    long_term_up_ips,instability_ips = analysis_no_ip()
    ip_state_details(long_term_up_ips)