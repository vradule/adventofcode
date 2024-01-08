def find_first_last_number(line):
    first = None
    last = None
    for char in line:
        if(char.isdigit()):
            if(first is None):
                first = int(char)
            last = int(char)
    return first * 10 + last

def sum_first_lasts_numbers(docs):
    res = 0
    for doc in docs:
        res = res + find_first_last_number(doc)
    return res

def get_docs(file_name):
    file = open(file_name)
    return file.readlines()

docs = get_docs("example1.txt")
assert(find_first_last_number(docs[0]) == 12)
assert(find_first_last_number(docs[1]) == 38)
assert(find_first_last_number(docs[2]) == 15)
assert(find_first_last_number(docs[3]) == 77)
assert(sum_first_lasts_numbers(docs) == 142)

docs = get_docs("input.txt")
res = sum_first_lasts_numbers(docs)
print(res)

docs = get_docs("example2.txt")
for i, doc in enumerate(docs):
    docs[i] = doc.replace('one', 'o1').replace('two', 't2').replace('three', 't3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', 'e8').replace('nine', '9').replace('zero', '0')

assert(find_first_last_number(docs[0]) == 29)
assert(find_first_last_number(docs[1]) == 83)
assert(find_first_last_number(docs[2]) == 13)
assert(find_first_last_number(docs[3]) == 24)
assert(find_first_last_number(docs[4]) == 42)
assert(find_first_last_number(docs[5]) == 14)
assert(find_first_last_number(docs[6]) == 76)
assert(sum_first_lasts_numbers(docs) == 281)

docs = get_docs("input.txt")
for i, doc in enumerate(docs):
    docs[i] = doc.replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e').replace('four', 'f4r').replace('five', 'f5e').replace('six', 's6x').replace('seven', 's7n').replace('eight', 'e8t').replace('nine', 'n9e').replace('zero', 'z0o')
res = sum_first_lasts_numbers(docs)
print(res)