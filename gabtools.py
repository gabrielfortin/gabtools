from numpy import float32, float64, float128
class FloatArray:
    def __init__(self, numbers=None, floatType=None):
        
        if floatType == 32 or floatType == 64 or floatType == 128:
            self.floatType = floatType
        else:
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
    def is32(self):
        return self.floatType == 32
    @property
    def is64(self):
        return self.floatType == 64
    @property
    def is128(self):
        return self.floatType == 128
        
    def append(self, elem):
        if self.is32:
            self.numbers.append(float32(elem))
        elif self.is128:
            self.numbers.append(float128(elem))
        else:
          self.numbers.append(float64(elem))

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
        if self.floatType == 32:
            for number in numbers:
                self.numbers.append(float32(number))

        elif self.floatType == 64:
            for number in numbers:
                self.numbers.append(float64(number))
                
        elif self.floatType == 128:
            for number in numbers:
                self.numbers.append(float128(number))
