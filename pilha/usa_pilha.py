from pilha import Pilha

stack = Pilha(1)

stack.put("USP")
stack.put("FIAP")
stack.put("FGV")
stack.put("UNICAMP")
stack.put("UNIP")

while not stack.isEmpty():
    print(stack.pop())


fila = []

#enfila (put)
fila.append("USP")

#fila cheia -> return False
#fila vazia
if len(fila) == 0:
    return True
else:
    return False

#desenfila (get)    
fila.pop(0)

#primeiro da fila (peek)
fila[0]

