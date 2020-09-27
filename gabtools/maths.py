import numpy
from numpy import float16, float32, float64
import warnings

supports128 = True

try:
    from numpy import float128
except ImportError:
    supports128 = False
    pass

class FloatArray:
    def __init__(self, numbers=None, floatType=None):
        
        if floatType in [16, 32, 64] or floatType == 128 and supports128:
            self.floatType = floatType
        elif floatType == 128 and not supports128:
            warnings.warn(f'{floatType} does not exist on this system. Switching to float64 instead.')
            self.floatType = 64
        else:
            warnings.warn(f'{floatType} is not a valid or supported float type. Switching to float64 instead.')
            self.floatType = 64

        self.numbers = []
        if numbers:
            self.numbers = numbers
            self.convertToType()
            
    def __str__(self):
        return (str(self.numbers))
        
    def __getitem__(self,index):
        return self.numbers[index]
      
    def __setitem__(self,index,value):
        self.numbers[index] = value

    @property
    def is16(self):
        return self.floatType == 16
    @property
    def is32(self):
        return self.floatType == 32
    @property
    def is64(self):
        return self.floatType == 64
    @property
    def is128(self):
        return self.floatType == 128
        
    def append(self, elem):
        if self.is16:
            self.numbers.append(float16(elem))
        if self.is32:
            self.numbers.append(float32(elem))
        elif self.is128:
            self.numbers.append(float128(elem))
        else:
          self.numbers.append(float64(elem))

    def convertTo16(self):
        self.floatType = 16
        self.convertToType()
    
    def convertTo32(self):
        self.floatType = 32
        self.convertToType()

    def convertTo64(self):
        self.floatType = 64
        self.convertToType()
        
    def convertTo128(self):
        self.floatType = 128
        self.convertToType()

    def convertToType(self):
        numbers = self.numbers
        self.numbers = []
        
        if self.is16:
            for number in numbers:
                self.numbers.append(float16(number))
        
        if self.is32:
            for number in numbers:
                self.numbers.append(float32(number))

        elif self.is64:
            for number in numbers:
                self.numbers.append(float64(number))
                
        elif self.is128:
            if supports128:
                for number in numbers:
                    self.numbers.append(float128(number))
            else:
                self.numbers = numbers
                warnings.warn(f'{self.floatType} does not exist on this system. Skipping conversion.')

def maths():
    pass
