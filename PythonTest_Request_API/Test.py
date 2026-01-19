from datetime import datetime
from collections import defaultdict


COST_MAP = {
    "Computer": 500,
    "Printer": 300,
    "Network": 400
}


maintenance_data = [
    {"device_id": "PC-001", "type": "Computer", "date": "2025-06-01"},
    {"device_id": "PR-001", "type": "Printer",  "date": "2025-06-05"},
    {"device_id": "NT-001", "type": "Network",  "date": "2025-06-10"},
    {"device_id": "PC-002", "type": "Computer", "date": "2025-06-20"},
    {"device_id": "PR-002", "type": "Printer",  "date": "2025-05-15"},
]


def filter_by_month_year(data, month: int, year: int):
    filtered = []
    for item in data:
        date_obj = datetime.strptime(item["date"], "%Y-%m-%d")
        if date_obj.month == month and date_obj.year == year:
            filtered.append(item)
    return filtered


def calculate_cost(data):
    cost_summary = defaultdict(int)
    total = 0
    for item in data:
        device_type = item["type"]
        cost = COST_MAP.get(device_type, 0)
        cost_summary[device_type] += cost
        total += cost
    return cost_summary, total


def generate_report(month, year):
    print(f"\n📅 รายงานค่าใช้จ่าย Maintenance เดือน {month}/{year}")
    filtered_data = filter_by_month_year(maintenance_data, month, year)

    if not filtered_data:
        print("ไม่พบข้อมูล Maintenance ในช่วงเวลานี้")
        return

    cost_summary, total_cost = calculate_cost(filtered_data)

    print("\nรายละเอียด:")
    for device in filtered_data:
        print(f"  - {device['device_id']} | {device['type']} | วันที่ {device['date']}")

    print("\nสรุปรายจ่าย:")
    for device_type, cost in cost_summary.items():
        print(f"  - {device_type}: {cost} บาท")
    print(f"  ✅ รวมทั้งหมด: {total_cost} บาท")


generate_report(month=6, year=2025)