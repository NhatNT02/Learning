# #Kiểu dữ liệu String
# #Ví dụ về chuỗi
# s1 = "xin chào"
# s2 = "mọi người"
# s3 = s1 + " " + s2
# print(s3)

# #Tạo chuỗi nhiều dòng
# chuoi_nhieu_dong = '''
# Dòng 1
# Dòng 2
# Dòng 3
# '''
# print(chuoi_nhieu_dong)

# #Lặp lại chuỗi
# chep_bai = "điều phải chứng minh\n"
# chep_bai_10 = chep_bai*10
# print(chep_bai_10)

# #Kiểm tra chuỗi có thuộc chuỗi khác hay không
# chuoi_1 = "xin chào mọi người"
# chuoi_2 = "mọi người"
# chuoi_3 = "VN"
# if chuoi_2 in chuoi_1:
#     print("chuỗi 2 là chuỗi con của chuỗi 1")
# else:
#     print("chuỗi 2 không là con của chuỗi 1")
# if chuoi_3 in chuoi_1:
#     print("chuỗi 3 là chuỗi con của chuỗi 1")
# else:
#     print("chuỗi 3 không là chuỗi con của chuỗi 1")

# #Viết hoa chữ cái đầu của chuỗi
# s = "xin chào mọi người"
# s = str.capitalize(s)
# print(s)

# #Viết hoa toàn bộ chuỗi
# s = s.upper()
# print(s)

# #Viết thường toàn bộ chuỗi
# s = s.lower()
# print(s)

# #Tìm và đếm số lượng chuỗi con
# s = "Lập trình Python là xu hướng hiện nay. Bạn nên học lập trình Python."
# print(s.find("Python")) #Trả về giá trị -1 nếu không tìm thấy, ngược lại trả về vị trí đầu tiên
# print(s.count("Python")) #Trả về số lượng phần tử trong chuỗi 

# #Thay thế
# s = "Lập trình Python là xu hướng hiện nay. Bạn nên học lập trình Python."
# s = s.replace("Python", "PYTHON")
# print(s)

# #Cắt chuỗi thành một LIST    
# s = "Lập trình Python là xu hướng hiện nay. Bạn nên học lập trình Python."
# list1 = s.split(" ") #cắt các khoảng khi gặp dấu cách
# print(list1)
# list2 = s.split(".") #cắt các khoảng khi gặp dấu chấm
# print(list2)

# #Format
# print("{0} + {1} = {2}".format(1, 2, 1+2))

# #Lấy chuỗi con
# print(s[0:10])


# #Vòng lặp While
# #Ví dụ: Yêu cầu người dùng nhập vào một con số n>0. Nếu nhập sai thì yêu cầu người dùng nhập lại.
# n = -1
# while n<=0:
#     n = int(input("Nhập vào n: "))
# #Thao tác cơ bản
# i = 0
# tong = 0
# while i<=n:
#     tong += i
#     i += 1   
# print("Tong =", tong)

# j = 0
# while j<=10:
#     print(j, ": Bên trong vòng lặp")
#     j += 1
#     if j>=5:
#         break
# else:
#     print(j, ": Bên ngoài vòng lặp")

# #Bài tập chuyển từ hệ thập phân sang hệ nhị phân
# #Nhập n (n>0)
# n = -1
# while (n<=0):
#     n = int(input("Nhập vào n>0: "))
# #Chuyển từ thập phân sang nhị phân
# ketqua = ""
# while (n>0): #//:chia lấy phần nguyên, %:chia lấy phần dư
#     ketqua = str(n%2) + ketqua
#     print("n%2 =", n%2)
#     n = n//2
#     print("n =", n)
# print("Kết quả là:", ketqua)

# for i in range(0,10):
#     if i%2==1:
#         continue #bỏ qua phần còn lại khi tiếp tục nhận điều kiện đúng
#     print(i)


# #Kiểu dữ liệu Tuple
# #Ví dụ
# gioitinh = ("Nam", "Nữ")
# lophoc = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# traicay = ("Táo", "Chuối", "Táo", "Cam", "Mận", "Dưa hấu")

# #Lấy ra các phần tử
# print(gioitinh[0])
# print(traicay[0:2])
# print(lophoc[0])

# #In ra toàn bộ phần tử
# for x in traicay:
#     print(x)

# #Cộng hai Tuple
# y = (1,2,3) + (4,5,6)
# print(y)

