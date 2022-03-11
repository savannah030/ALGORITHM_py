def solution(phone_book):
    phone_book = sorted(phone_book)
    l = len(phone_book)
    for i in range(l-1):
        # 접'두'어 인지만 확인하면 되므로 바로 뒷단어만 확인하면 됨
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

