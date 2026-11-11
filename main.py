import matplotlib.pyplot as plt
import numpy as np
from fontTools.varLib.models import nonNone


# FUNÇÕES DE GERAÇÃO DE SINAIS
def generate_NRZ_unipolar_signal(string):
    bits = np.array([int(bit) for bit in string])
    return bits

def generate_NRZ_polar_signal(string):
    bits = np.array([int(bit) for bit in string])
    for i in range(len(bits)):
        if bits[i] == 0:
            bits[i] = -1
    return bits

def generate_manchester_signal(string):
    bits = np.array([int(bit) for bit in string])
    signal = []
    for bit in bits:
        if bit == 0:
            signal.extend([1, -1])
        else:
            signal.extend([-1, 1])
    return np.array(signal)

#FUNÇÕES DE GERAÇÃO DE MODULAÇÃO
def generate_ASK_modulated_signal(string):
    bits = np.array([int(bit) for bit in string])
    amplitude = 1
    frequency = 5
    samples_per_bit = 500
    signal = []
    for bit in bits:
        t = np.linspace(0, 1, samples_per_bit, endpoint=False)
        if bit == 1:
            wave = amplitude * np.sin(2 * np.pi * frequency * t)
        else:
            wave = np.zeros(samples_per_bit)
        signal.extend(wave)
    return np.array(signal)

def generate_FSK_modulated_signal(string):
    bits = np.array([int(bit) for bit in string])

    amplitude = 1
    frequency_0 = 2
    frequency_1 = 5
    samples_per_bit = 500

    signal = []

    for bit in bits:
        t = np.linspace(0, 1, samples_per_bit, endpoint=False)
        if bit == 0:
            wave = amplitude * np.sin(2 * np.pi * frequency_0 * t)
        else:
            wave = amplitude * np.sin(2 * np.pi * frequency_1 * t)
        signal.extend(wave)
    return np.array(signal)

def generate_BPSK_modulated_signal(string):
    bits = np.array([int(bit) for bit in string])
    amplitude = 1
    frequency = 5
    samples_per_bit = 500
    signal = []

    for bit in bits:
        t = np.linspace(0, 1, samples_per_bit, endpoint=False)
        if bit == 0:
            wave = amplitude * np.sin(2 * np.pi * frequency * t)
        else:
            wave = -amplitude * np.sin(2 * np.pi * frequency * t)
        signal.extend(wave)
    return np.array(signal)


# FUNÇÕES DE GERAÇÃO DE GRÁFICOS
def generate_graph_NRZ_unipolar(string):
    if len(string) < 16:
        return "String is too short, please enter a string with more than 16 characters."
    for i in range(len(string)):
        if string[i] != '0' and string[i] != '1':
            return "Invalid input, please enter a binary string."

    signal = generate_NRZ_unipolar_signal(string)
    times = []
    for i in range(len(signal)):
        times.append(i)


    fig, ax = plt.subplots(figsize=(12, 4))
    ax.step(times, signal, where='post', linewidth=2)
    ax.set_title("NRZ Unipolar Encoding")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude (V)")
    ax.set_ylim(-0.1, 1.2)
    ax.set_yticks([0, 1])
    ax.set_xticks(times)
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.show()
    return None


def generate_graph_NRZ_polar(string):
    if len(string) < 16:
        return "String is too short, please enter a string with more than 16 characters."
    for i in range(len(string)):
        if string[i] != '0' and string[i] != '1':
            return "Invalid input, please enter a binary string."

    signal = generate_NRZ_polar_signal(string)
    times = []
    for i in range(len(signal)):
        times.append(i)


    fig, ax = plt.subplots(figsize=(12, 4))
    ax.step(times, signal, where='post', linewidth=2)
    ax.set_title("NRZ Polar Encoding")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude (V)")
    ax.set_ylim(-1.2, 1.2)
    ax.set_yticks([-1, 0, 1])
    ax.set_xticks(times)
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.show()
    return None


def generate_manchester_signal(string):

    bits = np.array([int(bit) for bit in string])
    signal = []

    for bit in bits:
        if bit == 0:
            signal.extend([1, -1])
        else:
            signal.extend([-1, 1])

    return np.array(signal)


def generate_graph_manchester(string):
    if len(string) < 16:
        return "String is too short, please enter a string with more than 16 characters."
    for bit in string:
        if bit != '0' and bit != '1':
            return "Invalid input, please enter a binary string."

    bits = [int(bit) for bit in string]
    signal = generate_manchester_signal(string)
    times = []
    for i in range(len(bits)):
        times.extend([i, i + 0.5])

    times.append(len(bits))
    signal = np.append(signal, signal[-1])
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.step(times, signal, where='post', linewidth=2)
    ax.set_title("Manchester Encoding")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude (V)")
    ax.set_ylim(-1.2, 1.2)
    ax.set_yticks([-1, 0, 1])
    ax.set_xticks(range(len(bits) + 1))
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.show()
    return None

def generate_graph_ASK(string):
    if len(string) < 16:
        return "String is too short, please enter a string with more than 16 characters."

    for i in range(len(string)):
        if string[i] != '0' and string[i] != '1':
            return "Invalid input, please enter a binary string."

    signal = generate_ASK_modulated_signal(string)
    times = np.linspace(0, len(string), len(signal), endpoint=False)

    fig, ax = plt.subplots(figsize=(20, 4))
    ax.plot(times, signal, linewidth=1.5)
    ax.set_title("ASK Modulation")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude (V)")
    ax.set_ylim(-1.2, 1.2)
    ax.set_xticks(np.arange(len(string) + 1))
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.show()
    return None

def generate_graph_FSK(string):
    if len(string) < 16:
        return "String is too short, please enter a string with more than 16 characters."
    for i in range(len(string)):
        if string[i] != '0' and string[i] != '1':
            return "Invalid input, please enter a binary string."

    signal = generate_FSK_modulated_signal(string)
    times = np.linspace(0, len(string), len(signal), endpoint=False)

    fig, ax = plt.subplots(figsize=(20, 4))
    ax.plot(times, signal, linewidth=1.5)
    ax.set_title("FSK Modulation")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude (V)")
    ax.set_ylim(-1.2, 1.2)
    ax.set_xticks(np.arange(len(string) + 1))
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.show()
    return None

def generate_graph_BPSK(string):
    if len(string) < 16:
        return "String is too short, please enter a string with more than 16 characters."
    for i in range(len(string)):
        if string[i] != '0' and string[i] != '1':
            return "Invalid input, please enter a binary string."
    signal = generate_BPSK_modulated_signal(string)
    times = np.linspace(0, len(string), len(signal), endpoint=False)

    fig, ax = plt.subplots(figsize=(20, 4))
    ax.plot(times, signal, linewidth=1.5)
    ax.set_title("BPSK Modulation")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude (V)")
    ax.set_ylim(-1.2, 1.2)
    ax.set_xticks(np.arange(len(string) + 1))
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.show()
    return None

# MAIN.PY
if __name__ == '__main__':
    generate_graph_NRZ_unipolar("10101010101010101")
    generate_graph_NRZ_polar("10101010101010101")
    generate_graph_manchester("10101010101010101")
    generate_graph_ASK("00000000111111101")
    generate_graph_FSK("00000000111111101")
    generate_graph_BPSK("00000000111111101")