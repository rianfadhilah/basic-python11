try:
    coba = int(input("Masukkan Angka: "))
except ValueError:
    print("Proggram error")
except KeyboardInterrupt:
    print("Proggram dihentikan")
else:
    print(f"angka anda adalah {coba}")
finally:
    print("program selesai")