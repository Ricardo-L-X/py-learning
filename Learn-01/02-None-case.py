def check_age(age):
    if age < 18:
        return None
    else:
        return "SUCCESS"

result = check_age(16)
if not result:
    print("未成年!")

