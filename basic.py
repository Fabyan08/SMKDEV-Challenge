# Data untuk Udin
massa_udin_data1 = 78  # kg
tinggi_udin_data1 = 1.69  # m

massa_udin_data2 = 95  # kg
tinggi_udin_data2 = 1.88  # m

# Data untuk Nanang
massa_nanang_data1 = 92  # kg
tinggi_nanang_data1 = 1.95  # m

massa_nanang_data2 = 85  # kg
tinggi_nanang_data2 = 1.76  # m

# Fungsi untuk menghitung BMI
def hitung_bmi(massa, tinggi):
    return massa / (tinggi ** 2)

# Menghitung BMI Udin dan Nanang untuk Data 1
bmi_udin_data1 = hitung_bmi(massa_udin_data1, tinggi_udin_data1)
bmi_nanang_data1 = hitung_bmi(massa_nanang_data1, tinggi_nanang_data1)

# Menghitung BMI Udin dan Nanang untuk Data 2
bmi_udin_data2 = hitung_bmi(massa_udin_data2, tinggi_udin_data2)
bmi_nanang_data2 = hitung_bmi(massa_nanang_data2, tinggi_nanang_data2)

# Membandingkan BMI
udin_lebih_tinggi_data1 = bmi_udin_data1 > bmi_nanang_data1
udin_lebih_tinggi_data2 = bmi_udin_data2 > bmi_nanang_data2

# Menampilkan hasil perbandingan BMI
if udin_lebih_tinggi_data1:
    print(f"BMI Udin ({bmi_udin_data1:.1f}) lebih tinggi dari Nanang ({bmi_nanang_data1:.1f})!")
else:
    print(f"BMI Nanang ({bmi_nanang_data1:.1f}) lebih tinggi dari Udin ({bmi_udin_data1:.1f})!")

if udin_lebih_tinggi_data2:
    print(f"BMI Udin ({bmi_udin_data2:.1f}) lebih tinggi dari Nanang ({bmi_nanang_data2:.1f})!")
else:
    print(f"BMI Nanang ({bmi_nanang_data2:.1f}) lebih tinggi dari Udin ({bmi_udin_data2:.1f})!")
