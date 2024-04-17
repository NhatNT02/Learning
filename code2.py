# #Câu lệnh cơ bản
# print("Hello world")
# a = 3
# b = 6
# print(a+b)

# #Thao tác nhập, xử lý, xuất dữ liệu cơ bản
# a = input("Nhập vào a: ")
# b = int(a) + 2
# print(b)

# #Sử dụng sep để ngăn cách các đoạn dữ liệu nhập vào
# print("xin", "chào", "mọi", "người", sep=", ")
# #Sử dụng end để nối các đoạn dữ liệu nhập vào trên các dòng lệnh khác nhau
# print("xin", "chào", end=": ")
# print("mọi người")

# print("Tên={0},Họ={1}".format("Nhật", "Nguyễn"))

# #Ví dụ về ép kiểu dữ liệu
# n = 100
# m = "200"
# print(str(n)+m)
# print(n+int(m))

# #Ví dụ về câu lệnh if/else
# x = input("Nhập số nguyên x: ")
# x = int(x)
# if x%2 == 0:
#     print("{0} {1}".format(x, "là số chẵn"))
# elif x%2 == 1:
#     print(x, "là số lẻ")
# else:
#     print(x, "không là số chẵn cũng không là số lẻ")


# #Giải phương trình bậc 2
# import math

# a = float(input("Nhập a: "))
# b = float(input("Nhập b: "))
# c = float(input("Nhập c: "))
# if b < 0 and c > 0:
#     print("Giải phương trình: {0}x^2-{1}x+{2}=0".format(a, -b, c))
# elif b > 0 and c < 0:
#     print("Giải phương trình: {0}x^2+{1}x-{2}=0".format(a, b, -c))
# elif b < 0 and c < 0:
#     print("Giải phương trình: {0}x^2-{1}x-{2}=0".format(a, -b, -c))
# else:
#     print("Giải phương trình: {0}x^2+{1}x+{2}=0".format(a, b, c))

# if a != 0:
#     delta = b**2 - 4*a*c
#     if delta < 0:
#         print("Phương trình vô nghiệm")
#     elif delta == 0:
#         x = -b/(2*a)
#         print("Phương trình có nghiệm kép x1 = x2 = ", x)
#     else:
#         x1 = (-b+math.sqrt(delta))/(2*a)
#         x2 = (-b-math.sqrt(delta))/(2*a)
#         print("Phương trình có hai nghiệm phân biệt x1 = {0} và x2 = {1}".format(x1, x2))
# else:
#     print("Không phải phương trình bậc 2")


# #Xác định tam giác, từ đó tính chu vi và diện tích của tam giác đó
# import math

# xA = float(input("Nhập xA: "))
# yA = float(input("Nhập yA: "))
# zA = float(input("Nhập zA: "))
# xB = float(input("Nhập xB: "))
# yB = float(input("Nhập yB: "))
# zB = float(input("Nhập zB: "))
# xC = float(input("Nhập xC: "))
# yC = float(input("Nhập yC: "))
# zC = float(input("Nhập zC: "))
# print("Trong hệ trục tọa độ Oxyz, cho ba điểm A({0},{1},{2}), B({3},{4},{5}), C({6},{7},{8}). Nếu ba điểm này tạo thành một hình tam giác, hãy tính chu vi và diện tích của tam giác đó.".format(xA, yA, zA, xB, yB, zB, xC, yC, zC))

# AB = float(math.sqrt((xB-xA)**2+(yB-yA)**2+(zB-zA)**2))
# BC = float(math.sqrt((xC-xB)**2+(yC-yB)**2+(zC-zB)**2))
# CA = float(math.sqrt((xA-xC)**2+(yA-yC)**2+(zA-zC)**2))
# if AB<BC+CA and BC<CA+AB and CA<AB+BC:
#     print("Ba điểm A, B, C tạo thành một hình tam giác")
#     chuvi = float(AB+BC+CA)
#     p = float(chuvi/2)
#     dientich = float(math.sqrt(p*(p-AB)*(p-BC)*(p-CA)))
#     print("Chu vi của tam giác đó là ", chuvi)
#     print("Diện tích của tam giác đó là ", dientich)
# else:
#     print("Ba điểm A, B, C không tạo thành một hình tam giác")


# #Khởi tạo một list rỗng
# emptyList = []
# emptyList = list()
# #Tạo list có dữ liệu
# colors = ["red", "green", "orange"]
# print(colors)

# #Tạo list có thứ tự và thao tác cơ bản với list
# studentList = ["An", "Bình", "Chi", "Doanh"]
#  #Độ dài của list
# print(len(studentList))

#  #In ra phần tử cụ thể
# print(studentList[1])
# print(studentList[3])
#  #In ra toàn bộ phần tử của list
# print(studentList)
# print(studentList[:])
#  #In ra các phần tử trong khoảng giới hạn
# print(studentList[1:2])
# print(studentList[1:4])

#  #Thêm phần tử vào cuối list
# studentList.append("Hương")
# print(studentList)
# studentList[len(studentList):] = ["Bình"]
#  #Thêm phần tử vào vị trí cụ thể trong list
# studentList.insert(2, "Bảo")
# print(studentList)

#  #Đếm số lượng phần tử thỏa mãn điều kiện
# print(studentList.count("Bình"))
# print(studentList.count("Bảo"))

#  #Xóa phần tử cụ thể trong list
# studentList.remove("An")
# print(studentList)
#  #Xóa phần tử theo vị trí
# studentList.pop(0)
# print(studentList)

#  #Kiểm tra phần tử có trong list hay không: in/not in
# if "Bình" in studentList:
#     studentList.remove("Bình")
#     print(studentList)

#  #Đảo ngược list
# studentList.reverse()
# print(studentList)

#  #Sắp xếp list(từ nhỏ đến lớn)
# studentList.sort()
# print(studentList)
#  #Sắp xếp list(từ lớn về nhỏ)
# studentList.sort(reverse=True)
# print(studentList)

#  #Xóa sạch dữ liệu trong list
# studentList.clear()
# print(studentList)


# #Vòng lặp for
#  #Vòng lặp từ 0 đến n-1
# n=10
# for i in range(n):
#     print(i)

#  #Tính tổng các số nguyên từ 0 đến n
# n = int(input("Nhập vào n: "))
# tong = 0
# for i in range(n+1):
#     tong += i
# print("Tổng các giá trị là:", tong)

#  #Vòng lặp for có bước nhảy
# for i in range(0, 10, 2):
#     print(i)
# for k in range(10, 0, -1):
#     print(k)

#  #Vòng lặp for duyệt các phần tử của list
# colors = ["red", "green", "blue", "yellow"]
# for color in colors:
#     print(color)

#  #Vòng lặp for duyệt phần tử theo vị trí
# for i in range(len(colors)):
#     print(colors[i])








