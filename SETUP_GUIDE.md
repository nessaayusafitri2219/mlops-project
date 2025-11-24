# 🚀 Setup Guide - MLOps Project

## LANGKAH 1: Setup Docker Hub

### 1.1 Daftar Docker Hub (jika belum punya)
1. Buka: https://hub.docker.com/signup
2. Email: nessaayusafitri2219@gmail.com
3. Buat username (contoh: `nessaayusafitri` atau `nessaayu`)
4. Verifikasi email

### 1.2 Buat Access Token
1. Login ke Docker Hub: https://hub.docker.com
2. Klik profile → **Account Settings** → **Security**
3. Klik **"New Access Token"**
4. Token name: `github-actions`
5. **COPY TOKEN** yang muncul dan simpan!

---

## LANGKAH 2: Setup GitHub Secrets

### 2.1 Buka Settings
1. Buka: https://github.com/nessaayusafitri2219/mlops-project/settings/secrets/actions
2. Atau: Repository → Settings → Secrets and variables → Actions

### 2.2 Tambahkan Secret #1
1. Klik **"New repository secret"**
2. Name: `DOCKER_USERNAME`
3. Secret: (username Docker Hub Anda, contoh: `nessaayusafitri`)
4. Klik **"Add secret"**

### 2.3 Tambahkan Secret #2
1. Klik **"New repository secret"** lagi
2. Name: `DOCKER_PASSWORD`
3. Secret: (paste Personal Access Token dari Docker Hub)
4. Klik **"Add secret"**

**✅ Hasil:** Anda harus punya 2 secrets:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

---

## LANGKAH 3: Jalankan GitHub Actions

### 3.1 Trigger Workflow
1. Buka: https://github.com/nessaayusafitri2219/mlops-project/actions
2. Klik workflow **"MLOps CI/CD Pipeline"**
3. Klik **"Run workflow"** → pilih `main` branch → **"Run workflow"**

### 3.2 Tunggu Workflow Selesai (±5-10 menit)
- Train model ✅
- Evaluate model ✅
- Build Docker image ✅
- Push to Docker Hub ✅

### 3.3 Screenshot
**📸 SCREENSHOT #1:** Ambil screenshot saat workflow berhasil (centang hijau semua)

---

## LANGKAH 4: Install Docker Desktop

### 4.1 Download
- Windows: https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe
- Atau: https://www.docker.com/products/docker-desktop/

### 4.2 Install
1. Jalankan installer
2. Enable WSL 2 feature jika diminta
3. **Restart komputer**

### 4.3 Verify
```powershell
docker --version
docker-compose --version
```

---

## LANGKAH 5: Jalankan Monitoring Lokal

### 5.1 Start Services
```powershell
cd C:\Users\62813\Downloads\MlOps
docker-compose up -d
```

### 5.2 Tunggu 1-2 menit, lalu cek status
```powershell
docker-compose ps
```

Semua service harus status **"Up"**:
- api
- prometheus
- grafana
- alertmanager

---

## LANGKAH 6: Akses dan Screenshot

### 📸 SCREENSHOT #2 - Grafana Dashboard
1. Buka: http://localhost:3000
2. Login: `admin` / `admin` (skip password change)
3. Klik **"+"** → **"Import dashboard"**
4. Klik **"Upload JSON file"** → pilih `grafana-dashboard.json`
5. Klik **"Load"** → **"Import"**
6. **Screenshot dashboard (HARUS ADA NAMA "Nessa ayu safitri" di title)**

### 📸 SCREENSHOT #3 - Prometheus Targets
1. Buka: http://localhost:9090
2. Klik **Status** → **Targets**
3. Screenshot (pastikan semua target UP)

### 📸 SCREENSHOT #4 - API Response
1. Buka terminal baru
2. Jalankan:
```powershell
# Test health endpoint
curl http://localhost:8000/health

# Test metrics endpoint
curl http://localhost:8000/metrics

# Test prediction (jika ada endpoint predict)
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}"
```
3. Screenshot response

### 📸 SCREENSHOT #5 - Docker Images
```powershell
docker images | Select-String "mlops"
```

### 📸 SCREENSHOT #6 - MLflow (Optional - jika ada)
1. Buka: http://localhost:5000
2. Screenshot experiments

---

## LANGKAH 7: Submit Tugas

### 7.1 Upload Screenshots ke Google Drive
1. Buat folder: `MLOps Screenshots`
2. Upload semua screenshot
3. Set folder menjadi **"Anyone with the link can view"**
4. Copy link folder

### 7.2 Checklist Sebelum Submit
- [ ] Repository GitHub public
- [ ] Workflow GitHub Actions berhasil (screenshot)
- [ ] Grafana dashboard dengan nama "Nessa ayu safitri" (screenshot)
- [ ] Prometheus metrics berjalan (screenshot)
- [ ] API serving response (screenshot)
- [ ] Docker images tersedia (screenshot)
- [ ] README.md lengkap dengan username Dicoding

### 7.3 Submit ke Dicoding
Submission berisi:
- **GitHub Repository URL:** https://github.com/nessaayusafitri2219/mlops-project
- **Google Drive Screenshots:** (link folder Anda)
- **Username Dicoding:** Nessa ayu safitri

---

## ⚠️ Troubleshooting

### Workflow Gagal
- Cek apakah secrets sudah benar
- Lihat log error di GitHub Actions
- Pastikan token Docker Hub masih valid

### Docker Compose Error
```powershell
# Stop semua container
docker-compose down

# Hapus container lama
docker system prune -a

# Start ulang
docker-compose up -d
```

### Port Already in Use
```powershell
# Cek port yang digunakan
netstat -ano | findstr :8000
netstat -ano | findstr :3000
netstat -ano | findstr :9090

# Kill process jika perlu
Stop-Process -Id <PID> -Force
```

---

## 📞 Kontak
- Email: nessaayusafitri2219@gmail.com
- GitHub: https://github.com/nessaayusafitri2219

**Good luck! 🚀**
