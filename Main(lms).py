import Admin as ad
import Student as st
def main():
    while True:
        print('-----------------------------------')
        print('Welcome to the library!')
        print('-----------------------------------')

        login = input('Enter your username(press e to exit): ')
        if login.lower() == 'e':
            break
        password = input('Enter your password: ')
        if login == 'admin' and password == 'admin':
            ad.admin()
        elif password == login+'253':
            print(f'Welcome {login}')
            st.stud()
        else:
            print('Invalid login or password!')

if __name__ == '__main__':
    main()