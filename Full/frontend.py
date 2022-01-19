import binaryAdd
import convert

inputOne = input("First number = ")
inputTwo = input("Second number = ")

if len(inputOne) > len(inputTwo):
    inputTwo = convert.toBit(len(inputOne), inputTwo)
elif len(inputTwo) > len(inputOne):
    inputOne = convert.toBit(len(inputTwo), inputOne)

print(f"Output: {convert.shorten(binaryAdd.bit(len(inputOne), inputOne, inputTwo))}")
