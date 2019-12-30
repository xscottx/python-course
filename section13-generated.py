# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# counter
from collections import Counter
l = [1,1,1,1,2,2,3,32,12,4]
Counter(l)


# %%
s = 'aasdfddsasadasfaasdfd'
Counter(s)


# %%
s = 'How many times does each word show up in this sentence word word shoe up up show?'
words = s.split()
Counter(words)


# %%
c = Counter(words)
c.most_common(2)


# %%
# least common
c.items()
for a,b in c.items():
    print(a,b)


# %%
c.most_common()[:-3-1:-1]


# %%
from collections import defaultdict
# will never raise a KeyError. if DNE, will return nothing
d = {'k1':1}
d['k1']


# %%
# d['k2'] # will get KeyError


# %%
d = defaultdict(object) # sets d to a defaultdictionary


# %%
d['one']


# %%
for item in d:
    print(item)


# %%
d = defaultdict(lambda : 0)
d['one']


# %%
d['two'] = 2
d


# %%
# ordered dictionary will retain order to dict
from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
d['g'] = 7
# keeps insertion order, but NOT sort order, unless u use OrderedDict


# %%
d


# %%
for k,v in d.items():
    print(k,v)


# %%
d1 = {}
d1['a'] = 1
d1['b'] = 2
d2 = {}
d2['b'] = 2
d2['a'] = 1
print(d1 == d2)  # true


# %%
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2
d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
print(d1 == d2)  # false, bc diff order of objects


# %%
t = (1,2,3)
t[0]


# %%
from collections import namedtuple


# %%
Dog = namedtuple('Dog','age breed name')


# %%
sam = Dog(age=2,breed='lab',name='Sammy')
sam


# %%
sam.age


# %%
sam[0]


# %%
Cat = namedtuple('Cat','fur claws name')


# %%
c = Cat(fur='Fuzzy',claws=False,name='Kitty')


# %%
c.name


# %%
import datetime

t = datetime.time(5,25,1) # hr, min, sec
print(t)


# %%
t.minute


# %%
t.microsecond


# %%
print(datetime.time.min)


# %%
print(datetime.time.max)


# %%
print(datetime.time.resolution)


# %%
today = datetime.date.today()


# %%
print(today)


# %%
today.timetuple()


# %%
today.year


# %%
dt = datetime.date(year=2019,month=12,day=30)
dt.year


# %%
naive = datetime.datetime.now()
naive.tzinfo


# %%
import pytz

timezone = pytz.timezone('America/Chicago')
d_aware = timezone.localize(naive)
d_aware.tzinfo


# %%
d1 = datetime.date(2015,3,11)
print(d1)


# %%
d2 = d1.replace(year=1990)
d2


# %%
d1-d2 # returns delta between d1 and d2, d1 is AHEAD of d2


# %%
d2-d1 # d2 is BEHIND d1


# %%
import pdb

x = [1,3,4]
y = 2
z = 3
result = y + z
print(result)

pdb.set_trace()

result2 = y+x # intentionally doing int to list
print(result2)


# %%


