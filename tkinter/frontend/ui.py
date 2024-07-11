import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from backend import main
backend = main.main()

import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk, messagebox

root = tk.Tk()

root.title("측정 프로그램")
root.geometry("350x500")

# 첫 번째 화면 프레임
frame1 = tk.Frame(root)
frame1.pack(fill="both", expand=True)

# 두 번째 화면 프레임
frame2 = tk.Frame(root)
frame2.pack(fill="both", expand=True)
frame2.pack_forget()  # 처음에는 숨기기

# 세 번째 화면 프레임 (전화번호 입력)
frame_phone = tk.Frame(root)
frame_phone.pack(fill="both", expand=True)
frame_phone.pack_forget()  # 처음에는 숨기기

# 네 번째 화면 프레임 (이메일 입력)
frame_email = tk.Frame(root)
frame_email.pack(fill="both", expand=True)
frame_email.pack_forget()  # 처음에는 숨기기

# 다섯 번째 화면 프레임 (검사 시작 후 화면)
frame3 = tk.Frame(root)
frame3.pack(fill="both", expand=True)
frame3.pack_forget()  # 처음에는 숨기기

# 여섯 번째 화면 프레임 (신체 측정 화면)
frame_physical_measurements = tk.Frame(root)
frame_physical_measurements.pack(fill="both", expand=True)
frame_physical_measurements.pack_forget()  # 처음에는 숨기기

# 일곱 번째 화면 프레임 (신체 측정 결과 보기 화면)
result_frame = tk.Frame(root)
result_frame.pack(fill="both", expand=True)
result_frame.pack_forget() # 처음에는 숨기기

# 아홉 번째 화면 프레임 (혈액 측정 화면)
frame_blood_measure = tk.Frame(root)
frame_blood_measure.pack(fill="both", expand=True)
frame_blood_measure.pack_forget()  # 처음에는 숨기기

# 열 번째 화면 프레임 (혈액 측정 결과 보기 화면)
frame_results = tk.Frame(root)
frame_results.pack(fill="both", expand=True)
frame_results.pack_forget()  # 처음에는 숨기기

# 열두 번째 화면 프레임 (01 Face)
frame01 = tk.Frame(root)
frame01.pack(fill="both", expand=True)
frame01.pack_forget()  # 처음에는 숨기기

# 열세 번째 화면 프레임 (02 Body)
frame02 = tk.Frame(root)
frame02.pack(fill="both", expand=True)
frame02.pack_forget()  # 처음에는 숨기기

# 열네 번째 화면 프레임 (03 Skin)
frame03 = tk.Frame(root)
frame03.pack(fill="both", expand=True)
frame03.pack_forget()  # 처음에는 숨기기

# 열다섯 번째 화면 프레임 (04 Eye)
frame04 = tk.Frame(root)
frame04.pack(fill="both", expand=True)
frame04.pack_forget()  # 처음에는 숨기기

# 열여섯 번째 화면 프레임 (05 Gait)
frame05 = tk.Frame(root)
frame05.pack(fill="both", expand=True)
frame05.pack_forget()  # 처음에는 숨기기

# 열일곱 번째 화면 프레임 (06 Sleeping)
frame06 = tk.Frame(root)
frame06.pack(fill="both", expand=True)
frame06.pack_forget()  # 처음에는 숨기기

# 열여덟 번째 화면 프레임 (English)
frame_en = tk.Frame(root)
frame_en.pack(fill="both", expand=True)
frame_en.pack_forget()  # 처음에는 숨기기

# 열아홉 번째 화면 프레임 (tel 입력))
frame_tel = tk.Frame(root)
frame_tel.pack(fill="both", expand=True)
frame_tel.pack_forget()  # 처음에는 숨기기

# 스무 번째 화면 프레임 (email 입력)
frame_en_email = tk.Frame(root)
frame_en_email.pack(fill="both", expand=True)
frame_en_email.pack_forget()  # 처음에는 숨기기

# 스물한 번째 화면 프레임 (결과지)
report = tk.Frame(root)
report.pack(fill="both", expand=True)
report.pack_forget()

photo = tk.PhotoImage(file='global.png')
image = tk.Label(frame1, image=photo)
image.place(x=125, y=30)

custom_font1 = tkfont.Font(family='GungSeo', size=17, weight='bold')
custom_font2 = tkfont.Font(family='GungSeo', size=14, weight='bold')
custom_font3 = tkfont.Font(family='GungSeo', size=10)

phone_number = ""
email_address = ""

def on_click(button, switch_frame=None):
    original_color = button.cget("background")
    button.config(bg="yellow")
    if switch_frame:
        root.after(50, lambda: [button.config(bg=original_color), switch_frame()])
    else:
        root.after(50, lambda: button.config(bg=original_color))

