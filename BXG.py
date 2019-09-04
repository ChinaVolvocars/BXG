#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json
import os

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Cookie': 'zg_did=%7B%22did%22%3A%20%2216c89bbd7ed17-0444739cbea2d6-7373e61-1fa400-16c89bbd7ee9f9%22%7D; bad_idb91bf240-868c-11e8-beff-b3a73470030e=4c174bd1-bd96-11e9-bc20-e71d1b8e4bb6; Hm_lvt_84c8fd20cad502132fed4406f9aa22e9=1565678885,1565703967,1566005969,1567557469; Hm_lvt_c11880ab74b1d3cd437ca5f41060fd17=1565678884,1565703967,1566005969,1567557469; nice_idb91bf240-868c-11e8-beff-b3a73470030e=383dc5e1-ceac-11e9-86a0-c515246118df; _uc_t_=375998%3B15136221475%3Bf1551265ff914b04bd821120ae47241b%3Bonline%3B1567643884149%3Bfalse; vssid=d49b188da6144c639b9025c0ec08a56f; Hm_lpvt_84c8fd20cad502132fed4406f9aa22e9=1567557486; Hm_lpvt_c11880ab74b1d3cd437ca5f41060fd17=1567557486; Hm_lvt_9f3069df154c115a922cad5be4cead79=1565703970,1566005986,1567557488; href=https%3A%2F%2Fxuexi.boxuegu.com%2F%3Fanchor%3Dcourse; accessId=b91bf240-868c-11e8-beff-b3a73470030e; qimo_seosource_b91bf240-868c-11e8-beff-b3a73470030e=%E7%AB%99%E5%86%85; qimo_seokeywords_b91bf240-868c-11e8-beff-b3a73470030e=; uniqueVisitorId=fc2cca18-5491-3eb3-91cd-b8e11579ffe8; studentId=d3ebcd38d13711e8a92200163e10f7de; Hm_lpvt_9f3069df154c115a922cad5be4cead79=1567558044; pageViewNum=9; zg_ea5fe1a9d6d94bfdbdd8a54e0ac598c2=%7B%22sid%22%3A%201567557468760%2C%22updated%22%3A%201567559311210%2C%22info%22%3A%201567557468764%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.boxuegu.com%2F%22%2C%22cuid%22%3A%20%22375998%22%7D; SERVERID=90cd839c3c54a6398b3f3f4cfa6cb288|1567559311|1567557486'
}

cookies = {
    'zg_did=%7B%22did%22%3A%20%2216c89bbd7ed17-0444739cbea2d6-7373e61-1fa400-16c89bbd7ee9f9%22%7D; bad_idb91bf240-868c-11e8-beff-b3a73470030e=4c174bd1-bd96-11e9-bc20-e71d1b8e4bb6; Hm_lvt_84c8fd20cad502132fed4406f9aa22e9=1565678885,1565703967,1566005969,1567557469; Hm_lvt_c11880ab74b1d3cd437ca5f41060fd17=1565678884,1565703967,1566005969,1567557469; nice_idb91bf240-868c-11e8-beff-b3a73470030e=383dc5e1-ceac-11e9-86a0-c515246118df; _uc_t_=375998%3B15136221475%3Bf1551265ff914b04bd821120ae47241b%3Bonline%3B1567643884149%3Bfalse; vssid=d49b188da6144c639b9025c0ec08a56f; Hm_lpvt_84c8fd20cad502132fed4406f9aa22e9=1567557486; Hm_lpvt_c11880ab74b1d3cd437ca5f41060fd17=1567557486; Hm_lvt_9f3069df154c115a922cad5be4cead79=1565703970,1566005986,1567557488; href=https%3A%2F%2Fxuexi.boxuegu.com%2F%3Fanchor%3Dcourse; accessId=b91bf240-868c-11e8-beff-b3a73470030e; qimo_seosource_b91bf240-868c-11e8-beff-b3a73470030e=%E7%AB%99%E5%86%85; qimo_seokeywords_b91bf240-868c-11e8-beff-b3a73470030e=; uniqueVisitorId=fc2cca18-5491-3eb3-91cd-b8e11579ffe8; studentId=d3ebcd38d13711e8a92200163e10f7de; Hm_lpvt_9f3069df154c115a922cad5be4cead79=1567558044; pageViewNum=9; zg_ea5fe1a9d6d94bfdbdd8a54e0ac598c2=%7B%22sid%22%3A%201567557468760%2C%22updated%22%3A%201567559311210%2C%22info%22%3A%201567557468764%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.boxuegu.com%2F%22%2C%22cuid%22%3A%20%22375998%22%7D; SERVERID=90cd839c3c54a6398b3f3f4cfa6cb288|1567559311|1567557486'
}


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


def request_url_and_write_json(id, fileName):
    """
    发起请求并保存json到本地
    """
    url = "https://www.boxuegu.com/coursePlay/getCourseKnowledgeTree?studentId=d3ebcd38d13711e8a92200163e10f7de&courseId=1129&type=PATH&_=1567558043076&moduleId=%s" % (
        id)
    response = requests.get(url, headers=headers)
    print(response.text)
    try:
        if not os.path.exists('./课程'):
            os.mkdir('./课程')
        file_path = os.path.join('./课程', fileName)
        with open(file_path, 'w', encoding='utf-8') as fp:
            fp.write(json.dumps(response.json(), ensure_ascii=False))
    except Exception as err:
        print(err)


def reading_json():
    """
    读取本地json文件
    """
    with open('01.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read(), object_hook=JSONObject)
        data_result = data.result
        for course in data_result:
            for module in course.moduleAndPhaseHomeWorkList:
                id = module.id
                name = module.name
                print("课程id：%d  名称：%s" % (id, name))
                fileName = "%s.json" % (name)
                request_url_and_write_json(id, fileName)


if __name__ == '__main__':
    reading_json()
