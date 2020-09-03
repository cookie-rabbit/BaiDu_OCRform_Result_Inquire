# coding=utf-8

import re
from copy import deepcopy


class DataFind(object):
    """数据查询与整理"""

    @classmethod
    def valid_data(cls, search):
        """
        检查待查询字典列表是否符合要求
        :param search: 待查询字典列表
        :return: 检查后结果
        """
        for i in search:
            if i.get('word', None) is None:
                raise ValueError('待查询值不能为空')

            if i.get('direct', None) is None:
                raise ValueError('数据查询方向不能为空')
            i['distance'] = int(i.get('distance', 0))
            if i['distance'] < 0:
                raise ValueError('元素查询距离不能小于0')

            i['num'] = int(i.get('num', 1))
            if i['num'] < 1:
                raise ValueError('元素获取数量不能小于1')

            i['format'] = i.get('format', r'')

            i['accuracy'] = i.get('accuracy', ('like', 0))
            if not isinstance(i['accuracy'], tuple):
                raise ValueError('匹配精度必须为数组')
            if len(i['accuracy']) != 2:
                raise ValueError('匹配精度元祖长度必须为2')
            if i['accuracy'][0] not in ['like', 'equal'] or int(i['accuracy'][1]) < 0:
                raise ValueError('匹配精度模式必须为 like, equal 中的一个，且定位数必须大于0')

        return search

    @classmethod
    def content_handle(cls, content, search):
        """
        内容获取
        :param content: 处理后的OCR识别结果
        :param search: 待查询字典列表
        :return: 查询到的相关结果，待进一步处理
        """
        data = []
        for i in search:
            infos = []
            direct = 'row' if i.get('direct', 1) in [1, 2] else 'column'
            for j in content:

                word = i.get('word', None)
                if word is None:
                    raise ValueError('待查询值不能为空')

                contain_judge = "contains(j.get('word', ''), word)"
                equal_judge = "j.get('word', '') == word"
                a = contain_judge if i.get('accuracy', ('like', 0))[0] == 'like' else equal_judge
                if eval(a):
                    res = deepcopy(j)
                    res.update({'value': [], 'word': word})
                    res.update(i)
                    infos.append(res)
                continue

            if infos:
                try:
                    info = deepcopy(infos[int(i.get('accuracy')[1])])
                except IndexError:
                    info = deepcopy(infos[-1])
                    data.append(info)
                    continue
                line = info.get('row') if i.get('direct', 1) in [1, 2] else info.get('column')
                limit_line = info.get('column') if i.get('direct', 1) in [1, 2] else info.get('row')
                limit_direct = 'row' if direct == 'column' else 'column'
                for j in content:
                    if j.get(limit_direct)[0] > limit_line[-1] if i.get('direct') in [1, 4] else j.get(
                            limit_direct)[-1] < limit_line[0]:
                        if j.get(direct)[0] >= line[0] and j.get(direct)[-1] <= line[-1]:
                            if j.get('row') == info.get('row') and j.get('column') == info.get('column'):
                                continue
                            info['value'].append(j.get('word', ''))
                data.append(info)
            else:
                i['value'] = ''
                data.append(i)
        return data

    @classmethod
    def data_handle(cls, content, search):
        """
        数据截取，正则化处理
        :param content: 处理后的OCR识别结果
        :param search: 待查询字典列表
        :return: 截取，正则化处理后的查询结果
        """
        valid_search = cls.valid_data(search)
        data = cls.content_handle(content, valid_search)
        print(data)
        for i in data:
            number_rule = re.compile(f'{i.get("format")}')
            try:
                value = i.get('value')[i.get('distance'):i.get('distance') + i.get('num')]
            except IndexError:
                value = ''
            value = list(j for j in value if number_rule.match(j))
            i['value'] = value
        return data
