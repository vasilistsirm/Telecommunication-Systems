import commlib as cl
import matplotlib.pyplot as plt

# Set the time-related parameters
symbol_duration = 1e-6  # Duration of each symbol
samples_per_symbol = 20  # Number of samples per symbol
initial_time = 0  # Initial time
guard_interval = 10 * symbol_duration  # Guard interval duration

# Change the name to see a different waveform
your_name = 'Vasilis Tsirmakos'

# Function to generate QAM waveform
def generate_qam_waveform(name, M):
    # Convert your name to binary
    name_bits = ''.join(format(ord(char), '08b') for char in name)

    # Calculate the required bits for M-QAM
    bits_to_append = (len(name_bits) % int(M ** 0.5)) * '0'
    name_bits = name_bits + bits_to_append

    # QAM constellation
    constellation = cl.qam_constellation(M)

    # Create the waveform and plot
    waveform = cl.digital_signal(TS=symbol_duration, samples_per_symbol=samples_per_symbol,
                                  tinitial=initial_time, tguard=guard_interval, constellation=constellation)

    # Modulate the waveform from input bits
    waveform.modulate_from_bits(name_bits, constellation=constellation)

    # Plot the QAM waveform
    plt.figure()
    waveform.plot(True, M)
    plt.title(f'QAM Waveform for M = {M}')
    plt.title(f'QAM Waveform for M = {M} (Name: {name})')
    plt.show()

# Call the function for M = 4 and M = 16
generate_qam_waveform(your_name, 4)
generate_qam_waveform(your_name, 16)
