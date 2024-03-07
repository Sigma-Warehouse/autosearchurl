import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

#skip rows
skip_n = 0

#Execution count
exe_count = 0

# CSVファイルのパス
csv_file_path = r'C:\'
user_data_dir = r'C:\Users\[ユーザー名]\AppData\Local\Google\Chrome\'

# Chromeのオプション設定
options = Options()
options.add_argument(f"user-data-dir={user_data_dir}")
options.add_argument('--profile-directory=Default')

# 必要に応じてオプションを追加
# options.add_argument('--headless')  # ヘッドレスモードを有効にする場合

# WebDriverの初期化
driver = webdriver.Chrome(options=options)

def main():
    global driver
    # CSVファイルを開く
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        #skip the first n +1 rows.
        for _ in range(skip_n+1):
            next(reader)

        for row in reader:
            url = row[1]  # URLを読み込む
            try:
                print(f"{exe_count}, {url}")
                # URLを新しいタブで開く
                driver.execute_script("window.open('');")  # 新しいタブを開く
                driver.switch_to.window(driver.window_handles[-1])  # 新しいタブに切り替え
                driver.get(url)  # URLを開く

                # URLを開いた後の処理（必要に応じて）
                
                time.sleep(5)  # ページの読み込み等のために待機
                
                # タブを閉じて、最初のタブに戻る
                driver.close()  # 現在のタブを閉じる
                driver.switch_to.window(driver.window_handles[0])  # 最初のタブに戻る
            except Exception as e:
                print(f"URL: {url}, エラーが発生しました: {e}")
                #Reopen the driver in case of error occurs
                driver.quit()
                driver = webdriver.Chrome(options=options)
                continue  # 次のループへ進む
            

    # 全てのURLの処理が終わったら、ブラウザを閉じる
    driver.quit()

if __name__ == '__main__':
    main()
