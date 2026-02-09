raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99", "120"]

# 数据清洗与处理
cleaned_data = []
for item in raw_data:
    try:
        # 跳过非数字项
        value = float(item)
        # 仅保留≥80的数值
        if value >= 80:
            # 归一化为0.xx-1.xx小数 (除以100)
            normalized = value / 100
            cleaned_data.append(normalized)
    except ValueError:
        continue  # 跳过无法转换为数字的项

# 输出结果
print("=== 能源核心数据报告 ===")
print(f"原始数据: {raw_data}")
print(f"清洗后有效数据: {cleaned_data}")
print()

for i, value in enumerate(cleaned_data, 1):
    status = "核心过载" if value > 1.0 else "运转正常"
    print(f"核心{i}: {value:.2f} - {status}")