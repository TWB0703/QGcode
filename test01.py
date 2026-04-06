# 原始杂乱情报
raw_intel = " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X "

# 1. 利用String方法去除干扰空格
cleaned_intel = raw_intel.strip()

# 2. 解析各项信息
# 分割字符串获取各个字段
parts = cleaned_intel.split('; ')

# 提取并处理每个字段
agent_info = parts[0].split(':')[1]  # 007_Bond
coords_info = parts[1].split(':')[1]  # (40,74)
items_info = parts[2].split(':')[1]  # gun,money,gun
mission_info = parts[3].split(':')[1]  # 2025-RESCUE-X

# 3. 利用Set帮特工去除重复装备
items_list = items_info.split(',')
unique_items = list(set(items_list))  # 去重

# 4. 利用Slicing截取核心任务代号
core_mission = mission_info[5:-2]  # 从第5个字符到倒数第2个字符: RESCUE

# 5. 利用Tuple锁定坐标
# 提取坐标数字
coords_str = coords_info.strip('()')
x, y = map(int, coords_str.split(','))
coordinates = (x, y)  # 创建元组

# 6. 将所有信息归档进一个Dict档案中
intel_archive = {
    'Agent': agent_info,
    'Coordinates': coordinates,
    'Items': unique_items,
    'Core_Mission': core_mission,
    'Full_Mission': mission_info
}

# 输出清洗后的档案
print("=== 情报清洗完成 ===")
print(f"原始情报: {raw_intel}")
print(f"清洗后档案: {intel_archive}")
print("\n=== 详细信息 ===")
for key, value in intel_archive.items():
    print(f"{key}: {value}")
