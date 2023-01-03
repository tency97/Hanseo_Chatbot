import trainer
from bs4 import BeautifulSoup # 웹 스크래핑 및 파싱 모듈
# from pprint import pprint # 가독성 있게 텍스트 바꿔줌
import requests # html을 모두 긁어줌 테스트로 보는 용이라 실제로는 없어도 되는듯.

def cafeteria_info():
    html = requests.get('https://www.hanseo.ac.kr/food/foodView.do?m=0504&s=hs') # 학식정보 있는 html주소
    #pprint(html.text)

    soup = BeautifulSoup(html.text, 'html.parser')
    # pprint(soup)

    data1 = soup.findAll('td')

    data2 = []
    result = []
    for i in range(len(data1)):
        data2.append(data1[i].get_text(separator=", "))

    for j in range(len(data2)):
        if not data2[j]:
            data2[j] = '없음'

    for k in range(len(data2)):
        result.append(data2[k])
        result.append('\n')
        if (k+1) % 4 == 0:
            result.append('\n')
    output = ''.join(result)
    print(output)
    trainer.cafeteria_update(output)

def notice_info():
    SHOW_AMOUNT = 10 # 루프 돌리는 만큼 보여주는 양 변화
    html_collage = requests.get('https://www.hanseo.ac.kr/boardCnts/list.do?boardID=298&m=040101&s=hs')
    html_general = requests.get('https://www.hanseo.ac.kr/boardCnts/list.do?boardID=299&m=040102&s=hs')
    #pprint(html.text)
    for html in (html_collage, html_general):

        soup = BeautifulSoup(html.text, 'html.parser')
        # pprint(soup)
        get_title = [] # 일반공지 제목 저장을 위한 배열 선언
        for i in range(SHOW_AMOUNT):
            data1 = soup.select('td > a')[i]['title'] # title의 내용만 파싱해서 배열 저장
            get_title.append(data1)

        print()
        print(get_title)
        output = '\n\n'.join(get_title)
        collage_link = "학사 공지사항 링크 :\nhttps://www.hanseo.ac.kr/boardCnts/list.do?boardID=298&m=040101&s=hs\n\n"
        general_link = "일반 공지사항 링크 :\nhttps://www.hanseo.ac.kr/boardCnts/list.do?boardID=299&m=040102&s=hs\n\n"
        if (html == html_collage):
            trainer.information_update(collage_link+output, state = 'collage')
        elif (html == html_general):
            trainer.information_update(general_link+output, state = 'general')

cafeteria_info()
notice_info()