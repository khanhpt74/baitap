#- Xây dựng 1 vòng lặp không xác định thực hiện các việc sau:
#+ Hỏi người dùng có muốn tắt máy không? nếu có thì thực hiện tắt máy
# + Còn không thì đợi 30 giây sau mới hỏi lại câu hỏi ở trên. 
import os 
showdown = input("ban co muon tat may khong ? (co / khong): ")
if showdown == "no":
    exit()
else:
    os.system("showdown /s 30")   
