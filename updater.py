import schedule # 정해진 시간에 코드 실행시켜주는 모듈
import time # 그냥 시간모듈


# def cafeteria_update(): # 학식정보 업데이트
#     information_scraper.cafeteria_info()

# def notice_update(): # 공지 두개 동시 업데이트
#     information_scraper.notice_info()

def timer(): # 터미널에 시간을 표시해줍니다.

    print(time.strftime('\rwaiting for update... %X', time.localtime(time.time())), end='') # 터미널에서 시간보기용

schedule.every(1).second.do(timer) # 매 초마다 시간 표시해줍니다
# schedule.every().monday.at("10:30").do(cafeteria_update) # 항상 월요일 10시 30분에 학식정보를 스크래핑 해서 자동으로 db에 업데이트
# schedule.every(10).seconds.do(notice_update) # 3시간마다 일반공지랑 학사공지를 스크래핑해서 자동으로 db 업데이트

while True:
    schedule.run_pending() #무한루프를 돌면서 스케쥴 유지
    time.sleep(1)

# ex))
# schedule.every(30).minutes.do(printhello) #30분마다 실행
# schedule.every().monday.at("00:10").do(printhello) #월요일 00:10분에 실행
# schedule.every().day.at("10:30").do(job) #매일 10시30분에 