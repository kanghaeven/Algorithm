text = input()

textlen = len(text)

start = text[:textlen//2]

if (textlen % 2 == 0): 
    end = list(reversed(text[textlen//2:]))
else:
    end = list(reversed(text[textlen//2 + 1:]))

if start == "".join(end):
    print(1)
else:
    print(0)