def switch_to_frame(frame):
    frame1.pack_forget()
    frame2.pack_forget()
    frame_phone.pack_forget()
    frame_email.pack_forget()
    frame3.pack_forget()
    frame_physical_measurements.pack_forget()
    result_frame.pack_forget()
    frame_blood_measure.pack_forget()
    frame_results.pack_forget()
    frame01.pack_forget()
    frame02.pack_forget()
    frame03.pack_forget()
    frame04.pack_forget()
    frame05.pack_forget()
    frame06.pack_forget()
    frame_en.pack_forget()
    frame_tel.pack_forget()
    frame_en_email.pack_forget()
    report.pack_forget()
    frame.pack(fill="both", expand=True)

    button_show_results.config(state=tk.DISABLED)
    button_view_results.config(state=tk.DISABLED)

    # 프레임 전환 시 초기화 추가
    if frame == frame_phone:
        entry_phone.delete(0, tk.END) # 전화번호 입력 초기화
        combo_prefix.current(0)
    elif frame == frame_tel:
        entry_tel.delete(0, tk.END) # 전화번호 입력 초기화
        combo_prefix_tel.current(0)
    elif frame == frame_email:
        entry_email_local.delete(0, tk.END)  # 이메일 local 부분 초기화
        entry_email_domain.delete(0, tk.END)  # 이메일 domain 부분 초기화
    elif frame == frame_en_email:
        entry_email_local_en.delete(0, tk.END)  # 이메일 local 부분 초기화
        entry_email_domain_en.delete(0, tk.END)  # 이메일 domain 부분 초기화
    elif frame == frame_blood_measure:
        for entry in entries.values():
            entry.delete(0, tk.END)  # 혈액 측정 값 초기화
    elif frame == frame_physical_measurements:
        for entry in entry_widgets.values():
            entry.delete(0, tk.END)

def save_phone_number_and_switch():
    global phone_number
    prefix = combo_prefix.get()
    user_input = entry_phone.get()
    
    if prefix == "" or user_input == "":
        messagebox.showerror("오류", "앞자리와 뒷자리 모두 입력하세요.")
        return
    
    if len(user_input) == 8 and user_input.isdigit():
        phone_number = prefix + user_input
        switch_to_frame(frame3)  # 검사 시작 후 화면으로 전환
        print(f"저장된 전화번호: {phone_number}")  # Debugging 용
    else:
        messagebox.showerror("오류", "뒷자리를 숫자 8자리로 입력하세요.")

def validate_email(email):
    # 이메일 domain 부분에 .이 포함되어 있는지 확인
    local_part, domain_part = email.split('@')
    
    if any('\u1100' <= char <= '\u11FF' or  # Hangul Jamo
           '\u3130' <= char <= '\u318F' or  # Hangul Compatibility Jamo
           '\uAC00' <= char <= '\uD7A3' for char in local_part):  # Hangul Syllables
        return False
    if any('\u1100' <= char <= '\u11FF' or  # Hangul Jamo
           '\u3130' <= char <= '\u318F' or  # Hangul Compatibility Jamo
           '\uAC00' <= char <= '\uD7A3' for char in domain_part):  # Hangul Syllables
        return False
    
    if '.' not in domain_part:
        return False
    return True

def save_email_address_and_switch():
    global email_address
    local_part = entry_email_local.get().strip()
    domain_part = entry_email_domain.get().strip()
    
    if local_part == "" or domain_part == "":
        messagebox.showerror("오류", "이메일을 모두 입력하세요.")
        return
    
    # 한글이 포함되어 있으면 오류 표시
    if any('\u1100' <= char <= '\u11FF' or  # Hangul Jamo
           '\u3130' <= char <= '\u318F' or  # Hangul Compatibility Jamo
           '\uAC00' <= char <= '\uD7A3' for char in local_part):  # Hangul Syllables
        messagebox.showerror("오류", "올바른 이메일 형식이 아닙니다.")
        return
    
    full_email = f"{local_part}@{domain_part}"
    
    if not validate_email(full_email):
        messagebox.showerror("오류", "올바른 이메일 형식이 아닙니다.")
        return
    
    email_address = full_email
    print(f"저장된 이메일: {email_address}")  # Debugging 용
    switch_to_frame(frame3)  # 검사 시작 후 화면으로 전환

def validate_en_email(email):
    # 이메일 domain 부분에 .이 포함되어 있는지 확인
    local_part, domain_part = email.split('@')
    
    # local_part에 한글 자음부터 초성, 중성, 종성까지 포함되어 있는지 확인
    if any('\u1100' <= char <= '\u11FF' or  # Hangul Jamo
           '\u3130' <= char <= '\u318F' or  # Hangul Compatibility Jamo
           '\uAC00' <= char <= '\uD7A3' for char in local_part):  # Hangul Syllables
        return False

    # local_part에 한글 자음부터 초성, 중성, 종성까지 포함되어 있는지 확인
    if any('\u1100' <= char <= '\u11FF' or  # Hangul Jamo
           '\u3130' <= char <= '\u318F' or  # Hangul Compatibility Jamo
           '\uAC00' <= char <= '\uD7A3' for char in domain_part):  # Hangul Syllables
        return False
    
    # domain_part에는 . 이외의 한글 문자가 포함되어 있는지 확인
    if any('\uAC00' <= char <= '\uD7A3' for char in domain_part) or '.' not in domain_part:
        return False
    return True

