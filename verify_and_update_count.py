import os
import csv
from collections import defaultdict

# 定义路径
STATIC_DIR = '/Users/easyo/Desktop/vividict_crawl/oeasy_oracle/static'
COUNT_CSV = '/Users/easyo/Desktop/vividict_crawl/oeasy_oracle/count.csv'

# 步骤1: 遍历static目录下的所有子文件夹，统计每个文件夹中的PNG和SVG文件数量
print("正在统计static目录下的文件数量...")
actual_counts = defaultdict(int)

# 遍历所有子文件夹
for root, dirs, files in os.walk(STATIC_DIR):
    # 只处理一级子目录
    if root == STATIC_DIR:
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            # 统计该目录下的PNG和SVG文件数量
            count = 0
            for file in os.listdir(dir_path):
                if file.lower().endswith('.png') or file.lower().endswith('.svg'):
                    count += 1
            actual_counts[dir_name] = count
            print(f"目录 {dir_name}: {count} 个文件")

# 步骤2: 读取count.csv文件中的记录
print("\n正在读取count.csv文件...")
csv_records = []
csv_dir_counts = defaultdict(int)

with open(COUNT_CSV, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            # 解析行，格式为 "行号→目录名,数量"
            line = row[0].strip()
            if '→' in line and ',' in line:
                line_num_part, rest = line.split('→', 1)
                dir_name, count_part = rest.split(',', 1)
                line_num = line_num_part.strip()
                dir_name = dir_name.strip()
                count = int(count_part.strip())
                csv_records.append((line_num, dir_name, count))
                csv_dir_counts[dir_name] = count

# 步骤3: 比较实际数量和CSV中的记录
print("\n比较实际数量和CSV中的记录...")
discrepancies = []
missing_in_csv = []

# 检查CSV中记录的目录
for dir_name, csv_count in csv_dir_counts.items():
    if dir_name in actual_counts:
        actual_count = actual_counts[dir_name]
        if csv_count != actual_count:
            discrepancies.append((dir_name, csv_count, actual_count))
    else:
        # CSV中记录的目录在实际中不存在
        print(f"警告: CSV中记录的目录 {dir_name} 在static目录中不存在")

# 检查实际存在但CSV中没有记录的目录
for dir_name, actual_count in actual_counts.items():
    if dir_name not in csv_dir_counts:
        missing_in_csv.append((dir_name, actual_count))

# 步骤4: 更新count.csv文件
if discrepancies or missing_in_csv:
    print("\n发现不匹配，正在更新count.csv文件...")
    
    # 创建新的记录列表，保留原有的行号格式
    new_records = []
    line_num = 1
    
    # 首先处理原有的记录
    for old_line_num, dir_name, csv_count in csv_records:
        if dir_name in actual_counts:
            # 更新数量为实际数量
            new_count = actual_counts[dir_name]
            new_records.append(f"{line_num}→{dir_name},{new_count}")
            line_num += 1
    
    # 然后添加CSV中缺失的目录
    for dir_name, actual_count in missing_in_csv:
        new_records.append(f"{line_num}→{dir_name},{actual_count}")
        line_num += 1
    
    # 写入更新后的内容
    with open(COUNT_CSV, 'w', encoding='utf-8') as f:
        for record in new_records:
            f.write(record + '\n')
    
    print("更新完成！")
    
    # 输出统计信息
    print(f"\n统计信息:")
    print(f"- 检查的目录总数: {len(actual_counts)}")
    print(f"- CSV中更新的记录数: {len(discrepancies)}")
    print(f"- CSV中新增的记录数: {len(missing_in_csv)}")
    
    if discrepancies:
        print(f"\n不匹配的记录 (", len(discrepancies), "条):")
        print("目录名, CSV数量, 实际数量")
        for dir_name, csv_count, actual_count in discrepancies:
            print(f"{dir_name}, {csv_count}, {actual_count}")
    
    if missing_in_csv:
        print(f"\nCSV中缺失的记录 (", len(missing_in_csv), "条):")
        print("目录名, 实际数量")
        for dir_name, actual_count in missing_in_csv:
            print(f"{dir_name}, {actual_count}")
else:
    print("\n所有记录都匹配，无需更新！")
    print(f"检查的目录总数: {len(actual_counts)}")