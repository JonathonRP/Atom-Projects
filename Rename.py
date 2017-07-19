import os, sys, getpass
from colorama import init, Style, Fore
from termcolor import colored, cprint
from msvcrt import getch

init(autoreset=True)

def main():
    user = getpass.getuser()
    cdPath = input(Style.BRIGHT + colored('Your Desired Directory? ','yellow')) or  'C:/Users/'+ user +'/Downloads/Rename Files'
    if cdPath.strip():
        if '\\' in cdPath:
            cdPath.replace('\\','/')
        elif '/' in cdPath:
            cdPath
        else:
            print(Style.BRIGHT + colored('Invalid, Try again','red'))
            main()
    try:
        os.chdir(cdPath.strip())
    except:
        print(Style.BRIGHT + colored('Could not find directory, Try again','red'))
        main()

    print(Style.BRIGHT + colored(os.getcwd(),'yellow'))

    for f in os.listdir():
        print(colored(f,'cyan','on_magenta'))
        f_name, f_ext = os.path.splitext(f)
        f_full = colored(f_name,'cyan')+colored(f_ext,'magenta')
        print( f_full )
        print(colored(f_name,'cyan'))

        new_name = input( Style.BRIGHT + colored('Enter new name: ','cyan' ))

        if new_name.strip():
            if new_name.lower() == 'exit':
                print('Good Bye')
                raise SystemExit
            elif new_name.lower() == 'cd':
                main()
            else:
                print( f_full )
                print('{}{}'.format(Style.BRIGHT + colored(new_name.strip(),'cyan' ), colored(f_ext.strip(),'magenta')))
                rename = '{}{}'.format(new_name.strip(), f_ext.strip())

                while True:
                    print('Press Enter to rename or Escape to exit...')
                    key = ord(getch())
                    if key == 27:
                        print('Good Bye')
                        raise SystemExit
                    elif key ==13:
                        break
                os.rename(f, rename)
                print('Rename Complete')
        else:
            print(Style.BRIGHT + 'Next file is')

    sys.exit(
    print(colored('No Files','yellow'))
    ,main()) 

if __name__ == '__main__':
            main()