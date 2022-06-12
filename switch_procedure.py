switch_istatus = Faise #สถานะ

def turnon(): #ฟังก์ชันเปิดไฟ
    global switch_status
    switch_status = True
    print("ไฟเปิด")

def turnoff(): #ฟังก์ชันปิดไฟ
    global switch_status
    switch_status = False
    print("ไฟปิด")

if__naem__== "__main__":
    print(f'สถานะไฟ: {switch_status')
    turnon()
    turnoff()
    turnoff()
    turnoff()