# #Nhân hai Tuple
# y = (1,2,3)*2
# print(y)

# #Kiểm tra xem một phần từ có nằm trong Tuple hay không
# print("Táo" in traicay)

# #Lấy số lượng phần tử của Tuple
# x = len(traicay)
# print(x)

# #Đếm số lượt xuất hiện
# print(traicay.count("Táo"))

# #Tìm min, max và tính sum(chỉ áp dụng với Tuple là các số)
# print(min(gioitinh))
# print(max(traicay))
# print(sum(lophoc))

# #Sắp xếp Tuple và chuyển về List
# listTC = sorted(traicay)
# print(listTC)


# #Kiểu dữ liệu Set
# #Ví dụ
# monhoc = {"Toán", "Lý", "Hóa"}
# print(monhoc)

# #Duyệt các phần tử bên trong Set
# for x in monhoc:
#     print(x)

# #Thêm mới phần tử vào bên trong Set:
#  #Thêm 1 phần tử: add()
# monhoc.add("Lịch sử")
# print(monhoc) #Nếu cố thêm một phần tử "Lịch sử" nữa thì nó sẽ đè lên phần tử sẵn có
#  #Thêm một tập hợp khác hoặc một List khác: update()
# hocthem = {"Anh", "Guitar"}
# monhoc.update(hocthem)
# print(monhoc)

# Xóa phần tử:
#  remove(): nếu phần tử không tồn tại sẽ phát sinh lỗi 
#  discard(): nếu phần tử không tồn tại sẽ không phát sinh lỗi
#  pop(): loại bỏ phần tử cuối
#  clear(): làm rỗng tập hợp
#  del: xóa bỏ tập hợp

# Bài tập rút thăm trúng thưởng với các chức năng:
#  Thêm một số điện thoại dự thưởng vào thùng
#  Xóa một số điện thoại dự thưởng ra khỏi thùng
#  Quay số ngẫu nhiên lấy ra một số điện thoại trúng thưởng

# #Thư viện random
# import random
# #Khởi tạo set
# thungphieu = set() #Khởi tạo thungphieu = {} sẽ khiến hth hiểu nhầm là kiểu Dict
# #Vòng lặp
# while(True):
#     print("------MENU------")
#     print("Vui lòng lựa chọn chức năng: ")
#     print("1 - Thêm một số điện thoại dự thưởng")
#     print("2 - Xóa một số điện thoại dự thưởng")
#     print("3 - Quay số ngẫu nhiên một số điện thoại trúng thưởng")
#     print("4 - Kết thúc chương trình")
#     print("Thùng phiếu hiện tại:")
#     print(thungphieu)

#     luachon = int(input("Lựa chọn: "))

#     if(luachon == 1):
#         sdt = input("Nhập vào số điện thoại dự thưởng: ")
#         thungphieu.add(sdt)
#     elif(luachon == 2):
#         sdt = input("Nhập vào số điện thoại dự thưởng cần xóa: ")
#         thungphieu.discard(sdt)
#     elif(luachon == 3):
#         index = random.randint(0,len(thungphieu)-1)
#         print("Vị trí trúng thưởng " + str(index))
        
#         i = 0
#         for x in thungphieu:
#             if(i == index):
#                 break
#             i = i + 1
#         print("Chúc mừng SĐT: " + x + " đã trúng thưởng!")
#         thungphieu.discard(x)

#     else:
#         break

#     x = input("Nhập phím bất kỳ để tiếp tục")


# #Kiểu dữ liệu Dictionary
# #Ví dụ
# sinhvien = {
#     "hovaten" : "Nguyen Van A",
#     "malop" : "DH01",
#     "diemtrungbinh" : 8.5
# }
# print(sinhvien)
# print(sinhvien["hovaten"])

# #Sử dụng get() để lấy giá trị
# print(sinhvien.get("malop"))

# #Cập nhật giá trị
# sinhvien["malop"] = "DH02"
# print(sinhvien)

# sinhvien.update({"malop":"DH03","diemtrungbinh":8.6})
# print(sinhvien)

# #Thêm các mục mới: tương tự phần cập nhật giá trị nhưng với cặp key: value mới
# sinhvien["noisinh"] = "Ha Noi"
# print(sinhvien)

# sinhvien.update({"noisinh":"Ha Noi"})
# print(sinhvien)

