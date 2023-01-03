import dbconnect
import morpheme
import yaml

db = dbconnect.SqlCommunication()
komo = morpheme.Komo()

def yaml_trainer():
    with open('hanseo_chatbot_corpus_final.yaml', encoding = 'UTF-8') as corpus:
        corpus_deployment = yaml.load(corpus, Loader=yaml.FullLoader)
    sql = '''INSERT INTO conversation(input_text, output_text, pos_tags, tagging, link)VALUES(%s, %s, %s, %s, %s);'''
    for i in range (int(len(corpus_deployment['Conversations']))):
        user_question = corpus_deployment['Conversations'][i][0]
        user_response = corpus_deployment['Conversations'][i][1]
        try:
            user_link = corpus_deployment['Conversations'][i][2]
        except:
            user_link = 'NULL'
        converted_question_pos = komo.komo_pos(user_question)
        converted_question_pos_v2 = komo.komo_pos_v2(user_question, state = 'string')
        val = (str(user_question), str(user_response), str(converted_question_pos_v2), str(converted_question_pos), str(user_link))
        db.execute(sql, val)
        db.commit()
    print('데이터베이스 등록 완료.')

def clear_db():
    sql = '''TRUNCATE conversation;'''
    db.execute(sql,None)
    db.commit()
    print('초기화 완료.')
    
clear_db()
yaml_trainer()


def manual_trainer():
    print("학습시킬 질문을 입력하세요. : ",end = '')
    user_question = input()
    converted_question_pos = komo.komo_pos(user_question)
    converted_question_pos_v2 = komo.komo_pos_v2(user_question)
    print("학습시킬 답변을 입력하세요. : ",end = '')
    user_response = input()

    sql = '''INSERT INTO conversation(input_text, output_text, pos_tags, tagging)VALUES(%s, %s, %s, %s)'''
    val = (str(user_question), str(user_response), str(converted_question_pos_v2), str(converted_question_pos)
    )

    db.execute(sql, val)
    db.commit()

def cafeteria_update(info):
    print('학식 정보 DB를 업데이트 합니다.')
    input_text = '서산 학식 메뉴 뭐야?'
    sql = '''DELETE FROM chatbot.conversation WHERE input_text = %s'''
    val = input_text
    db.execute(sql, val)

    converted_question_pos = komo.komo_pos(input_text)
    converted_question_pos_v2 = komo.komo_pos_v2(input_text, state = 'string')

    sql = '''INSERT INTO conversation(input_text, output_text, pos_tags, tagging)VALUES(%s, %s, %s, %s)'''
    val = (input_text, info, str(converted_question_pos_v2), str(converted_question_pos))

    db.execute(sql, val)
    db.commit()
    print('학식 업데이트 완료.')

def information_update(info, **kwargs):
    print('공지사항 정보 DB를 업데이트 합니다.')
    if kwargs.get('state') == 'collage':
        input_text = '최신 학사공지 사항 뭐야?'
    elif kwargs.get('state') == 'general':
        input_text = '최신 일반공지 사항 뭐야?'

    sql = '''DELETE FROM chatbot.conversation WHERE input_text = %s'''
    val = input_text
    db.execute(sql, val)
 
    converted_question_pos = komo.komo_pos(input_text)
    converted_question_pos_v2 = komo.komo_pos_v2(input_text, state = 'string')

    sql = '''INSERT INTO conversation(input_text, output_text, pos_tags, tagging)VALUES(%s, %s, %s, %s)'''
    val = (input_text, info, str(converted_question_pos_v2), str(converted_question_pos))

    db.execute(sql, val)
    db.commit()
    print('공지사항 업데이트 완료.')

