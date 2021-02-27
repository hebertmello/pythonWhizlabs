import sys

random = ['b', 0, 5]

for entry in random:
    try:
        print("The Entry is", entry)
        d = 1 / int(entry)
        break
    except:
        print("oops!!", sys.exc_info(), "occurred")
        print("next entry")

print("The reciprocal of", entry, "is", d)