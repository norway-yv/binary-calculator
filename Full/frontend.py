import binaryAdd
import convert

inputOne = convert.to32bit(input("First number = "))
inputTwo = convert.to32bit(input("Second number = "))

print(f"Output: {convert.shorten(binaryAdd.bit32(inputOne, inputTwo))}")
