# Given values
RA = 43310
RB = 902.2
C = 10e-9  # 10 nF in Farads

# Calculations
tH = 0.693 * (RA + RB) * C
tL = 0.693 * RB * C
T = tH + tL
output_driver_duty_cycle = tL / T
output_waveform_duty_cycle = tH / T
low_to_high_ratio = tL / tH

# Display results
print(f"High Time (tH): {tH} seconds")
print(f"Low Time (tL): {tL} seconds")
print(f"Period (T): {T} seconds")
print(f"Output Driver Duty Cycle: {output_driver_duty_cycle}")
print(f"Output Waveform Duty Cycle: {output_waveform_duty_cycle}")
print(f"Low-to-High Ratio: {low_to_high_ratio}")
