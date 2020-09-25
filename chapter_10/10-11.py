import json

def get_stored_number():
    """Get stored number if available."""
    filename = 'fav_num.json'
    try:
        with open(filename) as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_num

def get_new_number():
    """Prompt for a new number."""
    fav_num = input("请输入你喜欢的数字：")
    filename = 'fav_num.json'
    with open(filename, 'w') as f_obj:
        json.dump(fav_num, f_obj)
    return fav_num

def greet_user():
    """Print favourite number"""
    fav_num = get_stored_number()
    if fav_num:
        print("I know your favorite number! It's " + str(fav_num) + "!")
    else:
        fav_num = get_new_number()
        print("We'll remember your favourite number.")

greet_user()
