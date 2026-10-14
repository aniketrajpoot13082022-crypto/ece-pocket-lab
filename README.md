# ⚡ ECE Pocket Lab
### A Mini Electronics Toolkit for Engineering Students

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green)
![Domain](https://img.shields.io/badge/Domain-Electronics-orange)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen)

**ECE Pocket Lab** is a beginner-friendly desktop application developed using Python and Tkinter. It provides a collection of interactive calculators designed to help Electronics and Communication Engineering (ECE) students perform basic electrical calculations and understand fundamental electronics concepts.

Instead of using separate tools for different calculations, users can access three useful electronics utilities through a single graphical interface.

The project combines basic electrical engineering principles with Python programming, graphical user interface development, input validation, and mathematical calculations.

---

## 📌 Table of Contents

1. [Project Overview](#-project-overview)
2. [Why I Built This Project](#-why-i-built-this-project)
3. [Features](#-features)
4. [How Each Calculator Works](#-how-each-calculator-works)
5. [Technologies Used](#-technologies-used)
6. [Application Interface](#-application-interface)
7. [Installation and Setup](#-installation-and-setup)
8. [Example Calculations](#-example-calculations)
9. [Project Structure](#-project-structure)
10. [How the Application Works](#-how-the-application-works)
11. [Testing and Validation](#-testing-and-validation)
12. [Limitations](#-limitations)
13. [Future Improvements](#-future-improvements)
14. [Learning Outcomes](#-learning-outcomes)
15. [Safety Disclaimer](#-safety-disclaimer)
16. [Author](#-author)

---

## 📖 Project Overview

ECE Pocket Lab is a Python-based graphical application that brings together three essential electronics tools:

- **Ohm's Law Calculator:** Calculates voltage, current, resistance, and electrical power.
- **LED Resistor Calculator:** Estimates the series resistance required for an LED circuit.
- **Resistor Colour-Code Decoder:** Determines the resistance and tolerance of a common four-band resistor.

The application uses a dark-themed interface with separate tabs for each tool. Users can enter values, select options, and view calculation results directly in the application window.

The main objective is to make basic electronics calculations more accessible to students who are learning electrical engineering and programming.

### Project Details

| Property | Description |
|---|---|
| Project Name | ECE Pocket Lab |
| Project Type | Desktop application |
| Programming Language | Python |
| GUI Framework | Tkinter |
| Intended Users | ECE students and electronics beginners |
| Primary Purpose | Educational electronics calculations |
| Interface | Dark-themed graphical interface |

---

## 🎯 Why I Built This Project

Electronics students frequently perform calculations involving voltage, current, resistance, LEDs, and resistor colour codes.

Although these calculations can be completed manually, a small application can make them quicker to perform and easier to repeat.

I developed ECE Pocket Lab to explore how programming can be used to solve practical engineering problems.

This project connects classroom concepts with a working software application. It also provides an opportunity to practise Python functions, graphical interfaces, input validation, mathematical expressions, and basic application design.

---

## 🚀 Features

### 1. Ohm's Law Calculator

The Ohm's Law Calculator helps users determine an unknown electrical quantity using the other two required values.

**Capabilities:**

- Calculate voltage using current and resistance.
- Calculate current using voltage and resistance.
- Calculate resistance using voltage and current.
- Calculate electrical power for the selected calculation.
- Display the formula used for the result.
- Validate numerical inputs and report invalid values.

**Example:**

If a circuit has a current of `0.02 A` and a resistance of `220 Ω`, the calculator determines the voltage across the resistor.

**Result:** `4.4 V`

### 2. LED Resistor Calculator

An LED normally requires a series resistor to limit the current flowing through it.

The LED Resistor Calculator estimates a suitable resistance using the supply voltage, LED forward voltage, and desired LED current.

**Capabilities:**

- Accept a supply voltage in volts.
- Accept an LED forward voltage in volts.
- Accept a target current in milliamps.
- Calculate the theoretical resistance.
- Suggest a standard resistor value from the implemented E12 series.
- Estimate the actual current using the suggested resistance.
- Calculate the resistor's power dissipation.
- Suggest a resistor power rating with a basic safety margin.

**Example:**

For a `5 V` supply, a `2 V` LED, and a desired current of `20 mA`, the calculator suggests a `150 Ω` resistor.

The application also estimates the current and power dissipation for that suggested value.

### 3. Resistor Colour-Code Decoder

Many conventional resistors use coloured bands to indicate their resistance and tolerance.

The Colour-Code Decoder allows users to choose the bands of a common four-band resistor and calculate its value.

**Capabilities:**

- Select the first significant digit.
- Select the second significant digit.
- Select the resistance multiplier.
- Select the tolerance band.
- Display the calculated resistance.
- Calculate the upper and lower tolerance limits.
- Display a simple resistor illustration reflecting the selected colours.

**Example:**

A resistor with the bands Brown, Black, Red, and Gold has a nominal resistance of `1 kΩ` with a tolerance of `±5%`.

The corresponding resistance range is `950 Ω` to `1050 Ω`.

---

## 🧮 How Each Calculator Works

### A. Ohm's Law

Ohm's Law describes the relationship between voltage, current, and resistance.

The main equation is:

`V = I × R`

Where:

- `V` = voltage in volts (V)
- `I` = current in amperes (A)
- `R` = resistance in ohms (Ω)

The application uses the following equations:

**To calculate voltage:**

`V = I × R`

**To calculate current:**

`I = V / R`

**To calculate resistance:**

`R = V / I`

Electrical power is calculated using:

`P = V × I`

Where `P` represents power in watts (W).

The program selects the appropriate formula according to the user's choice and displays the calculated result.

### B. LED Series Resistor

The LED calculator uses the voltage remaining after the LED forward voltage drop to determine the required resistor.

The equation is:

`R = (Vs - Vf) / I`

Where:

- `R` = required resistance in ohms
- `Vs` = supply voltage
- `Vf` = LED forward voltage
- `I` = desired LED current in amperes

Since the user enters current in milliamps, the program converts it into amperes:

`I (A) = I (mA) / 1000`

The resistor's power dissipation is calculated using:

`P = (Vs - Vf)² / R`

The program then suggests a preferred resistor value that is not below the calculated resistance.

This is an estimate for a basic series LED circuit. Actual component specifications, supply variations, and operating conditions must also be considered.

### C. Four-Band Resistor Colour Code

For a conventional four-band resistor, the first two bands represent significant digits, the third band is the multiplier, and the fourth band represents tolerance.

The resistance is calculated using:

`Resistance = (First Digit × 10 + Second Digit) × Multiplier`

For example:

- First band: Brown = 1
- Second band: Black = 0
- Third band: Red = ×100
- Fourth band: Gold = ±5%

Therefore:

`Resistance = (1 × 10 + 0) × 100`

`Resistance = 1000 Ω = 1 kΩ`

The tolerance limits are:

`Minimum = Nominal Resistance × (1 - Tolerance / 100)`

`Maximum = Nominal Resistance × (1 + Tolerance / 100)`

For a `1 kΩ ±5%` resistor, the possible nominal tolerance range is `950 Ω` to `1050 Ω`.

---

## 🛠️ Technologies Used

### Python

Python handles the application's calculations, program logic, input processing, and error handling.

### Tkinter

Tkinter is used to create the graphical user interface, including the main application window, buttons, labels, input fields, and tabs.

### ttk

The themed Tkinter widgets provide interface components such as dropdown menus and tab navigation.

### Python Standard Library

The project uses standard Python functionality and does not normally require third-party packages.

---

## 🖥️ Application Interface

ECE Pocket Lab contains a main window with separate tabs for its three calculators.

Each tab provides the inputs and controls needed for its specific function, along with an area where calculation results are displayed.

The interface uses a dark background, contrasting text, highlighted buttons, and a simple layout to keep the tools organised.

**Screenshot:**

<!--
To add your screenshot:
1. Take a screenshot of the running ECE Pocket Lab application.
2. Upload it to the root of this GitHub repository.
3. Name the uploaded image ece-pocket-lab.png.
4. Uncomment the image line below.

![ECE Pocket Lab Application](ece-pocket-lab.png)
-->

---

## 💻 Installation and Setup

### Requirements

- Python 3
- Thonny IDE or another Python editor
- Tkinter support in your Python installation

Tkinter is included with many standard Python installations.

### Step 1: Download the Project

Clone the repository using Git:

```bash
git clone https://github.com/aniketrajpoot13082022-crypto
/ece-pocket-lab.git
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### Step 2: Open the Python File

Open the project folder and locate:

`ece_pocket_lab.py`

Open the file in Thonny or another compatible Python editor.

### Step 3: Run the Application in Thonny

1. Open `ece_pocket_lab.py`.
2. Click the green Run button or press `F5`.
3. Wait for the application window to appear.
4. Select a calculator tab and enter the required values.

### Step 4: Run from a Terminal

Navigate to the folder containing the Python file and execute:

```bash
python ece_pocket_lab.py
```

On systems where Python is invoked using `python3`, use:

```bash
python3 ece_pocket_lab.py
```

If Tkinter is unavailable, install or enable the Tkinter component appropriate for your Python installation.

---

## 🧪 Example Calculations

The following examples can be used to check the expected mathematical results.

| Calculator | Input | Expected Result |
|---|---|---|
| Ohm's Law | Current = 0.02 A, Resistance = 220 Ω | Voltage = 4.4 V |
| LED Resistor | Supply = 5 V, LED = 2 V, Current = 20 mA | Recommended resistance = 150 Ω |
| Colour-Code Decoder | Brown, Black, Red, Gold | 1 kΩ ±5% |

These values provide simple reference cases for checking the application's calculations.

---

## 📁 Project Structure

The repository can be organised as follows:

```text
ece-pocket-lab/
│
├── ece_pocket_lab.py
│   └── Main Python application
│
├── README.md
│   └── Project description and documentation
│
└── ece-pocket-lab.png
    └── Optional screenshot of the application
```

The screenshot file is optional. Upload it only if you want to display the application's interface in the README.

---

## ⚙️ How the Application Works

The program follows a simple input-process-output approach.

### 1. Input

The user enters numerical values or selects options from dropdown menus.

### 2. Processing

Python functions read the supplied values, validate them, and perform the mathematical calculations required by the selected tool.

### 3. Output

The application displays the result in the graphical interface.

### 4. Error Handling

When an input is missing, non-numeric, or invalid for the selected calculation, the application can display an error message instead of attempting to use an invalid value.

This structure makes the program easier to understand and provides a foundation for adding more calculators later.

---

## ✅ Testing and Validation

The application's three main calculators have been run using the following example inputs.

| Test | Input | Expected Output |
|---|---|---|
| Ohm's Law | 0.02 A and 220 Ω | 4.4 V |
| LED Resistor | 5 V, 2 V, 20 mA | 150 Ω |
| Resistor Colour Code | Brown, Black, Red, Gold | 1 kΩ ±5% |

All three example calculations produced the expected results during testing.

Further testing can include invalid text inputs, zero values where they are not permitted, and different combinations of resistor bands and circuit parameters.

---

## ⚠️ Limitations

ECE Pocket Lab is an educational project focused on basic electronics calculations.

- The application does not simulate a complete electrical circuit.
- The LED calculator assumes a simple series LED and resistor arrangement.
- The suggested resistor power rating is an estimate and must be checked against real component specifications.
- The colour-code decoder currently focuses on common four-band resistors rather than every resistor marking system.
- The correctness of a result depends on the values entered by the user and the assumptions used in the calculation.

These limitations provide opportunities for future improvements and more advanced engineering features.

---

## 🔮 Future Improvements

Possible extensions include:

- Adding series and parallel resistance calculators.
- Adding capacitance, reactance, and impedance calculators.
- Supporting additional resistor colour-code formats.
- Adding more visual diagrams of basic electrical circuits.
- Providing unit conversions for common electrical quantities.
- Improving the interface with additional visual feedback.
- Adding automated tests for calculation functions.
- Organising the application into separate Python modules as the project grows.

The goal is to gradually develop ECE Pocket Lab into a more comprehensive educational toolkit for electronics students.

---

## 📚 Learning Outcomes

Developing this project provides practical experience with:

- Python functions and program structure.
- Basic electrical engineering formulas.
- Graphical user interface development using Tkinter.
- Numerical calculations and unit conversions.
- Input validation and exception handling.
- Dropdown menus, buttons, and event-driven programming.
- Testing calculations against known examples.
- Documenting and sharing a software project on GitHub.

This project demonstrates how fundamental engineering concepts can be translated into a small, interactive software application.

---

## 🔒 Safety Disclaimer

This application is intended for learning and demonstration purposes.

Its calculations are not a substitute for engineering verification. Before constructing or powering a circuit, check component datasheets, voltage and current limits, resistor power ratings, circuit conditions, and applicable safety requirements.

---

## 👨‍💻 Author

Created as a personal learning project focused on Python programming and fundamental Electronics and Communication Engineering concepts.

**Project:** ECE Pocket Lab  
**Category:** Electronics / Python / GUI Development

---

### ⚡ Small Tools, Bigger Ideas.

*Exploring electronics through code, one calculation at a time.*
