from MyException import NegativeError, TreagleError
import log_info


class Treagle:
    def __init__(self, A: int, B: int, C: int) -> None:
        if A > 0:
            self.A = A
        else:
            log_info.log_error(NegativeError(A, 0)) 
        if B > 0:
            self.B = B
        else:
            log_info.log_error(NegativeError(B, 0)) 
        if C > 0:
            self.C = C
        else:
            log_info.log_error(NegativeError(C, 0)) 
        
    def compare(self):
        if (self.A + self.B < self.C or self.A + self.C < self.B or self.B + self.C < self.A):
            log_info.log_error(TreagleError(self.A, self.B, self.C)) 
        else:
            if (self.A == self.B and self.B == self.C and self.C == self.A):
                text = 'Треугольник равносторонний'
                log_info.log_info(text)
                return text
            elif (self.A != self.B and self.B != self.C):
                text = 'Треугольник разносторонний'
                log_info.log_info(text)
                return text    
            else:
                text = 'равнобедренный'
                log_info.log_info(text)


if __name__ == "__main__":   
    A = 5
    B = 4
    C = 3
    
    r1 = Treagle(A, B, C)
    print(r1.compare())   