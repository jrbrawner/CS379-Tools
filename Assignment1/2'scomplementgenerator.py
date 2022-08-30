from asyncore import write
import random

### Helper program for programming assignment
### Randomly generates number between 0 and 11 and writes machine language for simulated machine

def twos(val_str, bytes):
    import sys
    val = int(val_str, 2)
    b = val.to_bytes(bytes, byteorder=sys.byteorder, signed=False)                                                          
    return int.from_bytes(b, byteorder=sys.byteorder, signed=True)

number = random.randint(0,11)
number1 = random.randint(0,11)

number_hex = hex(number)[2:].capitalize() # splice off leading chars
number_hex1 = hex(number1)[2:].capitalize() # splice off leading chars

number_hex = '0' + str(number_hex)
number_hex1 = '0' + str(number_hex1)

number_prod = number * number1
number_prod_hex = hex(number_prod)[2:].capitalize() # splice off leading chars

if len(str(number_prod_hex)) == 1:
    number_prod_hex = '0' + str(number_prod_hex)

print('First number:', number, ' Hex value:', number_hex)
print('Second number:', number1, ' Hex value:', number_hex1)
print('Product:', number_prod, ' Hex value:', number_prod_hex)

#Memory address goes from 0 to 255, or 00 to FF (hex)

MemoryAddressOne = 'D1'
MemoryAddressTwo = 'D2'
MemoryAddressThree = 'D3'

LoadTwoNumbersIntoMemory = ['21', number_hex, '31', MemoryAddressOne, '21', number_hex1, '31', MemoryAddressTwo]
LoadTwoNumbersFromMemoryIntoR1andR2 = ['11', MemoryAddressOne, '12', MemoryAddressTwo]
StoreR2inR4ForLoop = ['40', '24']

PrepareR5ForIncrement = ['25', '01']
LoopCheckIfEqual = ['B4', '18']
LoopMath = ['53', '13']
IncrementR0 = ['50', '05']
LoopCheck = ['B0', '10']

StoreR3inMemory = ['33', MemoryAddressThree]
HaltExecution = ['C0', '00']

with open('Machine_In.txt', 'w') as write_obj:
    for i in LoadTwoNumbersIntoMemory:
        write_obj.write(str(i) + '\n')
    for i in LoadTwoNumbersFromMemoryIntoR1andR2:
        write_obj.write(str(i) + '\n')
    for i in StoreR2inR4ForLoop:
        write_obj.write(str(i) + '\n')
    for i in PrepareR5ForIncrement:
        write_obj.write(str(i) + '\n')
    for i in LoopCheckIfEqual:
        write_obj.write(str(i) + '\n')
    for i in LoopMath:
        write_obj.write(str(i) + '\n')
    for i in IncrementR0:
        write_obj.write(str(i) + '\n')
    for i in LoopCheck:
        write_obj.write(str(i) + '\n')
    for i in StoreR3inMemory:
        write_obj.write(str(i) + '\n')
    for i in HaltExecution:
        write_obj.write(str(i) + '\n')

write_obj.close()