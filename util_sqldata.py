#coding: utf-8
#2018.10
import dataset

def txt2table(fn, cols, dbname, tablename):
    db = dataset.connect('sqlite:///%s' %dbname)
    infile = open(fn, 'r', encoding='utf-8')
    lines = infile.readlines()
    infile.close()

    idx = 0
    for l in lines:
        tab = l.split('\t')
        if len(tab) < len(cols) :
            print('txt file columns !=', cols)
            return
        record = {}
        for i, col in enumerate(cols) :
            record[col] = tab[i]
        record['idx'] = idx
        idx += 1

        db[tablename].upsert(record, ['idx'])


def table2txt(dbname, tablename, cols, fn):
    db = dataset.connect('sqlite:///%s' %dbname)
    outfile = open(fn, 'w', encoding='utf-8')

    records = db[tablename].all()
    for rec in records:
        item = []
        for col in cols :
            item.append(rec[col])
        outfile.write('%s\n' %('\t'.join(item)))
    outfile.close()

def xlsx2table(dbname, tablename, fn):
    import pandas as pd
    import sqlite3 #pandas.to_sql() uses sqlite3 or sqlalchemy
    condb = sqlite3.connect(dbname)
    idata = pd.read_excel(fn, dtype=str) #without dtype(str), '00001' is to be '1'
    idata.to_excel('tmp.xlsx')
    idata.to_sql(name=tablename, con=condb, if_exists='replace') #'fail', 'replace'. 'append'
    condb.close()
    return

def table2xlsx(dbname, tablename, fn):
    #sudo pip3 install openpyxl
    import pandas as pd
    db = dataset.connect('sqlite:///%s' %dbname)
    records = db[tablename].all()
    columns = db[tablename].columns
    all_rec = [rec for rec in records]
    odata = pd.DataFrame(all_rec, columns=columns)
    outfile = pd.ExcelWriter(fn)
    odata.to_excel(outfile, 'meta')
    outfile.save()

if __name__ == "__main__":
    try:
        #Week 7:2018.10.16
        '''
        txt2table('data/한국학.txt', ['date', 'url', 'title', 'btext'], 'data/kdb', 'kstudies')
        txt2table('data/한글날.txt', ['date', 'url', 'title', 'btext'], 'data/kdb', 'HangulDay')
        table2txt('data/kdb.db', 'HangulDay', ['title', 'btext'], 'mydata.txt')
        '''
        #Week 9
        #Task1: Make xlxs file from kstudies table in kdb.db
        '''xlsx2table('data/kdb.db', 'students', 'students.xlsx')
        table2xlsx('data/kdb.db', 'students', 'data/students_db.xlsx')
        '''
        #week 14
        table2txt('data/periodicals.db', 'article_body_ma_013', ['body'], 'ma_013.txt')
    except Exception as e:
        print(e)