# #Xóa mục
#  #pop(): loại bỏ mục có tên khóa được chỉ định
# sinhvien.pop("noisinh")
# print(sinhvien)

#  #popitem(): xóa mục được chèn cuối cùng
# sinhvien.popitem()
# print(sinhvien)

#  #del: lọai bỏ mục có tên khóa được chỉ định, hoặc toàn bộ từ điển
# del sinhvien["noisinh"] #Xóa mục chỉ định
# print(sinhvien)

# del sinhvien #Xóa toàn bộ từ điển
# print(sinhvien)

# #Clear: làm trống từ điển
# sinhvien.clear()
# print(sinhvien)

# #In tất cả các tên khóa
# for x in sinhvien:
#     print(x)

# #Duyệt các giá trị
# for x in sinhvien.values():
#     print(x)

# #Duyệt các khóa
# for x in sinhvien.keys():
#     print(x)

# #Duyệt các cặp khóa-giá trị:
# for x, y in sinhvien.items():
#     print(x, y)

# #Bài tập xây dựng chương trình tra từ điển Anh-Việt
# #với các chức năng như sau:
#  #Thêm một từ vựng mới (kèm nghĩa của từ vựng) vào từ điển
#  #Tra cứu ý nghĩa của một từ vựng
#  #Cập nhật ý nghĩa cho một từ vựng 
#  #Cho phép người dùng xóa đi một từ vựng
#  #Cho phép người dùng xóa đi toàn bộ từ vựng
#  #Cho phép người dùng in ra toàn bộ từ vựng
#  #Cho phép người dùng in ra toàn bộ từ điển theo cấu trúc: "TỪ VỰNG" : "Ý NGHĨA"
#  #Kết thúc chương trình

# #Khai báo từ điển
# tudien = {}

# while(True):
#     print("Vui lòng chọn chức năng (bằng số): ")
#     print("""
#         1.Thêm một từ vựng mới (kèm nghĩa của từ vựng) vào từ điển\n
#         2.Tra cứu ý nghĩa của một từ vựng\n
#         3.Cập nhật ý nghĩa cho một từ vựng\n
#         4.Cho phép người dùng xóa đi một từ vựng\n
#         5.Cho phép người dùng xóa đi toàn bộ từ vựng\n
#         6.Cho phép người dùng in ra toàn bộ từ vựng\n
#         7.Cho phép người dùng in ra toàn bộ từ điển theo cấu trúc: "TỪ VỰNG" : "Ý NGHĨA"\n
#         8.Kết thúc chương trình\n
#         """)
    
#     luachon = int(input("Nhập vào lựa chọn của bạn: "))

#     if (luachon == 1) or (luachon == 3):
#         tuvung = input("Nhập vào từ vựng: ")
#         ynghia = input("Nhập vào ý nghĩa: ")
#         tudien[tuvung] = ynghia
#         print("Đã thêm/cập nhật từ vựng!")

#     elif (luachon == 2):
#         tuvung = input("Nhập vào từ vựng: ")
#         print("Ý nghĩa:", tudien[tuvung])
    
#     elif (luachon == 4):
#         tuvung = input("Nhập vào từ vựng cần xóa: ")
#         tudien.pop(tuvung)
#         print("Đã xóa dữ liệu!")

#     elif (luachon == 5):
#         tudien.clear()
#         print("Đã xóa toàn bộ dữ liệu!")
        
#     elif (luachon == 6):
#         print("Danh sách các từ vựng có trong từ điển: ")
#         for x in tudien.keys():
#             print(x)

#     elif (luachon == 7):
#         print("Danh sách các từ vựng có trong từ điển: ")
#         for x, y in tudien.items():
#             print(x,":",y)
#     elif (luachon == 8):
#         break
#     else:
#         print("Nhập lựa chọn không đúng!")


# #Xây dựng Function
# #Ví dụ
# def xinchao(ho, tendem, ten):
#     print("Xin chào " + ho + tendem + ten)
# xinchao("Nguyễn", " Văn", " A")

# #Khi không xác định được số đối số, chúng ta có thể sử dụng dấu *
# def thoikhoabieu(*monhoc):
#     print("Môn 1: " + monhoc[0])
#     print("Môn 2: " + monhoc[1])
# thoikhoabieu("Toán", "Lý", "Hóa", "Văn", "Anh", "Sử")

