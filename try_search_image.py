import sys
import os
import time
import csv
import pyperclip
import pyautogui as pya
from dotenv import load_dotenv

load_dotenv()
CSV_PATH = os.getenv("CSV_PATH")

if __name__ == "__main__":
    time.sleep(2)
    tab_x, tab_y =  290,214
    url_x, url_y =  261,258
    close_tab_x, close_tab_y = 473,219
    count = 0
    start_line = 4272  # 開始行を設定

    with open(CSV_PATH, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader, 1):  
            if i < start_line:
                continue    
            pya.click(tab_x, tab_y)
            time.sleep(1)
            pya.click(url_x, url_y)
            search_url = row[1]
            pya.write(search_url)
            time.sleep(1)
            pya.press('enter')
            time.sleep(4)
            pya.click(close_tab_x, close_tab_y)
            count += 1
            print(f"実行回数: {count}")

#マウスカーソルで座標の取得
# while True:
#         x, y = pya.position()
#         print(f"Current mouse position: X={x}, Y={y}")
#         time.sleep(2)
# while True:
    #     x, y = pya.position()
    #     print(f"Current mouse position: X={x}, Y={y}")
    #     time.sleep(2)
#検索バーの位置Current mouse position: X=443, Y=70
#タブの新しい画面を開く場所Current mouse position: X=314, Y=62
#タブのばつ印座標Current mouse position: X=227, Y=24
#タブを閉じるCurrent mouse position: X=463, Y=21