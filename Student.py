import file_handler as fh
import Admin as ad
def stud():
    shw = fh.load_data('books.json')
    print('What would you like to do?')
    print('1. Borrow a book')
    print('2. Return a book')
    print('3.See all books')
    print('4.See avaialable books')
    print('5. Exit')
    try:
        while True:
            choice = int(input('Enter your Choice: '))
            if choice == 1:
                bk_borrow = input('Enter the book code you want to borrow(Press e to exit): ')
                for i in shw:
                    if i['code'] == bk_borrow and i['status'] == 'available':
                        i['status'] = 'borrowed'
                        print('Book has been issued!')
                        fh.save_data(shw,'books.json')
                    elif i['code'] ==bk_borrow and i['status'] != 'available':
                        print('Book cannot be issued')
                    elif bk_borrow.lower() == 'e':
                        break
                    elif shw == []:
                        print('No books available!')
            elif choice == 2:
                print(shw)
                bk_return = input('Enter the book code you want to return(Press e to exit): ')
                for i in shw:
                    if i['code'] == bk_return and i['status'] == 'borrowed':
                        i['status'] = 'available'
                        print('Book returned successfully!')
                        fh.save_data(shw, 'books.json')
                    elif i['code'] != bk_return:
                        print('Book not found!')
                    elif bk_return.lower() == 'e':
                        break
                    elif shw == []:
                        print('No books available!')
                        break
            elif choice == 3:
                print(shw)
            elif choice == 4:
                for i in shw:
                    if i['status'] == 'available':
                        print(i)
            elif choice == 5:
                break
            else:
                print('Invalid input! Please put a number between 1 and 5.')
    except ValueError:
        print('Invalid input! Please put a number.')