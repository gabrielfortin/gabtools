from gabtools import FloatArray
import numpy
from numpy import float16, float32, float64

numbers = [1,2,3]

# Constructor tests

def test_checkConstructor16():
    arr = FloatArray(numbers, 16)
    assert type(arr[0]) == numpy.float16

def test_checkConstructor32():
    arr = FloatArray(numbers, 32)
    assert type(arr[0]) == numpy.float32

def test_checkConstructor64():
    arr = FloatArray(numbers, 64)
    assert type(arr[0]) == numpy.float64

def test_checkConstructorData():
    arr = FloatArray(numbers, 64)
    assert arr.numbers == numbers

# getitem and setitem tests

def test_getitem():
    arr = FloatArray(numbers, 64)
    assert arr[0] == numbers[0] and arr[1] == numbers[1]

def test_setitem():
    arr = FloatArray(numbers, 64)
    arr[0] = numbers[1]
    assert arr[0] == numbers[1]

# Conversion tests

def checkConversion(floatArray, floatType):
    return floatArray.numbers == numbers and type(floatArray[0])==floatType

def test_convert16To16():
    arr = FloatArray(numbers=numbers, floatType=16)
    arr.convertTo16()
    assert checkConversion(arr, float16)

def test_convert16To32():
    arr = FloatArray(numbers=numbers, floatType=32)
    arr.convertTo32()
    assert checkConversion(arr, float32)

def test_convert16To64():
    arr = FloatArray(numbers=numbers, floatType=64)
    arr.convertTo64()
    assert checkConversion(arr, float64)

def test_convert32To16():
    arr = FloatArray(numbers=numbers, floatType=16)
    arr.convertTo16()
    assert checkConversion(arr, float16)

def test_convert32To32():
    arr = FloatArray(numbers=numbers, floatType=32)
    arr.convertTo32()
    assert checkConversion(arr, float32)

def test_convert32To64():
    arr = FloatArray(numbers=numbers, floatType=64)
    arr.convertTo64()
    assert checkConversion(arr, float64)

def test_convert64To16():
    arr = FloatArray(numbers=numbers, floatType=16)
    arr.convertTo16()
    assert checkConversion(arr, float16)

def test_convert64To32():
    arr = FloatArray(numbers=numbers, floatType=32)
    arr.convertTo32()
    assert checkConversion(arr, float32)

def test_convert64To64():
    arr = FloatArray(numbers=numbers, floatType=64)
    arr.convertTo64()
    assert checkConversion(arr, float64)

# Append tests

def test_appendInt():
    arr = FloatArray(numbers, 64)
    arr.append(1)
    assert arr.numbers == [1,2,3,1]

def test_appendInts():
    arr = FloatArray(numbers, 64)
    arr.append(1)
    arr.append(2)
    assert arr.numbers == [1,2,3,1,2]
    
