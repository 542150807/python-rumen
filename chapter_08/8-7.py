def make_album(singer, title, numbers=''):
    """创建专辑字典"""
    album = {'singer': singer.title(), 'title': title.title()}
    if numbers:
        album['number'] = numbers
    return album

while True:
    print("\nPlease tell me information of the album：")
    print("Enter 'q' at any time to quit.")
    
    in_singer = input("Singer's name: ")
    if in_singer == 'q':
        break
    
    in_title = input("Album's title: ")
    if in_title == "q":
        break
    
    in_number = input("Number of songs: ")
    if in_number == 'q':
        break
    
    out_album = make_album(in_singer, in_title, in_number) 
    print(out_album)
