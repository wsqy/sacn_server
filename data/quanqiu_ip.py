import os
import sys
import json

import ipaddr
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scanserver.settings")
import django
django.setup()

from scanBase.models import CountryInfo, IPSection, IPInfo

Headers = {
    "Host": "ipblock.chacuo.net",
    "Cookie": r"__cfduid=d098bd5f7d49c89a68e282b7f5f12e0b71516010314; bdshare_firstime=1516010317823; Hm_lvt_ef483ae9c0f4f800aefdf407e35a21b3=1516010317,1516010360; Hm_lpvt_ef483ae9c0f4f800aefdf407e35a21b3=1516012334",
    "User-Agent": r"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Accept_Language": "zh-CN,zh;q=0.9",
    "Accept_Encoding": r"gzip, deflate",
    "Connection": r"keep-alive",
    "Cache-Control": r"max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "http://ipblock.chacuo.net/view/c_",
}

def get_ip_section(code='', CountryInfo=None):
    """
    获取 国家二位码获取 所有的ip块
    """
    if CountryInfo:
        code = CountryInfo.letter2
    url = r'http://ipblock.chacuo.net/down/t_txt=c_{}'.format(code)
    Headers['Referer'] = r"http://ipblock.chacuo.net/view/c_{}".format(code)
    try:
        r = requests.get(url, headers=Headers)
        line_list = r.text.split('\n')
        for line in line_list:
            dump_ip_section_data(line, CountryInfo)
    except Exception as e:
        print("获取国家ip段异常: {}".format(e))


def dump_ip_section_data(ip_section=None, CountryInfo=None):
    try:
        _section = ip_section.split('\t')[2]
    except IndexError as e:
        print("数组越界异常: {}".format(e))
    # return
    else:
        ips = ipaddr.IPv4Network(_section)
        ip_section = IPSection()
        ip_section.country = CountryInfo
        ip_section.ip_section = _section
        ip_section.network = ips.network.compressed
        ip_section.netmask = ips.netmask.compressed
        ip_section.total = ips.numhosts
        try:
            ip_section.save()
        except Exception as e:
            print("ip块插入异常--{}".format(e))
            section_objects = IPSection.objects.filter(ip_section=_section)
            if section_objects.count() > 0 and not section_objects[0].deal_time:
                dump_ip_info(ips.iterhosts(), CountryInfo, section_objects[0])
        finally:
            dump_ip_info(ips.iterhosts(), CountryInfo, ip_section)

def dump_ip_info(ip_iterhosts=None, CountryInfo=None, ip_section=None):
    for ip in ip_iterhosts:
        try:
            IPInfo.objects.create(country=CountryInfo, iP_section=ip_section, ip=ip.compressed)
        except Exception as e:
            print("ip插入异常--{}".format(e))

if __name__ == '__main__':
    country_info = CountryInfo.objects.all()[:1]
    for item_country in country_info:
        get_ip_section('', item_country)
