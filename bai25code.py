def CheckDoiXung(s):
    flag=True
    for i in range (len(s)):
        if s[i] !=s[len(s)-i-1]:
            flag=False
            break
    return flag
def main():
    print("nhap 1 chuoi:")
    s=input()
    if(CheckDoiXung(s)):
        print("Chuoi ban nhap doi xung")
    else:
        print('Chuoi ban nhap khong doi xung')
while True:
    main()
    print("Tiep khong Thim?(c/k):",end='')
    s=input()
    if s=='k':
        break
print("CAM ON THIM")