# def tinhtong(*giatri):
#     sum = 0
#     for x in giatri:
#         sum = sum + x
#     print(sum)
# tinhtong(1, 2, 5, 7, 8, 9)

# #Truyền nhiều đối số, xác định thông qua tên, sử dụng **
# def xinchao(**hovaten):
#     print("Xin chào: " + hovaten["ho"])
# xinchao(ten="Tung",tendem="Nhat",ho="Le")

# #Sử dụng return để trả về giá trị
# def tinhtich(*giatri):
#     tich=1
#     for x in giatri:
#         tich = tich*x
#     return tich
# tich1 = tinhtich(1,4,6)
# print(tich1)

# #Tìm UCLN của hai số a, b
# def gcd(a,b):
#     while (a!=b):
#         if (a>b):
#             a = a - b
#         else:
#             b = b - a
#     return a
# print(gcd(55, 100))

# #Nhập vào một dãy n số từ bàn phím, sau đó tính tổng 
# #Yêu cầu: xây dựng các hàm:
# #nhap(n, list_number)
# #tinhtong(list_number)
# list_number = []
# n = -1

# while(True):
#     try:
#         n = int(input("Nhập vào số lượng phần tử: "))
#     except:
#         print("Hãy nhập lại một giá trị n>=1")
#     if (n>=1):
#         break

# def nhap(n, list_number):
#     for i in range(n):
#         list_number.append(int(input("Nhập vào giá trị thứ " + str(i) + ": ")))

# def tinhtong(list_number):
#     tong = 0
#     for x in list_number:
#         tong += x
#     return tong

# nhap(n, list_number)
# print("Tong = " + str(tinhtong(list_number)))


# #Lambda Function
# #Ví dụ
# kiemtrasochan = lambda a : (a%2==0)
# print(kiemtrasochan(5))

# tinhtong = lambda a, b : a+b
# print(tinhtong(5, -2))

# #Ví dụ về sử dụng lambda function bên trong các function
# def hamMu(n):
#     return lambda x : x**n
# hamMu2 = hamMu(2)
# hamMu3 = hamMu(3)
# print(hamMu2, hamMu3)

# #Lập trình hướng đối tượng
# #Ví dụ về class 
# class SimpleClass:
#     #Attribute: khu vực để khai báo biến
#     i = 5 #ở đây i là biến toàn cục

#     #_init_: tạo ra đối tượng cần dùng
#     def __init__(self):
#         self.j = 7

#     #methods:
#     def printMe(self):
#         print(self.j)

# objectA = SimpleClass() #tạo ra những đối tượng cụ thể từ class
# objectB = SimpleClass()

# objectA.printMe()
# print(objectB.i)

# #Thay đổi giá trị của thuộc tính
# objectA.i = 100
# objectB.j = 500
# print(objectA.i)
# objectB.printMe()

# #Thử truy cập phương thức không phải static
# SimpleClass.printMe() #sẽ báo lỗi

# #Ví dụ khác
# class SimpleClass2:
#     #constructor
#     def __init__(self):
#         self.name = "Nhat"
    
#     #methods
#     def hello(self):
#         print("Hello " + self.name)
    
#     #static methods
#     #@: ở đây gọi là annotation, là những đánh dấu
#     @staticmethod
#     def hi(name):
#         print("Hi " + name)

# objectC = SimpleClass2()
# objectD = SimpleClass2()

# objectC.hello()
# objectD.hi("Peter")

# SimpleClass2.hello() #sẽ báo lỗi
# SimpleClass2.hi("Peter") #không báo lỗi

# #Bài tập: Xây dựng class Ngay, thuộc tính gồm có: ngày, tháng, năm
# #Xây dựng các phương thức:
# #Cho biết đó là ngày thứ bao nhiêu trong năm
# #Staticmethod: cho biết tháng đó có bao nhiêu ngày

# class Ngay:
#     #Constructor
#     def __init__(self, giatri_ngay, giatri_thang, giatri_nam):
#         self.ngay = giatri_ngay
#         self.thang = giatri_thang
#         self.nam = giatri_nam

#     #Xác định số ngày của tháng:
#     @staticmethod
#     def soNgayCuaThang(thang, nam):
#         if (thang in [1,3,5,7,8,10,12]):
#             return 31
#         elif (thang in [4,6,9,11]):
#             return 30
#         elif (thang==2):
#             if (nam%400==0 or (nam%4==0 and nam%100!=0)):
#                 return 29
#             else:
#                 return 28
            
