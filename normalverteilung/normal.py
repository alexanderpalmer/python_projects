import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Daten für die Äpfel, die jedes Kind gegessen hat
kinder = ['Kind 1', 'Kind 2', 'Kind 3', 'Kind 4', 'Kind 5']
aepfel = [3, 3, 4, 2, 3]

# Berechne den Durchschnitt
durchschnitt = np.mean(aepfel)

# Bereite die Daten für die Diagramme vor
data = pd.DataFrame({'Kinder': kinder, 'Äpfel': aepfel})

# Erstelle die Diagramme
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

standardabweichung = np.std(aepfel)

# Erstelle die Diagramme mit der Visualisierung der Standardabweichung
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# 1. Balkendiagramm mit Fehlerbalken (Standardabweichung)
axs[0].bar(kinder, aepfel, color='lightblue', yerr=standardabweichung, capsize=5)
axs[0].axhline(y=durchschnitt, color='red', linestyle='--', label=f'Durchschnitt = {durchschnitt}')
axs[0].set_title('Balkendiagramm: Anzahl der gegessenen Äpfel mit Standardabweichung')
axs[0].set_ylabel('Anzahl der Äpfel')
axs[0].legend()

# 2. Liniendiagramm mit schattierter Standardabweichung
axs[1].plot(kinder, aepfel, marker='o', color='orange', label='Gegessene Äpfel')
axs[1].axhline(y=durchschnitt, color='red', linestyle='--', label=f'Durchschnitt = {durchschnitt}')
axs[1].fill_between(kinder, durchschnitt - standardabweichung, durchschnitt + standardabweichung, color='gray', alpha=0.2,
                    label=f'Standardabweichung ±{round(standardabweichung, 2)}')
axs[1].set_title('Liniendiagramm: Anzahl der Äpfel mit Standardabweichung')
axs[1].set_ylabel('Anzahl der Äpfel')
axs[1].legend()


# Platzieren der Diagramme
plt.tight_layout()
plt.show()
