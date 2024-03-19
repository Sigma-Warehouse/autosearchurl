import csv

# 入力と出力ファイルのパス
input_csv_path = 'online-valid.csv'
output_csv_path = 'sample1.csv'

# 入力ファイルを読み込み
with open(input_csv_path, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    filtered_rows = []

    # `verified`が"yes"の行を抽出し、`verified`を1に変換
    for row in reader:
        if row['verified'] == 'yes':
            row['verified'] = 1
            filtered_rows.append(row)

# 出力ファイルに書き込み
with open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:
    fieldnames = ['id', 'url', 'verified']  # 出力ファイルの列名
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, row in enumerate(filtered_rows, start=1):
        writer.writerow({'id': i, 'url': row['url'], 'verified': row['verified']})