def save_email_address_and_switch_en():
    global email_address
    local_part = entry_email_local_en.get().strip()
    domain_part = entry_email_domain_en.get().strip()
    
    if local_part == "" or domain_part == "":
        messagebox.showerror("Error", "Please enter all your emails.")
        return
    
    # 한글이 포함되어 있으면 오류 표시
    if any('\u1100' <= char <= '\u11FF' or  # Hangul Jamo
           '\u3130' <= char <= '\u318F' or  # Hangul Compatibility Jamo
           '\uAC00' <= char <= '\uD7A3' for char in local_part):  # Hangul Syllables
        messagebox.showerror("Error", "This is not a valid email format.")
        return
    if any('\u1100' <= char <= '\u11FF' or  # Hangul Jamo
           '\u3130' <= char <= '\u318F' or  # Hangul Compatibility Jamo
           '\uAC00' <= char <= '\uD7A3' for char in domain_part):  # Hangul Syllables
        messagebox.showerror("Error", "This is not a valid email format.")
        return
    
    full_email = f"{local_part}@{domain_part}"
    
    if not validate_en_email(full_email):
        messagebox.showerror("Error", "This is not a valid email format.")
        return
    
    email_address = full_email
    print(f"saved e-mail: {email_address}")  # Debugging 용
    switch_to_frame(frame3)  # 검사 시작 후 화면으로 전환

def create_keypad(frame):
    keypad_frame = tk.Frame(frame)
    keypad_frame.pack(pady=10)
    buttons = [
        '1', '2', '3',
        '4', '5', '6',
        '7', '8', '9',
        '0', '←'  # 추가: 지우기 버튼
    ]
    row, col = 0, 0
    for button in buttons:
        if button == '←':
            tk.Button(keypad_frame, text=button, font=custom_font1, command=lambda: entry_phone.delete(len(entry_phone.get())-1), height=1, width=4).grid(row=row, column=col, padx=5, pady=5)
        else:
            tk.Button(keypad_frame, text=button, font=custom_font1, command=lambda b=button: entry_phone.insert(tk.END, b), height=1, width=4).grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 2:
            col = 0
            row += 1

def validate_entry(entry):
    """
    입력이 숫자와 '.'만 허용되도록 제한하는 함수
    """
    current_text = entry.get()
    filtered_text = ''.join(char for char in current_text if char.isdigit() or char == '.')
    if current_text != filtered_text:
        entry.delete(0, tk.END)
        entry.insert(tk.END, filtered_text)
    activate_results_button()

def activate_results_button():
    """
    결과보기 버튼을 활성화하고, 모든 입력이 올바르면 결과 화면으로 전환하는 함수
    """
    for text in labels_texts:
        entry = entry_widgets[text]
        if isinstance(entry, ttk.Combobox):
            if not entry.get():
                button_show_results.config(state=tk.DISABLED)
                return
        else:
            if not entry.get():
                button_show_results.config(state=tk.DISABLED)
                return
    button_show_results.config(state=tk.NORMAL)

def show_exit_confirmation():
    if messagebox.askyesno("종료 확인", "정말 종료하시겠습니까?"):
        root.destroy()

# 이미지 파일 로드
img_kr = tk.PhotoImage(file='kr.png')
img_en = tk.PhotoImage(file='en.png')
img_jp = tk.PhotoImage(file='jp.png')
img_ch = tk.PhotoImage(file='ch.png')

# 첫 번째 화면 버튼들 (2행 2열 정사각형 버튼)
button_kr = tk.Button(frame1, text="한국어", height=150, width=150, font=custom_font1, image=img_kr, compound="top", padx=5, pady=9, command=lambda: on_click(button_kr, switch_frame=lambda: switch_to_frame(frame2)))
button_kr.place(x=25, y=170, width=150, height=150)

button_en = tk.Button(frame1, text="English", height=150, width=150, font=custom_font1, image=img_en, compound="top", padx=5, pady=9, command=lambda: on_click(button_en, switch_frame=lambda: switch_to_frame(frame_en)))
button_en.place(x=175, y=170, width=150, height=150)

button_jp = tk.Button(frame1, text="日本語", height=150, width=150, font=custom_font1, image=img_jp, compound="top", padx=5, pady=9, command=lambda: on_click(button_jp))
button_jp.place(x=25, y=330, width=150, height=150)

button_ch = tk.Button(frame1, text="中国人", height=150, width=150, font=custom_font1, image=img_ch, compound="top", padx=5, pady=9, command=lambda: on_click(button_ch))
button_ch.place(x=175, y=330, width=150, height=150)

# 두 번째 화면 내용 (전화번호 또는 이메일 선택)
label2 = tk.Label(frame2, text="결과를 받을 방법을 선택해주세요.", font=custom_font2)
label2.pack(pady=25)

button_phone = tk.Button(frame2, text="전화번호", height=4, width=18, font=custom_font1, command=lambda: on_click(button_phone, switch_frame=lambda: switch_to_frame(frame_phone)))
button_phone.pack(pady=15)

button_email = tk.Button(frame2, text="이메일", height=4, width=18, font=custom_font1, command=lambda: on_click(button_email, switch_frame=lambda: switch_to_frame(frame_email)))
button_email.pack(pady=17)

button_back2 = tk.Button(frame2, text="뒤로가기", height=1, width=10, font=custom_font2, command=lambda: on_click(button_back2, switch_frame=lambda: switch_to_frame(frame1)))
button_back2.pack(pady=15)

