import binaryAdd
import convert

inputOne = convert.to32bit(input("First number = "))
inputTwo = convert.to32bit(input("Second number = "))

print(f"Output: {binaryAdd.bit32(inputOne, inputTwo)}")
