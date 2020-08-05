import sqlite3
import query

db = sqlite3.connect('contacts.db')
table_name = 'contacts'
print('operations:\n help - to view commands\n add - to insert new contact\n delete - to delete contact\n edit - to '
      'update contact\n view - to view all contact\n search - to find the contact\n exit - to exit')
cur = db.cursor()
cur.execute('create table if not exists Contacts(name text unique, phone numeric unique)')
db.commit()
operation = ['add', 'delete', 'edit', 'view', 'search', 'exit', 'help']
while True:
    op = input('enter the operation you want to perform: ')
    if op not in operation:
        print('invalid operation')
        continue
    elif op == 'help':
        print('operations:\n help - to view commands\n add - to insert new contact\n delete - to delete contact\n '
              'edit - to update contact\n view - to view all contact\n search - to find the contact\n exit - to exit')
        continue
    elif op == 'exit':
        exit()
    elif op == 'add':
        name = input('enter name: ')
        phone = input('enter phone: ')
        query.add(db, table_name, name=name, phone=phone)
    elif op == 'delete':
        name = input('enter name: ')
        query.delete(db, table_name, name)
    elif op == 'view':
        query.select(db, table_name)
    elif op == 'edit':
        var = input('update name or phone: ')
        if var == 'name':
            phone = input('enter the phone no of which name to be updated: ')
            new_name = input('enter the new name: ')
            query.update(db, table_name, phone=phone, where_name=new_name)
        if var == 'phone':
            name = input('enter the name whose number to be updated: ')
            new_phone = input('enter the new phone no: ')
            query.update(db, table_name, name=name, where_phone=new_phone)
    elif op == 'search':
        att = input('search by name or phone: ')
        if att == 'name':
            name = input('enter the name: ')
            query.search(db, table_name, name=name)
        if att == 'phone':
            num = input('enter the phone no: ')
            query.search(db, table_name, phone=num)

