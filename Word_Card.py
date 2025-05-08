import os
import csv

# 指定資料夾路徑
folder_path = r'C:\Users\Jimmy\AppData\Roaming\Anki2\使用者 1\collection.media'  # 替換為你的資料夾路徑

# 取得資料夾中所有檔案名稱
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 寫入CSV檔案
csv_file = 'file_names.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for name in file_names:
        writer.writerow([name[0:-4],f'<img src="{name}"/>'])

print(f"檔案名稱已成功寫入 {csv_file}")
