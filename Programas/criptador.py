msg = str(input("Digite uma mensagem para ser criptografada: ").strip().lower())

'''
a - 123
e - &
i - LL
o - $
u - @
'''

def invert(text: str) -> str:
    new_text = text.strip()
    return ''.join([new_text[-1:0:-1], new_text[0]])
    
def cript(text: str) -> str:
    new_text = []
    
    for _ in invert(text):
        if _ in "aeiou":
            if _ == "a":
                new_text.append("123")
            if _ == "e":
                new_text.append("&")
            if _ == "i":
                new_text.append("LL")
            if _ == "o":
                new_text.append("$")
            if _ == "u":
                new_text.append("@")
        else:
            new_text.append(_)
    
    return "".join(new_text)

cript_text = cript(msg)
print(cript_text)
    
    
flag = False
def descript(cript_text: str) -> str:

    new_text = []
    def add(char: str, lista: list) -> None:
        lista.append(char)
    global flag
    for _ in cript_text:
        if _ in ["1", "&", "L", "$", "@"]:
            match _:
                case "1":
                    pos = cript_text.index(_)
                    if cript_text[pos + 1] == "2" and cript_text[pos + 2] == "3":
                        add("a", new_text)
                        flag = True
                    
                    
                case "&":
                    add("e", new_text)
                    
                case "L":
                    if flag == True:
                        flag = False
                        continue
                      
                    pos = cript_text.index(_)
                    if cript_text[pos : pos + 2] == "LL":
                        add("i", new_text)
                        flag = True
                    
                case "$":
                    add("o", new_text)
                case "@":
                    add("u", new_text)

        elif _ == "2" or _ == "3" and flag == True:
            continue
        
        else:
            flag = False
            new_text.append(_)
            
    return invert(''.join(new_text))

print(descript(cript_text))
