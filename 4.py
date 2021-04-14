import argparse
import mysql.connector

parser = argparse.ArgumentParser(description='My parser')
parser.add_argument('-d', '--data', type=str, help='Create Databases')
parser.add_argument('-t', '--table', type=str, help='Create table')
parser.add_argument('-c', '--columns', type=str, help='Create columns')
parser.add_argument('-r', '--records', type=str, help='Create records')
parser.add_argument('-i', '--info', type=str, help='SQL-queries')
parser.add_argument('-e', '--erase', type=str, help='Delete row')
parser.add_argument('-u', '--update', type=str, help='Update lines')
parser.add_argument('-k', '--kill', type=str, help='Deleting database')
args = parser.parse_args()


class Parser1:
    def __init__(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="[newpassword]")
        self.mycursor = mydb.cursor()
        self.parser()
        mydb.commit()
        mydb.close()

    def createdb(self, data):
        try:
            self.mycursor.execute(f'create database {data}')
            print('The database was created!')
        except mysql.connector.Error as error:
            print(error)

    def kill_em_all(self, kill):
        try:
            self.mycursor.execute(f'drop database {kill}')
            print('The database was destroyed!')
        except mysql.connector.Error as error:
            print(error)

    def table_create(self, table=''):
        try:
            t = table.split(";")
            for i in t:
                self.mycursor.execute(i)
            print(f'table {table} was created!')
        except mysql.connector.Error as error:
            print(error)

    def create_column(self, column=''):
        try:
            t = column.split(";")
            for i in t:
                self.mycursor.execute(i)
            print(f'Column {column} create')
        except mysql.connector.Error as error:
            print(error)

    def create_records(self, records=''):
        try:
            t = records.split(";")
            for i in t:
                self.mycursor.execute(i)
            print(f'Records {records}inserted')
        except mysql.connector.Error as error:
            print(f'{error} Column login not exist!')

    def info(self, info=''):

        try:
            t = info.split(";")
            for i in t:
                self.mycursor.execute(i)
            while True:
                    info = input("Enter SQL > ")
                    if info == 'exit':
                        print('The work was completed!')
                        break
                    else:
                        self.mycursor.execute(f'{info}')
                        for i in self.mycursor:
                            print(', '.join(map(str, i)))
        except EOFError:
            print('Вы вышли из программы!')
        except mysql.connector.Error as error:
            print(f'{error}')

    def erase(self, delete=''):
        try:
            t = delete.split(";")
            for i in t:
                self.mycursor.execute(i)
            print(f'Records {delete}inserted')
        except mysql.connector.Error as error:
            print(f'{error} Column login not exist!')

    def mysql_update_lines(self, update=''):
        try:
            t = update.split(";")
            for i in t:
                self.mycursor.execute(i)
            print(f'Records {update}inserted')
        except mysql.connector.Error as error:
            print(f'{error}')

    def parser(self):
        if args.data:
            self.createdb(args.data)
        elif args.table:
            self.table_create(args.table)
        elif args.columns:
            self.create_column(args.columns)
        elif args.records:
            self.create_records(args.records)
        elif args.erase:
            self.erase(args.erase)
        elif args.update:
            self.mysql_update_lines(args.update)
        elif args.kill:
            self.kill_em_all(args.kill)
        elif args.info:
            self.info(args.info)
        else:
            parser.print_help()


if __name__ == '__main__':
    args = parser.parse_args()
    z = Parser1()