#     #15/3/2022:
#     #Tháng 1: 31 ngày
#     #Tháng 2: 28 ngày
#     #31 + 28 + 15 = ?
#     def ngayTrongNam(self):
#         giatriNgayTrongNam = 0
#         #Tính tổng số lượng ngày của những tháng trước
#         for x in range(1, self.thang):
#             giatriNgayTrongNam += self.soNgayCuaThang(x, self.nam)
#         #Cộng thêm số ngày của tháng hiện tại
#         giatriNgayTrongNam += self.ngay
#         #Trả kết quả
#         return giatriNgayTrongNam
    
# ngayA = Ngay(15, 3, 2022)
# print(ngayA.ngayTrongNam())

# ngayB = Ngay(15, 1, 2022)
# print(ngayB.ngayTrongNam())


# #Bài tập về kế thừa

# #Bài tập về động vật
# #Xây dựng class "cha"(base class-class cơ sở)
# class Animal:
#     #Constructor: xây dựng ra đối tượng
#     def __init__(self, animalTypeA, nameA, widthA, heightA, weightA):
#         self.animalType = animalTypeA
#         self.name = nameA
#         self.width = widthA
#         self.height = heightA
#         self.weight = weightA

#     #phát ra âm thanh:
#     def makeVoice(self):
#         print("Unknown voice")
    
#     #in thông tin
#     def printMe(self):
#         print("animalType: {0}, name={1}, width={2}, height={3}, weight={4}".format(self.animalType,self.name,self.width,self.height,self.weight))

# a1 = Animal("A cat", "Miu", "30cm", "100cm", "10kg")
# a1.printMe()
# a1.makeVoice()

# class Dog(Animal): 
#     #Constructor của lớp con:
#     def __init__(self, nameA, widthA, heightA, weightA, isChampionA):
#         #gọi constructor của lớp cha
#         Animal.__init__(self, "Dog", nameA, widthA, heightA, weightA)
#         #gán giá trị cho các thuộc tính bổ sung
#         self.isChampion = isChampionA
    
#     #override method
#     def makeVoice(self):
#         print("{0}: gau gau".format(self.name))
    
# dog1 = Dog("Mic", "80cm", "40cm", "20kg", True)
# dog2 = Dog("Mật", "100cm", "60cm", "40kg", True)
# dog1.makeVoice()
# dog1.printMe()
# dog2.makeVoice()
# dog2.printMe()

# #Sử dụng Try-Except
# #Ví dụ
# try:
#     a = int(input("Nhập vào số nguyên a: "))
#     print(str(a) + " + 5 = " + str(a+5))
# except:
#     print("Nhập dữ liệu không chính xác!")

# try:
#     a = int(input("Nhập vào số nguyên a: "))
#     print(str(a) + " + 5 = " + str(a+5))
# except Exception as e:
#     print(e)

# try:
#     a = int(input("Nhập vào số nguyên a: "))
#     print(str(a) + " + 5 = " + str(a+5))
# except Exception as e:
#     print(e)
# else:
#     print("Không có lỗi xảy ra!")
# finally:
#     print("Kết thúc chương trình!")

# #Làm việc với file
# #open()
# #"x" - tạo file
# try:
#     f = open("vidu1.txt", "x")
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# #"w" - ghi dữ liệu file
# #"a" - nối vào file
# try:
#     with open("vidu1txt", "w") as f: #ghi đề vào dữ liệu cũ
#         f.write("Xin chào các bạn.\n")
#         f.close()
# except Exception as e:
#     print(e)

# try:
#     with open("vidu1txt", "a") as f: #ghi nối tiếp vào nhau
#         f.write("Xin chào các bạn.\n")
#         f.close()
# except Exception as e:
#     print(e)

# #"r" - đọc file
# try:
#     with open("vidu1txt", "r") as f:
#         noidung = f.read()
#         print(noidung)
# except Exception as e:
#     print(e)

# try:
#     with open("vidu1txt", "r") as f:
#         list_noidung = f.readlines() #đọc tất cả các dòng
#         i = 1
#         for noidung in list_noidung:
#             print(str(i)+":"+noidung)
#             i += 1
# except Exception as e:
#     print(e)

# try:
#     with open("vidu1txt", "r") as f:
#         noidung = f.readline() #đọc 1 dòng
#         print(noidung)
# except Exception as e:
#     print(e)





