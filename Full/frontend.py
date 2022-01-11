import binaryAdd
import convert

inputOne = convert.toByte(input("First number = "))
inputTwo = convert.toByte(input("Second number = "))

print(f"Output: {binaryAdd.byte(inputOne, inputTwo)}")
