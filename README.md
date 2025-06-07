# Python Calculator

A simple command-line calculator written in Python that performs basic arithmetic operations.

## Features

- ✅ Addition
- ✅ Subtraction
- ✅ Multiplication
- ✅ Division (with zero division protection)
- ✅ Power/Exponentiation
- ✅ Square Root
- ✅ Interactive menu-driven interface
- ✅ Input validation
- ✅ Error handling

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abhishekrajpura/python-calculator.git
cd python-calculator
```

2. Run the calculator:
```bash
python calculator.py
```

## Usage

Run the script and follow the interactive menu:

```bash
$ python calculator.py

Welcome to Python Calculator!

=== Python Calculator ===
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Exit
=========================
Enter choice (1-7): 
```

### Example Operations

**Addition:**
```
Enter choice (1-7): 1
Enter first number: 10
Enter second number: 5

Result: 10.0 + 5.0 = 15.0
```

**Division:**
```
Enter choice (1-7): 4
Enter first number: 10
Enter second number: 3

Result: 10.0 ÷ 3.0 = 3.3333333333333335
```

**Square Root:**
```
Enter choice (1-7): 6
Enter number: 16

Result: √16.0 = 4.0
```

## Error Handling

The calculator includes robust error handling for:

- **Division by zero**: Returns an error message instead of crashing
- **Invalid input**: Prompts user to enter valid numbers
- **Negative square roots**: Returns an error message for mathematical impossibility
- **Keyboard interrupts**: Graceful exit when Ctrl+C is pressed

## Code Structure

The calculator is organized into clear functions:

- `add(x, y)` - Addition operation
- `subtract(x, y)` - Subtraction operation
- `multiply(x, y)` - Multiplication operation
- `divide(x, y)` - Division operation with zero check
- `power(x, y)` - Exponentiation operation
- `sqrt(x)` - Square root operation with negative check
- `display_menu()` - Shows the calculator menu
- `get_number(prompt)` - Input validation for numbers
- `main()` - Main program loop

## Contributing

Feel free to fork this repository and submit pull requests for any improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

- [ ] Scientific calculator functions (sin, cos, tan, log)
- [ ] Memory functions (store, recall, clear)
- [ ] History of calculations
- [ ] GUI interface using tkinter
- [ ] Expression evaluation (e.g., "2+3*4")
- [ ] Unit tests
