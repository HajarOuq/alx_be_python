def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            result = num1 + num2
        case "substract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                result = "Impossible"
            else:
                result = num1/num2
    return result