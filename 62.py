import leveldb

fname_db = 'test_db'

db = leveldb.LevelDB(fname_db)
# valueが日本のものを列挙
clue = 'Japan'.encode()
result = [value[0].decode() for value in db.RangeIter() if value[1] == clue]
# print(result)
print('{}件'.format(len(result)))
