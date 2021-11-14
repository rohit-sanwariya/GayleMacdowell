def get_hash(str):
        salt = 0
        for x in str:
                salt += ord(x)
        return salt//100

arr = [0] * 100
arr[get_hash("rohit")] = "rohit"
print(arr[get_hash("rohit")])
