import csv

# 既存のCSVファイルのパス
input_file_path = 'top50.csv'
# 出力する新しいCSVファイルのパス
output_file_path = 'top50-sample.csv'

# 新しいCSVファイルに書き込むデータを準備するリスト
data_to_write = []

# 既存のCSVファイルを読み込む
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file)
    for index, row in enumerate(reader, start=1):
        # 各行のURLを取得し、新しいデータ行を作成
        url = row[0]
        new_row = [index, url, 1]
        # 新しいデータ行をリストに追加
        data_to_write.append(new_row)

# 新しいCSVファイルにデータを書き込む
with open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file)
    # ヘッダー行を書き込む
    writer.writerow(['id', 'url', 'verified'])
    # データ行を書き込む
    writer.writerows(data_to_write)

print(f"New CSV file has been created at {output_file_path}")


# import csv

# # 入力ファイルと出力ファイルのパス
# input_file = 'seijyo_sample.csv'
# output_file = 'urls.csv'

# # CSVファイルを開く
# with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
#     # CSVリーダーとライターを作成
#     reader = csv.reader(infile)
#     fieldnames = ['id', 'url', 'valid']
#     writer = csv.DictWriter(outfile, fieldnames=fieldnames)

#     # ヘッダー行を書き込む
#     writer.writeheader()

#     # 各行をループ
#     for index, row in enumerate(reader, start=1):
#         # 指定された列を出力ファイルに書き込む
#         output_row = {'id': index, 'url': row[0], 'valid': 0}
#         writer.writerow(output_row)