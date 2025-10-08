import sys
import time
import argparse

Nama = "Favian Rafiq Athallah"
Nama_panggilan = "Favian"
NIM = 1202407019
Alamat = "Nusukan , Banjarsari , Surakarta"
Fakultas = "Sains dan Teknologi"
Jurusan = "Teknik Informatika"
Universitas = "Muhammadiyah PKU Surakarta"
Agama = "Islam"
Jenis_kelamin = "Laki-laki"
Status = "Mahasiswa"
Kegiatan_lain = "Nyocol coklat"
Motivasi = (
    "Pertumbuhan sejati dimulai saat kita berani menerima kelemahan diri sendiri"
)
Ketik = [
    f"Nama           : {Nama}",
    f"Nama Panggilan : {Nama_panggilan}",
    f"NIM            : {NIM}",
    f"Alamat         : {Alamat}",
    f"fakultas       : {Fakultas}",
    f"Universitas    : {Universitas}",
    f"Jurusan        : {Jurusan}",
    f"Agama          : {Agama}",
    f"Jenis Kelamin  : {Jenis_kelamin}",
    f"Status         : {Status}",
    f"kegiatan lain  : {Kegiatan_lain}"
    "",
    "Motivasi       :",
]

max_len = 70
mot_words = Motivasi.split()
mot_lines = []
cur = ""
for w in mot_words:
    if len(cur) + 1 + len(w) <= max_len:
        cur = (cur + " " + w).strip()
    else:
        mot_lines.append(cur)
        cur = w
if cur:
    mot_lines.append(cur)
Ketik.extend([f"  {line}" for line in mot_lines])
Ketik.append("")
COLOR_TITLE = "\033[1;36m"   
COLOR_KEY   = "\033[1;33m"   
COLOR_RESET = "\033[0m"

def type_write(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def fancy_line(line, delay, use_color=True):
    if not use_color or ":" not in line:
        type_write(line, delay)
        return

    key, val = line.split(":", 1)
    for ch in COLOR_KEY + key + COLOR_RESET + ":":
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if val.startswith(" "):
        sys.stdout.write(" ")
        sys.stdout.flush()
        time.sleep(delay)
        val = val[1:]
    for ch in val:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def main():
    parser = argparse.ArgumentParser(description="Ketik Biodata Favian Rafiq Athallah.")
    parser.add_argument("--speed", type=float, default=0.03, help="Delay per karakter (detik)")
    parser.add_argument("--no-color", action="store_true", help="Matikan warna ANSI")
    parser.add_argument("--fast", action="store_true", help="Mode cepat (speed = 0.005)")
    args = parser.parse_args()

    delay = 0.005 if args.fast else max(0.0, args.speed)
    use_color = not args.no_color

    bIODATA = "== Biodata Favian Rafiq Athallah =="

    if use_color:
        for ch in COLOR_TITLE + bIODATA + COLOR_RESET:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n\n")
        sys.stdout.flush()
    else:
        type_write(bIODATA, delay)
        sys.stdout.write("\n")

    for line in Ketik:
        fancy_line(line, delay, use_color)
        time.sleep(delay * 6)

    type_write("Terimakasih semua", delay * 1.0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write("\n[Dibatalkan]\n")
        sys.exit(0)
