import file_handler as fh
def admin():
    books = fh.load_data('books.json')
    print('welcome admin!')
    print('1. Add book')
    print('2. View books')
    print('3. Remove book')
    print('4. Exit')
    try:
        while True:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                bk_code = input('Enter the book code: ')
                bk_name = input('Enter the book name: ')
                book_dict = {'code': bk_code, 'name': bk_name, 'status': 'available'}
                books.append(book_dict)
                print('Book added successfully!')
                fh.save_data(books,'books.json')
            elif choice == 2:
                print(books)
            elif choice == 3:
                print(books)
                while True:
                    bk_remove = input('Enter the book code you want to remove.Press e to exit: ')
                    for i in books:
                        if i['code'] == bk_remove:
                            books.remove(i)
                            print('Book removed successfully!')
                            fh.save_data(books, 'books.json')
                        else:
                            print('Book not found!')
                            break
                    if bk_remove.lower() == 'e':
                        break
                    if bk_remove.isdigit():
                        print('Invalid input! Put a valid Book code!')
            elif choice == 4:
                break            
    except ValueError:
        print('Invalid input! Please put a number.')
        admin()