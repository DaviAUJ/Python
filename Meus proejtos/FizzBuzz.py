def FizzBuzz(FromNumber: int, ToNumber: int, NumberToCompare_0: int, NumberToCompare_1: int, Message_0: str, Message_1: str):
    for count in range(FromNumber, ToNumber + 1):
        output = str()
        
        if count % NumberToCompare_0 == 0:
            output += Message_0
        
        if count % NumberToCompare_1 == 0:
            output += Message_1
            
        print(f"{count} - {output}")
        
        
# Programa principal

FizzBuzz(1, 500, 7, 11, "Fizz", "Buzz")