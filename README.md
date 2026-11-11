A Python project for generating and visualizing digital signal encoding and modulation techniques using NumPy and Matplotlib.

## Features

The project implements the following techniques:

### Digital Encoding and a graphical representation when the input is 00000000111111101
- **NRZ Unipolar:** Represents binary bits using positive voltage levels and zero.
  <img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/8b334a97-b105-4f09-846b-3e6910341414" />
- **NRZ Polar:** Represents binary bits using positive and negative voltage levels.
  <img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/161d169f-d4bd-4741-a81f-32d8dac1aa9f" />
- **Manchester:** Represents each bit using a transition between two voltage levels.
  <img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/c5be6494-d7a7-4949-8118-e8630d8d714a" />


### Digital Modulation and a graphical representation when the input is 00000000111111101
- **ASK (Amplitude Shift Keying):** Encodes bits by varying the carrier amplitude.
  <img width="2000" height="400" alt="image" src="https://github.com/user-attachments/assets/7cdf22b8-e5dd-4444-98e6-970b4d70c2a7" />
- **FSK (Frequency Shift Keying):** Encodes bits by varying the carrier frequency.
  <img width="2000" height="400" alt="image" src="https://github.com/user-attachments/assets/4ad427f2-fee8-4424-bf9f-b98fdd9a3101" />
- **BPSK (Binary Phase Shift Keying):** Encodes bits by changing the carrier phase.
  <img width="2000" height="400" alt="image" src="https://github.com/user-attachments/assets/c5471a7a-22a5-422a-bf34-c3378316f655" />

## Requirements

- Python 3
- NumPy
- Matplotlib

## Installation

Install the required dependencies:

```bash
pip install numpy matplotlib
```

## Usage

Run the main Python file:

```bash
python main.py
```

The script generates plots for all implemented encoding and modulation techniques using predefined binary strings.

## Input Requirements

- Input must be a binary string containing only `0` and `1`.
- The input must contain at least 16 bits.

## Project Structure

```text
project/
├── main.py
└── README.md
```

## Configuration

Modulation parameters can be adjusted directly in the signal generation functions, including:

- Carrier amplitude
- Carrier frequency
- Number of samples per bit
- FSK frequencies for binary `0` and `1`

## Technologies

- Python
- NumPy
- Matplotlib
