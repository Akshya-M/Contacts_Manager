def add(db, tname, **data):
    col_name = ''
    val = ''
    values = []
    for i in data:
        col_name += '{}, '.format(i)
        val += '?, '
        values.append(data[i])
    col_name = col_name[:-2]
    val = val[:-2]
    try:
        cur = db.cursor()
        cur.execute('insert into {} ({}) values ({})'.format(tname, col_name, val), values)
        db.commit()
        print('insertion successful')
    except Exception as e:
        print('error in inserting data into the table', tname)
        print(e)


def delete(db, tname, name):
    cur = db.cursor()
    cur.execute('select * from {} where name=?'.format(tname), (name, ))
    row = cur.fetchone()
    if not row:
        print('data not exist')
    else:
        cur.execute('delete from {} where name=? '.format(tname), (name, ))
        print('data deleted')
        db.commit()


def update(db, tname, **data):
    old = ''
    new = ''
    old_val = []
    new_val = []
    for i, j in data.items():
        if i.startswith('where'):
            temp = i.replace('where_', '')
            new += '{}=?, '.format(temp)
            new_val.append(j)
        else:
            old += '{}=?, '.format(i)
            old_val.append(j)
    new = new[:-2]
    old = old[:-2]
    final = tuple(new_val + old_val)
    try:
        cur = db.cursor()
        cur.execute('select * from {} where {}=?'.format(tname, old[:-2]), (''.join(old_val), ))
        row = cur.fetchone()
        if not row:
            print('data not found')
        else:
            cur.execute('update {} set {} where {}'.format(tname, new, old), final)
            db.commit()
            print('update successful')
    except Exception as e:
        print('error in updating value in', tname)
        print(e)


def select(db, tname):
    cur = db.cursor()
    cur.execute('select * from {}'.format(tname))
    while True:
        row = cur.fetchone()
        if not row:
            break
        name, phone = row
        print('{} - {}'.format(name, phone))


def search(db, tname, **val):
    att = ''
    vals = ''
    for i in val:
        att += i
        vals += val[i]
    cur = db.cursor()
    key = '%{}%'.format(vals)
    cur.execute("select * from {} where {} like ?".format(tname, att), (key, ))
    data = 0
    while True:
        row = cur.fetchone()
        if not row and data == 0:
            print('data not found')
            break
        elif not row:
            break
        else:
            data = 1
            name, phone = row
            print('{} - {}'.format(name, phone))
