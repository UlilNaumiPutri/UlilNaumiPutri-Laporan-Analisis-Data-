import pandas as pd
import matplotlib.pyplot as plt

# Membaca file CSV
data = pd.read_csv("nilai_siswa.csv")

# Menampilkan data awal
print("=== Data Nilai Siswa ===")
print(data)

# Menghitung rata-rata per mapel
rata_rata = data.groupby("Mapel")["Nilai"].mean()
print("\n=== Rata-rata Nilai per Mapel ===")
print(rata_rata)

# Membuat grafik batang rata-rata nilai
plt.figure(figsize=(8,5))
rata_rata.plot(kind='bar', color='skyblue')
plt.title("Rata-rata Nilai Siswa per Mapel")
plt.ylabel("Nilai Rata-rata")
plt.xlabel("Mata Pelajaran")
plt.show()

# Menampilkan boxplot untuk melihat sebaran nilai
plt.figure(figsize=(8,5))
data.boxplot(column="Nilai", by="Mapel", grid=False)
plt.title("Sebaran Nilai per Mapel")
plt.suptitle("")
plt.xlabel("Mata Pelajaran")
plt.ylabel("Nilai")
plt.show()
