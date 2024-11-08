import pandas as pd

# Definisikan nama sumber dan tujuan
sumber = ['Sumber 1', 'Sumber 2', 'Sumber 3', 'Demand']
tujuan = ['Tujuan 1', 'Tujuan 2', 'Tujuan 3', 'Tujuan 4', 'Supply']

# Definisikan biaya pengangkutan dalam bentuk matriks
biaya = [
    [8, 6, 10, 9, 20],  # Biaya dari Sumber 1 ke masing-masing Tujuan + Supply
    [9, 12, 13, 7, 25], # Biaya dari Sumber 2 ke masing-masing Tujuan + Supply
    [14, 9, 16, 5, 15], # Biaya dari Sumber 3 ke masing-masing Tujuan + Supply
    [15, 20, 10, 15, 0]  # Baris untuk Demand
]

# Buat DataFrame menggunakan pandas
tabel_biaya = pd.DataFrame(biaya, index=sumber, columns=tujuan)

print("Tabel Biaya (Permasalahan Transportasi Seimbang):")
print(tabel_biaya)

# Identifikasi least cost pada setiap kolom (kecuali kolom 'Supply' dan baris 'Demand')
least_cost_indices = {}
for col in tujuan[:-1]:  # Exclude the 'Supply' column
    col_values = tabel_biaya.loc[sumber[:-1], col]  # Exclude the 'Demand' row
    least_cost_index = col_values.idxmin()
    least_cost_indices[col] = least_cost_index

print("\nLeast cost pada setiap kolom:")
for col, idx in least_cost_indices.items():
    print(f"Kolom {col}: {idx} dengan biaya {tabel_biaya.loc[idx, col]}")
