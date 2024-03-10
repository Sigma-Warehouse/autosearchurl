import csv

# 結果を保存するCSVファイルのパス
output_csv_path = r'C:\path\to\your\output.csv'  # 出力ファイルのパスを設定

# CSVファイルに結果を書き込む関数
def write_to_csv(url, title, is_japanese):
    with open(output_csv_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([url, title, "日本語" if is_japanese else "非日本語"])

def is_japanese(text):
    for char in text:
        if '\u3000' <= char <= '\u303f' or \
            '\u3040' <= char <= '\u309f' or \
            '\u30a0' <= char <= '\u30ff' or \
            '\u3400' <= char <= '\u4dbf' or \
            '\u4e00' <= char <= '\u9fff' or \
            '\uff66' <= char <= '\uff9f':
            return True
    return False

#skip rows
skip_n = 0

#Execution count
exe_count = 0

# CSVファイルのパス
csv_file_path = r'C:\path\to\your\file.csv'  # CSVファイルのパスを正確に設定してください
user_data_dir = r'C:\Users\[ユーザー名]\AppData\Local\Google\Chrome\User Data'  # [ユーザー名]を実際のものに置き換えてください

# Chromeのオプション設定
options = Options()
options.add_argument(f"user-data-dir={user_data_dir}")
options.add_argument('--profile-directory=Default')

# WebDriverの初期化
driver = webdriver.Chrome(options=options)

def main():

    global driver, exe_count
    # CSVファイルを開く
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        #skip the first n +1 rows.
        for _ in range(skip_n+1):
            next(reader)

        for row in reader:
            url = row[1]  # URLを読み込む
            exe_count += 1
            try:
                print(f"{exe_count}, {url}")
                # URLを新しいタブで開く
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(url)

                # ページの<title>を取得して日本語かどうかをチェック
                title = driver.title
                if is_japanese(title):
                    print(f"タイトル '{title}' は日本語です。")
                    write_to_csv(url, title, True)

                time.sleep(5)
                
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except Exception as e:
                print(f"URL: {url}, エラーが発生しました: {e}")
                driver.quit()
                driver = webdriver.Chrome(options=options)
                continue

    driver.quit()

if __name__ == '__main__':
    main()
