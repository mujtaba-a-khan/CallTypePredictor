# IDE Usage and Functional Programming Documentation

This document covers two significant aspects of the development process for the Call Type Predictor project: the use of Visual Studio Code (VSCode) as the Integrated Development Environment (IDE) and the application of functional programming principles within the project's codebase.

## Part 1: IDE Usage - Visual Studio Code

Visual Studio Code is a lightweight, powerful source code editor that runs on your desktop. It has built-in support for JavaScript, TypeScript, and Node.js and has a rich ecosystem of extensions for other languages (including Python, which this project uses).

### Key Features of VSCode Used in the Project

- **Syntax Highlighting and IntelliSense**: VSCode provides smart completions based on variable types, function definitions, and imported modules.
- **Code Navigation**: Quick navigation to definitions, references, and more.
- **Integrated Terminal**: Allows running shell commands and scripts directly from the IDE, facilitating a smooth workflow for testing and version control.
- **Extensions**: Utilization of Python-specific extensions like Python Extension Pack, Pylint, and autopep8 for linting and formatting, enhancing coding efficiency and standard compliance.
- **Debugging**: Built-in debugging tools to set breakpoints, inspect data, and debug scripts step by step.

### Favorite Key Shortcuts
- **`Ctrl + P`**: Quick file navigation
- **`Ctrl + Shift + P`**: Open command palette to access all available commands based on the current context.
- **`Ctrl + /`**: Toggle line comment, swiftly enabling or disabling code lines for testing variations.
- **`Shift + Alt + F`**: Format the entire document, keeping code clean and readable.

## Part 2: Functional Programming

Functional programming (FP) is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. Here's how FP principles were incorporated into the project:

### Functional Programming Principles Applied

- **Immutable Data Structures**: Wherever possible, data structures were kept immutable. This reduces side effects and makes the code easier to understand and predict.
- **Side-Effect-Free Functions**: Functions were designed to perform tasks without causing side effects, which means the function's output depends only on its input and does not alter the state outside its scope.
- **Higher-Order Functions**: Functions that take other functions as arguments or return them as results were used to enhance modularity and reusability.
- **Pure Functions**: Ensured that functions have no side effects and return a value that depends only on their input. This principle was particularly emphasized in data processing functions.


## Conclusion

The use of Visual Studio Code as an IDE and the integration of functional programming principles significantly contributed to the productivity and quality of the Call Type Predictor project. These tools and methodologies supported a robust, efficient, and error-resistant development process.

---