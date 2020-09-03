# coding=utf-8


import ast


class PrepareData(object):
    """
    该类处理从OCR识别得到的结果，加工成后续方便处理的结果
    """

    @classmethod
    def get_data(cls, result):
        """
        处理接口返回，去除错误结果
        :param result: OCR接口获取的待处理数据
        :return: 处理后的结果
        eg:
            {
                'data':'data',
                'data2':'data2',
            }
        """
        content = result.get('result', False)
        if not content:
            error_code = result.get('error_code', '00001')
            error_msg = result.get('error_msg', '未知错误')
            raise ValueError("识别错误！" + "   " + "错误码:" + str(error_code) + "," + "错误信息:" + str(error_msg))

        # 正常获取数据，开始读取header
        result_data = content.get('result_data', False)
        if not result_data:
            raise ValueError('无法识别表单，请重新上传图像')

        result_data = ast.literal_eval(result_data)
        return result_data

    @classmethod
    def pretreatment_body(cls, result):
        """
        对数据预处理，提取 body 部分数据中的部分字段，只保留有用字段
        :param result: OCR接口获取的待处理数据，经前一个函数处理过异常并将字符串转为json格式
        :return: 处理结果
        eg:
            [
                {'word': '查询内容',
                 'column': '查询内容所属列',
                 'row': '查询内容所属行',
                },
                {'word': '查询内容2',
                 'column': '查询内容2所属列',
                 'row': '查询内容2所属行',
                },
            ]
        """
        result_data = cls.get_data(result)
        body = result_data.get('forms')[0].get('body')
        pretreatment_body = []
        for i in body:
            res = {'word': i.get('word'), 'column': i.get('column'), 'row': i.get('row')}
            pretreatment_body.append(res)
        return pretreatment_body
