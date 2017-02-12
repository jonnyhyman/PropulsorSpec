
N1 = [125,                  # Thrust(N)
      3.65,                 # Power(kW)
      0.86177706194178263E-01, # ExitVelocity(Mach) # 0.086
      0.2,                  # Radius(m)
      2500,                 # RPM
      14,           	    # Blades
      99.8                 # Power Efficiency
      ]

N2 = [50,
      1.65,
      0.74141392429965688E-01, # 0.074
      0.147,
      5000,
      12,
      88.1
      ]

N3 = [94.00,
      2.94,
      0.79539312089252273E-01, # 0.08
      0.187,
      7600,
      4,
      80.2
      ]

N4 = [94.00,
      3.05,
      0.77458461924095584E-01, #  0.08
      0.193,
      6550,
      5,
      83.3
      ]

Ns = [N1,N2,N3,N4,N4,N4] # N4 dupes OK because inflow ~= outflow

Total_Thrust =0
Total_Power  =0

for n in range(len(Ns)):
    Total_Thrust += Ns[n][0]
    Total_Power  += Ns[n][1]

Total_Effectiveness = Total_Thrust/Total_Power

print("Total Thrust=",Total_Thrust)
print("Total Power=",Total_Power)
print("Total Effectiveness=",Total_Effectiveness)
