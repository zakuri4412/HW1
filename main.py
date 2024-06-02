import re

def find_max_dict(dict):
   print("Bai 1")
   if not dict:
       return
   maxValue = max(zip(dict.values(), dict.keys()))
   if maxValue is None:
       print("Empty dictionary")
   else:
       print(f"Max key is: {maxValue[1]} with value {maxValue[0]}\n")

def count_element(ele):
    print("Bai 2")
    list_dict ={}
    for item in ele:
        if item in list_dict:
            list_dict[item] +=1
        else:
            list_dict[item] = 1
    print(list_dict)
    print("\n")

def is_strong_password(password):
    print("bai 3")
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False

    if not re.search(r'[!@#$%^&*()_+{}|:"<>?]', password):
        return False

    return True

def split_name(users):
    print("bai 4")
    pattern = r'^(.*?)\s(.*?)$'

    for user in users:
        match_name = re.match(pattern,user)
        if match_name:
            print(f"Lastname {match_name.group(1)} "
                  f"Firstname {match_name.group(2)}")
        else:
            print("Name not match")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # bai 1
    dict = {"a" : 1, "b": 20, "c": 13, "d": 111}
    find_max_dict(dict)

    #bai 2
    list_ele = [1,3,5,1,2,3,5,7,3]
    count_element(ele=list_ele)

    #bai 3
    password = input("Pasword: ")
    if is_strong_password(password):
        print("password is strong\n")
    else:
        print("Password not strong enought\n")


    #bai 4
    users = ["Trần Thị Mai Anh",
            "Nguyễn Văn Bảo Long",
            "Lê Thị Hồng Nga",
            "Phạm Đức Trọng",
            "Hồ Văn Đức",
    ]
    split_name(users)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
