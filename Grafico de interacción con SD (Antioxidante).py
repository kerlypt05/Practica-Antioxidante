# Grafico de interacción con SD (errorbar) Kerly palacios | Laura Sala

import matplotlib.pyplot as plt
import numpy as np

# Data
mediadores = ["NF-κB", "Nrf2"]

means = {
    "NT": [0.923, 0.978],
    "t-BOOH": [2.066, 0.397],
    "ZN + t-BOOH": [1.272, 1.465],
    "ZN(B) + t-BOOH": [1.403, 1.445],
    "ZN-N(B) + t-BOOH": [0.699, 1.744]
}

sd = {
    "NT": [0.128, 0.039],
    "t-BOOH": [0.215, 0.016],
    "ZN + t-BOOH": [0.309, 0.072],
    "ZN(B) + t-BOOH": [0.273, 0.419],
    "ZN-N(B) + t-BOOH": [0.097, 0.121]
}

x = np.arange(len(mediadores))

plt.figure(figsize=(8,6))

for tratamiento in means:
    plt.errorbar(
        x,
        means[tratamiento],
        yerr=sd[tratamiento],
        marker='o',
        linewidth=2,
        capsize=4,
        label=tratamiento
    )

plt.xticks(x, mediadores)
plt.xlabel("Mediador")
plt.ylabel("Expresión génica relativa normalizada (2⁻ΔΔCt)")
plt.title("Interacción tratamiento × mediador en condiciones de estrés oxidativo (t-BOOH)")
plt.legend(frameon=False)
plt.grid(True, linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()
