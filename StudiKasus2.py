import numpy as np

np.random.seed(42) 
Nilaiujian = np.random.randint(50, 101, size=30)
Nilaiurutkan = np.sort(Nilaiujian) [::-1]
Limanilaiterbesar = Nilaiurutkan[:5]

print("Seluruh Nilai Ujian (Dari Terbesar ke Terkecil):")
print(Nilaiurutkan)
print("\n5 Nilai Ujian Terbesar:")
print(Limanilaiterbesar)