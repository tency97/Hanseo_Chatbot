import dbconnect
import morpheme
from collections import Counter
"""
id_list는 pos_tags에 저장된 입력한 질문의 명사 리스트를 데이터베이스 
명사 태그들과 하나씩 비교하여 그 명사가 들어있는 해당 답변의 번호를 출력한다. 
"""

db = dbconnect.SqlCommunication()
komo = morpheme.Komo()

class NoOneWordError(Exception):
    def __init__(self):
        super().__init__('Try more than One Word!')

#indexing db
def response_select(user_input):
    pos_list = komo.komo_pos_v2(user_input, state = 'normal')
    id_list = []
    sql = '''SELECT id FROM conversation WHERE pos_tags LIKE %s;'''
    for i in range (len(pos_list)):
        val = ('%' + pos_list[i] + '%',)
        result = db.fetchall(sql,val)
        try:
            for j in range (len(result)):
                id_list.append(result[j][0])
        except:
            pass

    mfv = Counter(id_list).most_common() # most frequency value, [(질문번호1, 점수1), (질문번호2, 점수2)]
    selected_response = []
    try:
        sql = '''SELECT output_text FROM chatbot.conversation WHERE id = %s;''' # 디테일한 질문에 대한 답변을 도출하는 쿼리문
        val = (mfv[0][0],)
        selected_response.append(db.fetchone(sql,val))
        if len(user_input) < 2:
            raise NoOneWordError
        try:
            sql = '''SELECT input_text FROM conversation WHERE id = %s;''' # 유사 질문 4개를 출력하기 위한 쿼리문
            for i in range (1,5):
                val = (mfv[i][0],)
                selected_response.append(db.fetchone(sql,val))
        except:
            for i in range (1,5):
                selected_response.append([('NULL'),]) # 유사 질문이 없는 경우 출력 형태를 맞추기 위한 NULL 처리
    except:
        selected_response = [('죄송해요. 잘 모르겠어요.',)] # 검색결과가 없을 때 송출 메시지
        for i in range (1,5):
                selected_response.append([('NULL'),])
    return selected_response