# Calculator GUI Application

This is a simple calculator application built using Python's Tkinter library. The calculator supports basic arithmetic operations, percentage calculation, negation, and more. The interface is user-friendly, featuring buttons for all functions and an entry widget to display the results.

## Features
- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Negation (±)**: Toggle between positive and negative numbers.
- **Percentage (%)**: Calculate percentages.
- **Clear (C)**: Reset the input.
- **Decimal Support**: Allows decimal input for precise calculations.

## Requirements
- Python 3.x
- Tkinter library (included with most Python installations)

## Installation
1. Clone the repository or download the script.
2. Ensure you have Python 3 installed on your machine.
3. Run the script using the following command:
   ```bash
   python calculator.py
   ```

## How to Use
1. Launch the application by running the script.
2. Use the on-screen buttons to input numbers and operations.
3. Press `=` to calculate the result.
4. Use the `C` button to clear the input.
5. Use the `±` button to toggle the sign of the number.
6. Use the `%` button to calculate percentages.

### Keyboard Shortcuts
- `Enter`: Evaluate the expression.
- `Backspace`: Clear the input.

## Code Explanation
The application consists of the following components:

### 1. **Entry Widget**
Displays the current input or the result of the calculation. It uses a `StringVar` to dynamically update the content.

### 2. **Buttons**
Each button is implemented using the `ttk.Button` widget, with a `command` parameter specifying the action to be performed when clicked. The buttons are laid out in a grid format.

### 3. **Event Handlers**
- `handle_button_click`: Handles the logic for all button clicks, including:
  - Evaluating expressions.
  - Clearing input.
  - Toggling sign.
  - Calculating percentages.

### 4. **Styling**
The application uses the `ttk.Style` class to customize the appearance of the buttons, ensuring a consistent and modern look.

### 5. **Responsive Design**
The `grid_rowconfigure` and `grid_columnconfigure` methods ensure the layout adjusts to the application window size.

## Customization
You can adjust the window size by modifying the `width` and `height` variables in the script:
```python
width = 500
height = 500
```

## Limitations
- The calculator does not handle advanced mathematical operations such as square roots, trigonometry, or logarithms.
- Division by zero will result in an error message.

## License
This project is open-source and available under the MIT License.

---
**My First Program.**

