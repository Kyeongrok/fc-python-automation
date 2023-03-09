import pandas as pd
import pyautogui as pg
import pyperclip
from time import sleep

df = pd.read_excel('./메세지 자동화.xlsx')

for i, row in df.iterrows():
    print(i, row['이름'])
    print(i, row['메세지'])

    # 카카오톡 클릭
    pg.moveTo(1710, 392) # x 1728 y 457
    pg.click()
    sleep(0.5)

    # 검색 버튼 나오게 하기
    pg.hotkey('ctrl', 'f')
    for i in range(15):
        pg.hotkey('backspace')

    # 이름 붙여넣기
    pyperclip.copy(row['이름'])
    pg.hotkey('ctrl', 'v')

    # 사용자 더블클릭 하기
    sleep(0.5)
    pg.moveTo(1722, 549)
    pg.doubleClick()

    # 메세지 보내기
    pg.moveTo(1689, 949)
    pg.click()
    pyperclip.copy(row['메세지'])
    pg.hotkey('ctrl', 'v')
    pg.hotkey('enter')

    # screen shot
    pg.screenshot(f"{row['이름']}_{'221120'}.png", region=(1548, 288, 1898, 1032))

    # 보낸 창 닫기
    sleep(1)
    pg.hotkey('esc')

