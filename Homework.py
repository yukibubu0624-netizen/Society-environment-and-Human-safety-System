import datetime

# ==========================================
# 模擬資料庫（標準值）
# ==========================================
database = {
    "breathing": {
        "min": 12,
        "max": 20
    },
    "food_waste": {
        "max": 5
    },
    "carbon": {
        "max": 100
    },
    # 第 4 個系統：智慧脆弱族群緊急守護系統的資料庫標準（以綜合安全指數為例，滿分100，低於60代表異常）
    "vulnerable_guard": {
        "min": 60
    }
}

# ==========================================
# 紀錄檔案
# ==========================================
LOG_FILE = "system_log.txt"

# ==========================================
# 紀錄功能（寫入紀錄檔）
# ==========================================
def write_log(system_name, value, status):
    now = datetime.datetime.now()
    
    log_message = (
        f"[{now}] "
        f"系統：{system_name} | "
        f"數值：{value} | "
        f"狀態：{status}\n"
    )
    
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_message)

# ==========================================
# 通知功能（通知相關機構）
# ==========================================
def send_notification(system_name, message, organization):
    print("\n==============================")
    print(f"【{system_name}】")
    print(f"異常訊息：{message}")
    print(f"已通知：{organization}")
    print("==============================\n")

# ==========================================
# 1. 人體呼吸中止偵測
# ==========================================
def breathing_system():
    value = float(input("請輸入呼吸頻率(次/分鐘)："))
    
    min_value = database["breathing"]["min"]
    max_value = database["breathing"]["max"]
    
    print("\n系統分析中...")
    
    if min_value <= value <= max_value:
        print("呼吸狀態正常")
        write_log(
            "人體呼吸中止偵測裝置",
            value,
            "正常"
        )
    else:
        print("呼吸異常！")
        send_notification(
            "人體呼吸中止偵測裝置",
            "偵測到呼吸異常",
            "醫療單位 / 緊急聯絡人"
        )
        write_log(
            "人體呼吸中止偵測裝置",
            value,
            "異常"
        )

# ==========================================
# 2. 剩食管理系統
# ==========================================
def food_waste_system():
    value = float(input("請輸入剩食重量(公斤)："))
    
    max_value = database["food_waste"]["max"]
    
    print("\n系統分析中...")
    
    if value <= max_value:
        print("剩食量正常")
        write_log(
            "剩食管理系統",
            value,
            "正常"
        )
    else:
        print("剩食量過高！")
        send_notification(
            "剩食管理系統",
            "剩食量超過標準值",
            "餐飲管理單位"
        )
        write_log(
            "剩食管理系統",
            value,
            "異常"
        )

# ==========================================
# 3. 環境碳排放監測
# ==========================================
def carbon_system():
    value = float(input("請輸入碳排放數值："))
    
    max_value = database["carbon"]["max"]
    
    print("\n系統分析中...")
    
    if value <= max_value:
        print("碳排放正常")
        write_log(
            "環境碳排放監測系統",
            value,
            "正常"
        )
    else:
        print("碳排放超標！")
        send_notification(
            "環境碳排放監測系統",
            "碳排放超過標準值",
            "環保機關"
        )
        write_log(
            "環境碳排放監測系統",
            value,
            "異常"
        )

# ==========================================
# 4. 面向脆弱族群的智慧人體安全預警與緊急守護系統
# ==========================================
def vulnerable_guard_system():
    # 步驟 1 & 2：選擇系統後，接收輸入訊號（感測器/穿戴裝置數據）
    print("\n--- 已啟動：面向脆弱族群的智慧人體安全預警與緊急守護系統 ---")
    value = float(input("請輸入脆弱族群生理/環境安全指數 (0-100)："))
    
    # 步驟 3：比對資料庫標準值
    min_safe_value = database["vulnerable_guard"]["min"]
    
    print("\n系統分析中...")
    
    # 步驟 4：判定是否異常
    if value >= min_safe_value:
        print("安全狀態：正常。受照顧者目前安全無虞。")
        # 步驟 6：寫入紀錄檔
        write_log(
            "智慧脆弱族群緊急守護系統",
            value,
            "正常"
        )
    else:
        print("安全狀態：⚠️ 異常！偵測到潛在危險或跌倒倒地訊號！")
        # 步驟 5：自動通知相關機構（家屬、醫療單位、救援機構）
        send_notification(
            "智慧脆弱族群緊急守護系統",
            "受照顧者安全指數過低，疑似發生緊急狀況（如跌倒或生理不適）！",
            "家屬 / 社福機構 / 緊急救援單位(119)"
        )
        # 步驟 6：寫入紀錄檔
        write_log(
            "智慧脆弱族群緊急守護系統",
            value,
            "異常（已發送緊急通知）"
        )

# ==========================================
# 主選單
# ==========================================
def main():
    while True:
        print("\n==============================")
        print(" 智慧監測整合系統 ")
        print("==============================")
        print("1. 人體呼吸中止偵測")
        print("2. 剩食管理系統")
        print("3. 環境碳排放監測")
        print("4. 智慧脆弱族群緊急守護系統")  # 新增的第 4 個選項
        print("0. 離開系統")
        print("==============================")
        
        choice = input("請選擇功能：")
        
        if choice == "1":
            breathing_system()
        elif choice == "2":
            food_waste_system()
        elif choice == "3":
            carbon_system()
        elif choice == "4":
            vulnerable_guard_system()  # 呼叫對應的函式
        elif choice == "0":
            print("\n系統已關閉")
            break
        else:
            print("\n輸入錯誤，請重新選擇")

# ==========================================
# 程式入口
# ==========================================
if __name__ == "__main__":
    main()