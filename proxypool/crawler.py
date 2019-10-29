from .utils import get_page
from pyquery import PyQuery as pq


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self):
        for page in range(1, 5):
            start_url = 'http://www.66ip.cn/{}.html'.format(page)
            html = get_page(start_url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text().strip()
                    port = tr.find('td:nth-child(2)').text().strip()
                    yield ':'.join([ip, port])

    def crawl_ip3366(self):
        for page in range(1, 4):
            start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
            html = get_page(start_url)
            if html:
                doc = pq(html)
                trs = doc('tbody tr').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text().strip()
                    port = tr.find('td:nth-child(2)').text().strip()
                    yield ':'.join([ip, port])

    def crawl_kuaidaili(self):
        for page in range(1, 2):
            start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
            html = get_page(start_url)
            if html:
                doc = pq(html)
                trs = doc('tbody tr').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text().strip()
                    port = tr.find('td:nth-child(2)').text().strip()
                    yield ':'.join([ip, port])

    def crawl_xicidaili(self):
        for page in range(1, 3):
            start_url = 'http://www.xicidaili.com/nn/{}'.format(page)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRjYzc5MmM1MTBiMDMzYTUzNTZjNzA4NjBhNWRjZjliBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUp6S2tXT3g5a0FCT01ndzlmWWZqRVJNek1WanRuUDBCbTJUN21GMTBKd3M9BjsARg%3D%3D--2a69429cb2115c6a0cc9a86e0ebe2800c0d471b3',
                'Host': 'www.xicidaili.com',
                'Referer': 'http://www.xicidaili.com/nn/',
                'Upgrade-Insecure-Requests': '1',
            }
            html = get_page(start_url, options=headers)
            if html:
                doc = pq(html)
                trs = doc('table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(2)').text().strip()
                    port = tr.find('td:nth-child(3)').text().strip()
                    yield ':'.join([ip, port])

    def crawl_iphai(self):
        urls = ['http://www.iphai.com/free/ng', 'http://www.iphai.com/free/wg']
        for start_url in urls:
            html = get_page(start_url)
            if html:
                doc = pq(html)
                trs = doc('table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text().strip()
                    port = tr.find('td:nth-child(2)').text().strip()
                    yield ':'.join([ip, port])

    def crawl_data5u(self):
        start_url = 'http://www.data5u.com'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=47AA0C887112A2D83EE040405F837A86',
            'Host': 'www.data5u.com',
            'Upgrade-Insecure-Requests': '1'
        }
        html = get_page(start_url, options=headers)
        if html:
            doc = pq(html)
            uls = doc('.wlist ul ul:gt(0)').items()
            for ul in uls:
                if ul.find('span:nth-child(3)').text().strip() != '高匿':
                    continue
                ip = ul.find('span:nth-child(1)').text().strip()
                port = ul.find('span:nth-child(2)').text().strip()
                yield ':'.join([ip, port])
