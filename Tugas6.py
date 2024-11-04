import numpy as np
import matplotlib.pyplot as plt

# Fungsi simulasi pengisian daya powerbank
def simulate_powerbank_charging(t_max, dt=0.1,
                                initial_capacity=0,
                                max_capacity=10000,
                                charging_current=2000,
                                initial_efficiency=0.95):
    # Inisialisasi parameter
    C0 = initial_capacity
    Cmax = max_capacity
    I = charging_current
    η0 = initial_efficiency
    
    # Inisialisasi array waktu dan kapasitas
    t = np.arange(0, t_max, dt)
    C = np.zeros(len(t))
    η = np.zeros(len(t))
    
    # Kondisi awal
    C[0] = C0
    
    # Simulasi
    for i in range(1, len(t)):
        η[i-1] = η0 * (1 - C[i-1]/Cmax)
        dC = η[i-1] * I * (1 - C[i-1]/Cmax) * dt
        C[i] = min(C[i-1] + dC, Cmax)
    
    return t, C, η

# Fungsi visualisasi hasil simulasi
def plot_results(t, C, η):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Plot Kapasitas
    ax1.plot(t/60, C/100, 'b-', label='Level Baterai')
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.set_title('Pengisian Daya Powerbank')
    ax1.set_ylabel('Kapasitas (%)')
    ax1.legend()
    
    # Plot Efisiensi
    ax2.plot(t/60, η*100, 'r-', label='Efisiensi Charging')
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.set_xlabel('Waktu (jam)')
    ax2.set_ylabel('Efisiensi (%)')
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

# Menjalankan simulasi dengan parameter default dan menampilkan grafik
t, C, η = simulate_powerbank_charging(t_max=18000)  # Simulasi untuk 5 jam (18000 detik)
plot_results(t, C, η)
