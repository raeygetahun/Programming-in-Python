class FormulaError(Exception):
    pass

while True:
    formula = input()
    
    if formula == 'quit':
        break
    
    try:
        elements = formula.split()
        if len(elements) != 3:
            raise FormulaError("Invalid formula: must contain 3 elements")
        
        num1 = float(elements[0])
        num2 = float(elements[2])
        
        if elements[1] not in ['+', '-']:
            raise FormulaError("Invalid operator: must be + or -")
        
        if elements[1] == '+':
            result = num1 + num2
        else:
            result = num1 - num2
        
        print("Result:", result)
    except ValueError:
        raise FormulaError("Invalid number: must be a valid float")
    except FormulaError as e:
        print("FormulaError:", e)
