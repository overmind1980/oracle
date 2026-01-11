import os

# 检查目录结构
base_path = "/Users/easyo/Desktop/vividict_crawl"
oeasy_path = os.path.join(base_path, "oeasy_oracle")
static_path = os.path.join(oeasy_path, "static")

print(f"检查基本路径: {base_path}")
print(f"基本路径存在: {os.path.exists(base_path)}")
print(f"基本路径是目录: {os.path.isdir(base_path)}")

print(f"\n检查oeasy_oracle路径: {oeasy_path}")
print(f"oeasy_oracle路径存在: {os.path.exists(oeasy_path)}")
print(f"oeasy_oracle路径是目录: {os.path.isdir(oeasy_path)}")

if os.path.exists(oeasy_path) and os.path.isdir(oeasy_path):
    print(f"\noeasy_oracle目录内容:")
    try:
        contents = os.listdir(oeasy_path)
        print(f"目录项数量: {len(contents)}")
        for item in sorted(contents):
            item_path = os.path.join(oeasy_path, item)
            item_type = "目录" if os.path.isdir(item_path) else "文件"
            print(f"  {item} ({item_type})")
    except Exception as e:
        print(f"  读取目录内容失败: {str(e)}")

print(f"\n检查static路径: {static_path}")
print(f"static路径存在: {os.path.exists(static_path)}")
print(f"static路径是目录: {os.path.isdir(static_path)}")

if os.path.exists(static_path) and os.path.isdir(static_path):
    print(f"\nstatic目录内容:")
    try:
        contents = os.listdir(static_path)
        print(f"目录项数量: {len(contents)}")
        for item in sorted(contents):
            item_path = os.path.join(static_path, item)
            item_type = "目录" if os.path.isdir(item_path) else "文件"
            print(f"  {item} ({item_type})")
    except Exception as e:
        print(f"  读取目录内容失败: {str(e)}")
