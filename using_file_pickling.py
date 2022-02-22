import pickle

shoplistfile = 'shoplist.data'

shoplist = ['яблоки', 'груши', 'морковь']

f = open(shoplistfile, 'wb')        # wb-write binary
pickle.dump(shoplist, f)            # консервация данных
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)

