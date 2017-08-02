import os, sys,getpass, cmd2, glob
from colorama import init, Style, Fore
from termcolor import colored
from msvcrt import getch

user = os.path.expanduser('~' + getpass.getuser())
init(autoreset=True)

#TODO: add color to prints

class Console(cmd2.Cmd):

    def __init__(self):
        cmd2.Cmd.__init__(self)
        self.prompt = 'how may I help you? '
        self.intro = self.do_help(arg=None)
        os.chdir('C:\\')

    def do_cd(self, arg='.'):
        try:
            os.chdir(arg)
        except:
            print(arg + ' is not a path')
        self.prompt = os.getcwd() + ' '

    def do_rename(self, args):
        if len(args.split()) == 3:
            filename, rename, directory = args.split()
            self.rename_file(filename, rename, directory)
        elif len(args.split()) == 2:
            if '*' in args:
                filext, directory = args.split()
                self.rename_files(filext, directory)
            elif '.' in args:
                filename, rename = args.split()
                directory = user + '\\Downloads'
                self.rename_file(filename, rename, directory)
        elif len(args.split()) == 1:
            if '*' in args:
                filext = args
                directory = '.'
                self.rename_files(filext, directory)
            elif '/' or '\\' in args:
                directory = args
                self.rename_files(directory=directory)
        else:
            self.rename_files()

    def do_find(self, args):
        if len(args.split()) == 2:
            name, directory = args.split()
        elif len(args.split()) == 1:
            name = args
            directory = '.'

        for root, dirs, files in os.walk(directory):
            if name in files:
                print(os.path.join(root, name))
                break

    def help_cd(self):
        print('\n'.join(['cd [path]',
            'change the current working directory, if path is empty directory doesnt change']))
    def help_find(self):
        print('\n'.join(['find file name, [path]',
            'find a file, quicker if path is provided']))
    def help_rename(self):
        print('\n'.join(['rename [file name] [ext], [new name] [path]',
            'rename one or many files. options are either no arguments or file name, new name and path;',
            'file name and new name; file extension and path; just file extension or path']))

    def pathcheck(self, directory):
        if os.path.isdir(directory):
            os.chdir(directory)
        else:
            print(directory + ' is not a path')

    def guard(self, f, rename):
        while True:
            print('Press Enter to rename or Escape to exit...')
            key = ord(getch())
            if key == 27:
                print('Good Bye')
                sys.exit(self.__init__)
            elif key ==13:
                os.renames(f, rename)
                print('Rename Complete')
                sys.exit(self.__init__)

    def rename_file(self, filename, rename, directory = '.'):

        self.pathcheck(directory)
        try:
            foundfile = self.find(filename, directory)
            f = os.path.basename(foundfile)
            print(f)
        except:
            print('unfound')
            self.__init__

        if os.path.dirname(foundfile) != os.getcwd():
            os.chdir(os.path.dirname(foundfile))

        print(Style.BRIGHT + colored(os.getcwd(),'yellow'))
        fname, fext = os.path.splitext(f)
        print(colored(filename,'cyan','on_magenta'))
        fulln = colored(fname,'cyan')+colored(fext,'magenta')
        print( fulln )
        print(colored(fname,'cyan'))
        print('{}{}'.format(Style.BRIGHT + colored(rename.strip(),'cyan' ), colored(fext.strip(),'magenta')))
        rename = '{}{}'.format(rename.strip(), fext.strip())
        self.guard(f, rename)

    def rename_files(self, filext = None, directory =  user + '\\Downloads\\Rename Files' ):

        self.pathcheck(directory)
        print(Style.BRIGHT + colored(os.getcwd(),'yellow'))

        if filext:
            directory = glob.glob(filext, recursive=True)
        else:
            directory = os.listdir()

        count = len(directory)

        for f in directory:
            print(colored(f,'cyan','on_magenta'))
            f_name, f_ext = os.path.splitext(f)
            full_n = colored(f_name,'cyan')+colored(f_ext,'magenta')
            print( full_n )
            print(colored(f_name,'cyan'))

            new_name = input( Style.BRIGHT + colored('Enter new name: ','cyan' ))

            if new_name.strip():
                if new_name.lower() == 'cancel':
                    self.prompt = 'What now? '
                    sys.exit(self.__init__)
                elif 'cd' in new_name.lower():
                    command, path = new_name.split()
                    self.do_cd(path or '.')
                    self.rename_files(filext = None)
                else:
                    print( full_n )
                    print('{}{}'.format(Style.BRIGHT + colored(new_name.strip(),'cyan' ), colored(f_ext.strip(),'magenta')))
                    rename = '{}{}'.format(new_name.strip(), f_ext.strip())
                    self.guard(f, rename)

            else:
                if count == 1:
                    break
                else:
                    print(Style.BRIGHT + 'Next file is')
                    count = count - 1
        else:
            print(Style.BRIGHT + colored('No files to rename', 'red'))
            sys.exit(self.__init__)

    def find(self, name, directory = '.'):
        for root, dirs, files in os.walk(directory):
            if name in files:
                return os.path.join(root, name)

if __name__ == '__main__':
    Console().cmdloop()
