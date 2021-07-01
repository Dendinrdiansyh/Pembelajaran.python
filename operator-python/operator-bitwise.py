a = int(input("inputkan nilai a: "))
b = int(input("inputkan nilai b: "))

# operasi AND
c = a & b
print("a", " & ", b," = ", c) 
# operasi R
c = a | b
print("a", " | ", b," = ", c) 
# operasi xor
c = a ^ b
print("a", " ^ ", b, " = ", c)

# operasi not
c = ~a
print("~a", " = ", c)

# operasi shift left (tukar posisi biner)
c = a << b
print("a", " << ", b, " = ", c)

# operasi shift right(tukar posisi biner)
c = a >> b
print("a", " >> ", b, " = ", c)


