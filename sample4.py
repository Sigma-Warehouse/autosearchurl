import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

# CSVファイルのパス
csv_file_path = '/Users/yurainagaki/Desktop/autogui/verified_online (1).csv'
user_data_dir = r'C:\Users\[ユーザー名]\AppData\Local\Google\Chrome\'
# Chromeのオプション設定
options = Options()
options.add_argument(f"user-data-dir={user_data_dir}")
# 必要に応じてオプションを追加
# options.add_argument('--headless')  # ヘッドレスモードを有効にする場合

# WebDriverの初期化
driver = webdriver.Chrome(options=options)

# CSVファイルを開く
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # URLを新しいタブで開く
        driver.execute_script("window.open('');")  # 新しいタブを開く
        driver.switch_to.window(driver.window_handles[-1])  # 新しいタブに切り替え
        url = row[1]  # URLを読み込む
        
        # try-exceptブロックを使用してURLを開く
        try:
            driver.get(url)  # URLを開く
        except Exception as e:
            print(f"URLを開く際にエラーが発生しました: {e}")
            driver.close()  # エラーが発生したタブを閉じる
            driver.switch_to.window(driver.window_handles[0])  # 最初のタブに戻る
            continue  # 次のループへ進む
        
        # URLを開いた後の処理（必要に応じて）
        
        time.sleep(5)  # ページの読み込み等のために待機
        
        # タブを閉じて、最初のタブに戻る
        driver.close()  # 現在のタブを閉じる
        driver.switch_to.window(driver.window_handles[0])  # 最初のタブに戻る

# 全てのURLの処理が終わったら、ブラウザを閉じる
driver.quit()
