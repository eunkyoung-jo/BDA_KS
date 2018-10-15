#coding: utf-8
#2018.10
import dataset


def txt2table(fn, db, tablename):
    infile = open(fn, 'r', encoding='utf-8')
    lines = infile.readlines()
    infile.close()

    idx = 0
    for l in lines:
        tab = l.split('\t')
        record = {}
        record['date'] = tab[0]
        record['url'] = tab[1]
        record['title'] = tab[2]
        record['btext'] = tab[3]
        record['idx'] = idx
        idx += 1

        db[tablename].upsert(record, ['idx'])


def table2txt(db, tablename, cols, fn):
    outfile = open(fn, 'w', encoding='utf-8')

    records = db[tablename].all()
    for rec in records:
        item = []
        for col in cols :
            item.append(rec[col])
        outfile.write('%s' %('\t'.join(item)))
    outfile.close()


if __name__ == "__main__":
    try:
        kdb = dataset.connect('sqlite:///data/kdb.db')

        txt2table('data/한국학.txt', kdb, 'kstudies')
        txt2table('data/한글날.txt', kdb, 'HangulDay')
        table2txt(kdb, 'HangulDay', ['title', 'btext'], 'mydata.txt')

    except Exception as e:
        print(e)