# 세 번째 화면 내용 (전화번호 입력)
label_phone = tk.Label(frame_phone, text="전화번호를 입력하세요.", font=custom_font2)
label_phone.pack(pady=20)

# 프레임 생성 및 배치
frame_phone_input = tk.Frame(frame_phone)
frame_phone_input.pack(pady=5)

# 콤보 상자 (전화번호 prefix 선택)
combo_prefix = ttk.Combobox(frame_phone_input, values=['010', '011', '016', '018', '019'], state="readonly", font=custom_font2, width=4)
combo_prefix.pack(side=tk.LEFT, padx=(0, 5))
combo_prefix.configure(width=4)

entry_phone = tk.Entry(frame_phone_input, font=custom_font2, width=12)
entry_phone.pack(side=tk.LEFT)
entry_phone.configure(width=13)

create_keypad(frame_phone)

button_back_phone = tk.Button(frame_phone, text="뒤로가기", height=1, width=10, font=custom_font2, command=lambda: on_click(button_back_phone, switch_frame=lambda: switch_to_frame(frame2)))
button_back_phone.pack(pady=16)

button_start_phone = tk.Button(frame_phone, text="검사 시작", height=1, width=10, font=custom_font2, command=lambda: [on_click(button_start_phone), save_phone_number_and_switch()])
button_start_phone.pack(pady=5)

# 네 번째 화면 내용 (이메일 입력)
label_email = tk.Label(frame_email, text="이메일을 입력하세요.", font=custom_font2)
label_email.pack(pady=20)

# 이메일 도메인 선택을 위한 프레임과 콤보 상자
frame_email_suffix = tk.Frame(frame_email)

entry_email_local = tk.Entry(frame_email, font=custom_font2)
entry_email_local.pack(pady=5)

label_at = tk.Label(frame_email, text='@', font=custom_font2)
label_at.pack(pady=10)

entry_email_domain = tk.Entry(frame_email_suffix, font=custom_font2, width=15)
entry_email_domain.pack(side=tk.LEFT, padx=(0, 5))

combo_email_domain = ttk.Combobox(frame_email_suffix, values=['직접 입력', 'naver.com', 'gmail.com', 'daum.net', 'kakao.com', 'nate.com', 'yahoo.com'], state="readonly", font=custom_font2, width=10)
combo_email_domain.current(0)  # 초기 선택은 '직접 입력'
combo_email_domain.pack(side=tk.LEFT)

def handle_email_domain_selection(event):
    selected_domain = combo_email_domain.get()
    if selected_domain == '직접 입력':
        entry_email_domain.config(state=tk.NORMAL)
        entry_email_domain.delete(0, tk.END)
        entry_email_domain.focus_set()
    else:
        entry_email_domain.config(state=tk.NORMAL)
        entry_email_domain.delete(0, tk.END)
        entry_email_domain.insert(tk.END, selected_domain)
        entry_email_domain.config(state=tk.DISABLED)

combo_email_domain.bind('<<ComboboxSelected>>', handle_email_domain_selection)

frame_email_suffix.pack(pady=5)

button_back_email = tk.Button(frame_email, text="뒤로가기", height=1, width=10, font=custom_font2, command=lambda: on_click(button_back_email, switch_frame=lambda: switch_to_frame(frame2)))
button_back_email.pack(pady=13)

button_start_email = tk.Button(frame_email, text="검사 시작", height=1, width=10, font=custom_font2, command=lambda: [on_click(button_start_email), save_email_address_and_switch()])
button_start_email.pack(pady=13)

# 다섯 번째 화면 내용 (검사 시작 후 화면)
buttons_frame = tk.Frame(frame3)
buttons_frame.pack(pady=10)  # 버튼들을 아래로 내리기 위해 패딩 추가

