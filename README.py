# Deskripsi
RSA (Rivest–Shamir–Adleman) adalah algoritma kriptografi kunci publik yang digunakan untuk mengamankan proses pertukaran data. RSA bekerja menggunakan dua kunci berbeda, yaitu public key untuk proses enkripsi dan private key untuk proses dekripsi. Keamanan RSA didasarkan pada kesulitan faktorisasi bilangan prima yang sangat besar.  

Dalam implementasinya, RSA banyak digunakan pada sistem keamanan digital seperti SSL/TLS, tanda tangan digital, serta berbagai protokol keamanan untuk melindungi informasi dari akses yang tidak sah.

## Fungsi utama
Program memiliki beberapa fungsi utama, yaitu:

• Membuat pasangan kunci RSA (Public Key dan Private Key)
• Mengenkripsi pesan (plaintext) menjadi ciphertext
• Mendekripsi ciphertext kembali menjadi plaintext

## Langkah - Langkah
Program bekerja dengan langkah-langkah berikut:

1. Pengguna memasukkan dua bilangan prima `p` dan `q`
2. Program menghitung nilai `n = p x q`
3. Program menghitung nilai `φ(n) = (p-1)(q-1)`
4. Program memilih nilai `e` yang relatif prima terhadap `φ(n)`
5. Program menghitung nilai `d` sebagai kunci privat
6. Program menampilkan pasangan public key dan private key
7. Pengguna dapat memilih proses enkripsi atau deskripsi

# Cara Menjalankan Program
### 1. Persiapan

Pastikan hal berikut ini sudah terinstall:
- Python sudah terinstal
- File program RSA sudah diunduh atau di-clone dari repository
- File program disimpan dengan nama rsa.py

### 2. Masuk ke Folder Program
Buka Terminal atau Command Prompt, lalu masuk ke folder tempat file program berada.
Contoh:
```
cd nama-folder
```

### 3. Menjalankan Program 
Setelah berada di folder program, jalankan perintah berikut:
```
python rsa.py
```

### 4. Menggunakan Program
Setelah program dijalankan, masukkan nilai bilangan prima yang diminta oleh program.

## Contoh Input:
Masukkan bilangan prima p: 17
Masukkan bilangan prima q: 11

### Program akan menampilkan:
```
Public Key (e, n) = (7, 187)
Private Key (d, n) = (23, 187)
```

`Untuk enkripsi:`
Pilih menu: 1
Masukkan plaintext: halo
Program akan mengubah plaintext menjadi ciphertext

### Program akan menampilkan:
```
Pilih menu: 1
Masukkan plaintext: 8

Ciphertext: 134
```

`Untuk deskripsi:`
Pilih menu: 2
Masukkan ciphertext: 134
Masukkan kunci privat d: 23
Masukkan nilai n: 187
Program akan menampilkan plaintext kembali.

## Program

```
Masukkan bilangan prima p: 17
Masukkan bilangan prima q: 11

Public Key (e, n) = (7, 187)
Private Key (d, n) = (23, 187)

Pilih menu:
1. Enkripsi
2. Dekripsi

Pilih menu: 1
Masukkan plaintext: 8
Ciphertext: 134

Pilih menu: 2
Masukkan ciphertext: 134
Masukkan kunci privat d: 23
Masukkan nilai n: 187
Plaintext: 8
``
