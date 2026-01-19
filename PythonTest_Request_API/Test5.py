# ข้อมูลจาก InvItem
inv_item = [
    {'Item No': 'A001', 'Group': 'A'},
    {'Item No': 'A002', 'Group': 'A'},
    {'Item No': 'A003', 'Group': 'A'},
    {'Item No': 'B001', 'Group': 'B'},
    {'Item No': 'B002', 'Group': 'B'},
    {'Item No': 'C001', 'Group': 'C'},
]

# ข้อมูลจาก InvStockTrans
inv_stock_trans = [
    {'Item No': 'A002', 'Qty': 2, 'RefId': 'Ref_001'},
    {'Item No': 'A002', 'Qty': 3, 'RefId': 'Ref_002'},
    {'Item No': 'A002', 'Qty': -1, 'RefId': 'Ref_002'},
    {'Item No': 'B001', 'Qty': 1, 'RefId': 'Ref_006'},
    {'Item No': 'B002', 'Qty': 2, 'RefId': 'Ref_007'},
    {'Item No': 'B002', 'Qty': 2, 'RefId': 'Ref_008'},
    {'Item No': 'C001', 'Qty': -1, 'RefId': 'Ref_009'},
]

# ข้อมูลจาก InvWH
inv_wh = [
    {'RefId': 'Ref_001', 'Warehouse': 'RM'},
    {'RefId': 'Ref_002', 'Warehouse': 'FG'},
    {'RefId': 'Ref_003', 'Warehouse': 'FG'},
    {'RefId': 'Ref_004', 'Warehouse': 'RM'},
    {'RefId': 'Ref_005', 'Warehouse': 'RM'},
    {'RefId': 'Ref_006', 'Warehouse': 'RM'},
    {'RefId': 'Ref_007', 'Warehouse': 'FG'},
    {'RefId': 'Ref_008', 'Warehouse': 'RM'},
    {'RefId': 'Ref_009', 'Warehouse': 'RM'},
]

# 1. หาว่า RefId ไหนอยู่ในคลัง RM
rm_ref_ids = []
for wh in inv_wh:
    if wh['Warehouse'] == 'RM':
        rm_ref_ids.append(wh['RefId'])

# 2. กรองเฉพาะรายการใน RM
rm_stock = []
for row in inv_stock_trans:
    if row['RefId'] in rm_ref_ids:
        rm_stock.append(row)

# 3. สร้าง map ของ item -> group
item_to_group = {}
for item in inv_item:
    item_to_group[item['Item No']] = item['Group']

# 4. รวม Qty ตาม Group
group_qty = {}
for row in rm_stock:
    item = row['Item No']
    qty = row['Qty']
    group = item_to_group.get(item)
    if group:
        group_qty[group] = group_qty.get(group, 0) + qty

# 5. แสดงผลเรียงตาม Group
for group in sorted(group_qty.keys()):
    print(f"{group}\t{group_qty[group]}")