buttons_9 = ['01\n얼굴', '02\n신체', '03\n피부', '04\n눈', '05\n걸음걸이', '06\n수면', '07\n신체 측정', '08\n혈액 측정', '결과지']
for i, button_text in enumerate(buttons_9):
    if button_text == '07\n신체 측정':
        tk.Button(buttons_frame, text=button_text, font=custom_font2, height=6, width=8, command=lambda: switch_to_frame(frame_physical_measurements)).grid(row=i//3, column=i%3, padx=3, pady=5)
    elif button_text == '08\n혈액 측정':
        tk.Button(buttons_frame, text=button_text, font=custom_font2, height=6, width=8, command=lambda: switch_to_frame(frame_blood_measure)).grid(row=i//3, column=i%3, padx=3, pady=5)
    elif button_text == '01\n얼굴':
        tk.Button(buttons_frame, text=button_text, font=custom_font2, height=6, width=8, command=lambda: switch_to_frame(frame01)).grid(row=i//3, column=i%3, padx=3, pady=5)
    elif button_text == '02\n신체':
        tk.Button(buttons_frame, text=button_text, font=custom_font2, height=6, width=8, command=lambda: switch_to_frame(frame02)).grid(row=i//3, column=i%3, padx=3, pady=5)
    elif button_text == '03\n피부':
        tk.Button(buttons_frame, text=button_text, font=custom_font2, height=6, width=8, command=lambda: switch_to_frame(frame03)).grid(row=i//3, column=i%3, padx=3, pady=5)
    elif button_text == '04\n눈':
        tk.Button(buttons_frame, text=button_text, font=custom_font2, height=6, width=8, command=lambda: switch_to_frame(frame04)).grid(row=i//3, column=i%3, padx=3, pady=5)
    elif button_text == '05\n걸음걸이':
        tk.Button(buttons_frame, text=button_text, font=custom_font2, height=6, width=8, command=lambda: switch_to_frame(frame05)).grid(row=i//3, column=i%3, padx=3, pady=5)
    elif button_text == '06\n수면':
        tk.Button(buttons_frame, text=button_text, font=custom_font2, height=6, width=8, command=lambda: switch_to_frame(frame06)).grid(row=i//3, column=i%3, padx=3, pady=5)
    elif button_text == '결과지':
        tk.Button(buttons_frame, text=button_text, font=custom_font2, height=6, width=8, command=lambda: switch_to_frame(report)) .grid(row=i//3, column=i%3, padx=3, pady=5)
    else:
        tk.Button(buttons_frame, text=button_text, font=custom_font2, height=6, width=8) .grid(row=i//3, column=i%3, padx=3, pady=5)

# 여섯 번째 화면 내용 (신체 측정 화면)
label_measurements = tk.Label(frame_physical_measurements, text="신체 측정 정보를 입력하세요.", font=custom_font2)
label_measurements.pack(pady=10)

labels_texts = [
    "나이", "성별", "키 (cm)", "체중 (kg)", "체지량지수 (BMI)", "체지방 (Kg)", 
    "체지방률 (%)", "심장박동수 (bpm)", "허리둘레 (cm)", "골반과 허리둘레 (WHR)", 
    "근육량 (kg)", "수축기 혈압 (SBP)", "이완기 혈압 (DBP)"
]

entry_widgets = {}

for text in labels_texts:
    frame = tk.Frame(frame_physical_measurements)
    frame.pack(pady=5, fill=tk.X)
    label = tk.Label(frame, text=text, font=custom_font3)
    label.pack(side=tk.LEFT, padx=(10, 5), fill=tk.X)

    if text == "성별":
        combo_gender = ttk.Combobox(frame, values=['남', '여'], state="readonly", font=custom_font3, width=4)
        combo_gender.pack(side=tk.LEFT, padx=(0, 10))
        entry_widgets[text] = combo_gender
    else:
        entry = tk.Entry(frame, font=custom_font3)
        entry.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X)
        entry.bind('<KeyRelease>', lambda event, entry=entry: validate_entry(entry))
        entry_widgets[text] = entry

button_back_measurements = tk.Button(frame_physical_measurements, text="뒤로가기", height=1, width=10, font=custom_font2, command=lambda: switch_to_frame(frame3))
button_back_measurements.pack(side=tk.LEFT, padx=(30, 30))

button_show_results = tk.Button(frame_physical_measurements, text="결과보기", height=1, width=10, font=custom_font2, state=tk.DISABLED, command=lambda: switch_to_frame(result_frame))
button_show_results.pack(side=tk.LEFT, padx=(0, 10))

# 일곱 번째 화면 내용 (신체 측정 결과 보기 화면)
label_result_title = tk.Label(result_frame, text="신체 측정 결과입니다.", font=custom_font2)
label_result_title.pack(pady=20)

recommendations = [
    "고혈압이 어쩌구저쩌구",
    "비만 위험해요",
    "키에 비해 체중이 좀",
    "남자인지 여자인지",
    "심장박동 둥둥"
]

for recommendation in recommendations:
    tk.Label(result_frame, text=recommendation, font=custom_font2).pack(pady=5)

# '검사 재선택' 버튼
button_back_body = tk.Button(result_frame, text="검사 재선택", height=1, width=10, font=custom_font2, command=lambda: on_click(button_back_body, switch_frame=lambda: switch_to_frame(frame3)))
button_back_body.pack(side=tk.LEFT, padx=(30, 15))

def send_results():
    confirmation_label = tk.Label(result_frame, text="결과 전송 완료", font=custom_font3, fg="blue")
    confirmation_label.pack(pady=5)

    button_x = button_send_result.winfo_x()
    button_y = button_send_result.winfo_y()
    button_width = button_send_result.winfo_width()
    label_width = confirmation_label.winfo_reqwidth()

    x_position = button_x + (button_width // 2) - (label_width // 2)
    y_position = button_y + button_send_result.winfo_height() + 10  # 간격을 10으로 조정

    confirmation_label.place(x=x_position, y=y_position)

# '결과 전송' 버튼
button_send_result = tk.Button(result_frame, text="결과 전송",  height=1, width=10, font=custom_font2, command=send_results)
button_send_result.pack(side=tk.LEFT, padx=(15, 30))

# 아홉 번째 화면 내용 (혈액 측정 화면)
label_blood = tk.Label(frame_blood_measure, text="혈액 측정 정보를 입력하세요.", font=custom_font2)
label_blood.pack(pady=20)

# 혈액 측정 항목 추가
blood_tests = [
    "저밀도콜레스테롤(LDL)", "고밀도콜레스테롤(HDL)", "중성지방(TG)",
    "알라닌아미노전이효소(ALT)", "헤모글로빈(Hb)", "갑상선자극호르몬(TSH)",
    "공복혈당(FG)", "식후2시간혈당(PPG)"
]

entries = {}

def validate_numeric_input(event, entry):
    value = entry.get()
    if not value.replace('.', '', 1).isdigit():  # '.'을 제외한 나머지 문자가 숫자인지 확인
        entry.delete(0, tk.END)

def activate_view_results_button():
    for test, entry in entries.items():
        if not entry.get():
            button_view_results.config(state=tk.DISABLED)
            return
    button_view_results.config(state=tk.NORMAL)

for test in blood_tests:
    frame = tk.Frame(frame_blood_measure)
    frame.pack(pady=5, fill=tk.X)
    label = tk.Label(frame, text=test, font=custom_font3)
    label.pack(side=tk.LEFT, padx=(10, 5), fill=tk.X)
    
    entry = tk.Entry(frame, font=custom_font3)
    entry.pack(side=tk.LEFT, padx=(10, 0), fill=tk.X)
    entry.bind("<KeyRelease>", lambda event, e=entry: [validate_numeric_input(event, e), activate_view_results_button()])
    entries[test] = entry

button_back_blood = tk.Button(frame_blood_measure, text="뒤로가기", height=1, width=10, font=custom_font2, command=lambda: [on_click(button_back_blood, switch_frame=lambda: switch_to_frame(frame3))])
button_back_blood.pack(side=tk.LEFT, padx=(30, 30))

button_view_results = tk.Button(frame_blood_measure, text="결과보기", height=1, width=10, font=custom_font2, state=tk.DISABLED, command=lambda: switch_to_frame(frame_results))
button_view_results.pack(side=tk.LEFT, padx=(0, 10))

# 열 번째 화면 내용 (혈액 측정 결과 보기 화면)
label_results = tk.Label(frame_results, text=" 혈액 측정 결과입니다.", font=custom_font2)
label_results.pack(pady=20)

recommend = [
    "혈액이 이상해요",
    "공복혈당이 와우 넘 높아요",
    "집 가고 싶어요",
    "측정이 이러쿵저렁쿵",
    "이거는 어찌고저찌고"
]

for recommendation in recommend:
    tk.Label(frame_results, text=recommendation, font=custom_font2).pack(pady=5)

button_back_results = tk.Button(frame_results, text="검사 재선택", height=1, width=10, font=custom_font2, command=lambda: on_click(button_back_results, switch_frame=lambda: switch_to_frame(frame3)))
button_back_results.pack(side=tk.LEFT, padx=(30, 15))

def send_results():
    confirmation_label = tk.Label(frame_results, text="결과 전송 완료", font=custom_font3, fg="blue")
    confirmation_label.pack(pady=5)

    button_x = button_send_results.winfo_x()
    button_y = button_send_results.winfo_y()
    button_width = button_send_results.winfo_width()
    label_width = confirmation_label.winfo_reqwidth()

    x_position = button_x + (button_width // 2) - (label_width // 2)
    y_position = button_y + button_send_results.winfo_height() + 10  # 간격을 10으로 조정

    confirmation_label.place(x=x_position, y=y_position)
    
button_send_results = tk.Button(frame_results, text="결과 전송", height=1, width=10, font=custom_font2, command=send_results)
button_send_results.pack(side=tk.LEFT, padx=(15, 30))

# 열두 번째 화면 내용 (01 Face)
label01 = tk.Label(frame01, text="얼굴 결과입니다.", font=custom_font2)
label01.pack(pady=20)

button_back_01 = tk.Button(frame01, text="검사 재선택", height=1, width=10, font=custom_font2, command=lambda: switch_to_frame(frame3))
button_back_01.pack(side=tk.LEFT, padx=(30, 15))

def send_results_01():
    confirmation_label = tk.Label(frame01, text="결과 전송 완료", font=custom_font3, fg="blue")
    confirmation_label.pack(pady=5)

    button_x = button_send_01.winfo_x()
    button_y = button_send_01.winfo_y()
    button_width = button_send_01.winfo_width()
    label_width = confirmation_label.winfo_reqwidth()

    x_position = button_x + (button_width // 2) - (label_width // 2)
    y_position = button_y + button_send_01.winfo_height() + 10  # 간격을 10으로 조정

    confirmation_label.place(x=x_position, y=y_position)

button_send_01 = tk.Button(frame01, text="결과 전송", height=1, width=10, font=custom_font2, command=send_results_01)
button_send_01.pack(side=tk.LEFT, padx=(15, 30))

button_exit_01 = tk.Button(frame01, text="종료", font=custom_font2, command=lambda: on_click(button_exit_01, show_exit_confirmation))
button_exit_01.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# 열세 번째 화면 내용 (02 Body)
label02 = tk.Label(frame02, text="신체 결과입니다.", font=custom_font2)
label02.pack(pady=20)

button_back_02 = tk.Button(frame02, text="검사 재선택", height=1, width=10, font=custom_font2, command=lambda: switch_to_frame(frame3))
button_back_02.pack(side=tk.LEFT, padx=(30, 15))

def send_results_02():
    confirmation_label = tk.Label(frame02, text="결과 전송 완료", font=custom_font3, fg="blue")
    confirmation_label.pack(pady=5)

    button_x = button_send_02.winfo_x()
    button_y = button_send_02.winfo_y()
    button_width = button_send_02.winfo_width()
    label_width = confirmation_label.winfo_reqwidth()

    x_position = button_x + (button_width // 2) - (label_width // 2)
    y_position = button_y + button_send_02.winfo_height() + 10  # 간격을 10으로 조정

    confirmation_label.place(x=x_position, y=y_position)

button_send_02 = tk.Button(frame02, text="결과 전송", height=1, width=10, font=custom_font2, command=send_results_02)
button_send_02.pack(side=tk.LEFT, padx=(15, 30))

button_exit_02 = tk.Button(frame02, text="종료", font=custom_font2, command=lambda: on_click(button_exit_02, show_exit_confirmation))
button_exit_02.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# 열네 번째 화면 내용 (03 Skin)
label03 = tk.Label(frame03, text="피부 결과입니다.", font=custom_font2)
label03.pack(pady=20)

button_back_03 = tk.Button(frame03, text="검사 재선택", height=1, width=10, font=custom_font2, command=lambda: switch_to_frame(frame3))
button_back_03.pack(side=tk.LEFT, padx=(30, 15))

def send_results_03():
    confirmation_label = tk.Label(frame03, text="결과 전송 완료", font=custom_font3, fg="blue")
    confirmation_label.pack(pady=5)

    button_x = button_send_03.winfo_x()
    button_y = button_send_03.winfo_y()
    button_width = button_send_03.winfo_width()
    label_width = confirmation_label.winfo_reqwidth()

    x_position = button_x + (button_width // 2) - (label_width // 2)
    y_position = button_y + button_send_03.winfo_height() + 10  # 간격을 10으로 조정

    confirmation_label.place(x=x_position, y=y_position)

button_send_03 = tk.Button(frame03, text="결과 전송", height=1, width=10, font=custom_font2, command=send_results_03)
button_send_03.pack(side=tk.LEFT, padx=(15, 30))

button_exit_03 = tk.Button(frame03, text="종료", font=custom_font2, command=lambda: on_click(button_exit_03, show_exit_confirmation))
button_exit_03.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# 열다섯 번째 화면 내용 (04 Eye)
label04 = tk.Label(frame04, text="눈 결과입니다.", font=custom_font2)
label04.pack(pady=20)

button_back_04 = tk.Button(frame04, text="검사 재선택", height=1, width=10, font=custom_font2, command=lambda: switch_to_frame(frame3))
button_back_04.pack(side=tk.LEFT, padx=(30, 15))

def send_results_04():
    confirmation_label = tk.Label(frame04, text="결과 전송 완료", font=custom_font3, fg="blue")
    confirmation_label.pack(pady=5)

    button_x = button_send_04.winfo_x()
    button_y = button_send_04.winfo_y()
    button_width = button_send_04.winfo_width()
    label_width = confirmation_label.winfo_reqwidth()

    x_position = button_x + (button_width // 2) - (label_width // 2)
    y_position = button_y + button_send_04.winfo_height() + 10  # 간격을 10으로 조정

    confirmation_label.place(x=x_position, y=y_position)

button_send_04 = tk.Button(frame04, text="결과 전송", height=1, width=10, font=custom_font2, command=send_results_04)
button_send_04.pack(side=tk.LEFT, padx=(15, 30))

button_exit_04 = tk.Button(frame04, text="종료", font=custom_font2, command=lambda: on_click(button_exit_04, show_exit_confirmation))
button_exit_04.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# 열여섯 번째 화면 내용 (05 Gait)
label05 = tk.Label(frame05, text="걸음걸이 결과입니다.", font=custom_font2)
label05.pack(pady=20)

button_back_05 = tk.Button(frame05, text="검사 재선택", height=1, width=10, font=custom_font2, command=lambda: switch_to_frame(frame3))
button_back_05.pack(side=tk.LEFT, padx=(30, 15))

def send_results_05():
    confirmation_label = tk.Label(frame05, text="결과 전송 완료", font=custom_font3, fg="blue")
    confirmation_label.pack(pady=5)

    button_x = button_send_05.winfo_x()
    button_y = button_send_05.winfo_y()
    button_width = button_send_05.winfo_width()
    label_width = confirmation_label.winfo_reqwidth()

    x_position = button_x + (button_width // 2) - (label_width // 2)
    y_position = button_y + button_send_05.winfo_height() + 10  # 간격을 10으로 조정

    confirmation_label.place(x=x_position, y=y_position)

button_send_05 = tk.Button(frame05, text="결과 전송", height=1, width=10, font=custom_font2, command=send_results_05)
button_send_05.pack(side=tk.LEFT, padx=(15, 30))

button_exit_05 = tk.Button(frame05, text="종료", font=custom_font2, command=lambda: on_click(button_exit_05, show_exit_confirmation))
button_exit_05.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# 열일곱 번째 화면 내용 (06 Sleeping)
label06 = tk.Label(frame06, text="수면 결과입니다.", font=custom_font2)
label06.pack(pady=20)

button_back_06 = tk.Button(frame06, text="검사 재선택", height=1, width=10, font=custom_font2, command=lambda: switch_to_frame(frame3))
button_back_06.pack(side=tk.LEFT, padx=(30, 15))

def send_results_06():
    confirmation_label = tk.Label(frame06, text="결과 전송 완료", font=custom_font3, fg="blue")
    confirmation_label.pack(pady=5)

    button_x = button_send_06.winfo_x()
    button_y = button_send_06.winfo_y()
    button_width = button_send_06.winfo_width()
    label_width = confirmation_label.winfo_reqwidth()

    x_position = button_x + (button_width // 2) - (label_width // 2)
    y_position = button_y + button_send_06.winfo_height() + 10  # 간격을 10으로 조정

    confirmation_label.place(x=x_position, y=y_position)

button_send_06 = tk.Button(frame06, text="결과 전송", height=1, width=10, font=custom_font2, command=send_results_06)
button_send_06.pack(side=tk.LEFT, padx=(15, 30))

button_exit_06 = tk.Button(frame06, text="종료", font=custom_font2, command=lambda: on_click(button_exit_06, show_exit_confirmation))
button_exit_06.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# 열여덟 번째 화면 내용 (Tel or Email 선택)
label18 = tk.Label(frame_en, text="Choose a way to get results.", font=custom_font2)
label18.pack(pady=25)

button_phone_en = tk.Button(frame_en, text="a telephone number", height=4, width=18, font=custom_font1, command=lambda: on_click(button_phone, switch_frame=lambda: switch_to_frame(frame_en_phone)))
button_phone_en.pack(pady=15)

button_email_en = tk.Button(frame_en, text="E-mail", height=4, width=18, font=custom_font1, command=lambda: on_click(button_email, switch_frame=lambda: switch_to_frame(frame_en_email)))
button_email_en.pack(pady=17)

button_back18 = tk.Button(frame_en, text="back", height=1, width=10, font=custom_font2, command=lambda: on_click(button_back2, switch_frame=lambda: switch_to_frame(frame1)))
button_back18.pack(pady=15)

# 열아홉 번째 화면 내용 (Tel)

# 스무 번째 화면 내용 (Email)
label_en_email = tk.Label(frame_en_email, text="이메일을 입력하세요.", font=custom_font2)
label_en_email.pack(pady=20)

# 이메일 도메인 선택을 위한 프레임과 콤보 상자
frame_email_suffix_en = tk.Frame(frame_en_email)

entry_email_local_en = tk.Entry(frame_en_email, font=custom_font2)
entry_email_local_en.pack(pady=5)

label_at_en = tk.Label(frame_en_email, text='@', font=custom_font2)
label_at_en.pack(pady=10)

entry_email_domain_en = tk.Entry(frame_email_suffix_en, font=custom_font2, width=15)
entry_email_domain_en.pack(side=tk.LEFT, padx=(0, 5))

combo_email_domain_en = ttk.Combobox(frame_email_suffix_en, values=['직접 입력', 'aol.com', 'gmail.com', 'hotmail.com', 'icloud.com', 'yahoo.com', 'zoho.com'], state="readonly", font=custom_font2, width=10)
combo_email_domain_en.current(0)  # 초기 선택은 '직접 입력'
combo_email_domain_en.pack(side=tk.LEFT)

def handle_email_domain_selection(event):
    selected_domain = combo_email_domain_en.get()
    if selected_domain == '직접 입력':
        entry_email_domain_en.config(state=tk.NORMAL)
        entry_email_domain_en.delete(0, tk.END)
        entry_email_domain_en.focus_set()
    else:
        entry_email_domain_en.config(state=tk.NORMAL)
        entry_email_domain_en.delete(0, tk.END)
        entry_email_domain_en.insert(tk.END, selected_domain)
        entry_email_domain_en.config(state=tk.DISABLED)

combo_email_domain_en.bind('<<ComboboxSelected>>', handle_email_domain_selection)

frame_email_suffix_en.pack(pady=5)

button_back_en_email = tk.Button(frame_en_email, text="back", height=1, width=14, font=custom_font2, command=lambda: on_click(button_back_en_email, switch_frame=lambda: switch_to_frame(frame_en)))
button_back_en_email.pack(pady=13)

button_start_en_email = tk.Button(frame_en_email, text="Start inspection", height=1, width=14, font=custom_font2, command=lambda: [on_click(button_start_en_email), save_email_address_and_switch_en()])
button_start_en_email.pack(pady=13)

# 스물한 번째 화면 내용 (결과지)
result_07_08 = tk.Label(report, text="07 08 결과입니다.", font=custom_font2)
result_07_08.pack(pady=20)

recommend_07_08 = tk.Label(report, text="추천 문구입니다.", font=custom_font2)
recommend_07_08.pack(pady=60)

report_back = tk.Button(report, text="뒤로가기", height=1, width=10, font=custom_font2, command=lambda: switch_to_frame(frame3))
report_back.pack(side=tk.LEFT, padx=(30, 15))

# 종료 버튼
button_exit = tk.Button(report, text="종료", font=custom_font2, command=lambda: on_click(button_exit, show_exit_confirmation))
button_exit.pack(side=tk.LEFT, padx=(15, 30))

root.mainloop()
