import pyautogui as pg
import pyperclip
from time import sleep

# 카카오톡 클릭
pg.moveTo(1710, 392)
pg.click()

# 검색 버튼 나오게 하기
pg.hotkey('ctrl', 'f')

# 이름 붙여넣기
pyperclip.copy('W사 이아름 차장')
pg.hotkey('ctrl', 'v')

# 사용자 더블클릭 하기
sleep(0.5)
pg.moveTo(1722, 549)
pg.doubleClick()

# 메세지 보내기
pg.moveTo(1689, 949)
pg.click()
pyperclip.copy('안녕하세요. KY마케팅 담당자 김경록입니다. 금일 네이버 파워링크 광고리포트 발송 드립니다. "신생아 가습기"키워드 CPC 452원으로 클릭수 23회, 클릭률 0.34% 총 광고비 10,396원입니다. 감사합니다.')
pg.hotkey('ctrl','v')
pg.hotkey('enter')