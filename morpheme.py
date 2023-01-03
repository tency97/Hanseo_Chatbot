from konlpy.tag import Komoran

class Komo:
    def __init__(self):
        self.komo = Komoran(userdic='dic.user')
    def komo_pos(self, user_input): # 평문을 코모란 형태소로 변환합니다.
        result = self.komo.pos(user_input)
        return result

    def komo_pos_v2(self, user_input, **kwargs): # 명사, 형용사, 동사를 추출합니다.
        raw_list = self.komo.pos(user_input)
        mod_list = []
        for i in range(len(raw_list)):
            if (raw_list[i][1] == 'NNP'
            or raw_list[i][1] == 'NNG'
            or raw_list[i][1] == 'VV'
            or raw_list[i][1] =='VA'
            or raw_list[i][1] == 'NA'):
                mod_list.append(raw_list[i][0])

        if kwargs.get('state') == 'normal':
            return mod_list
        elif kwargs.get('state') == 'string':
            result = ", ".join(mod_list)
            return result