# 📋 CHECKLIST PENGUMPULAN TUGAS MLOPS

**Username Dicoding:** Nessa ayu safitri  
**GitHub:** https://github.com/nessaayusafitri2219/mlops-project  
**Email:** nessaayusafitri2219@gmail.com

---

## ✅ YANG SUDAH SELESAI

- [x] Repository GitHub public dibuat
- [x] Code di-push ke GitHub
- [x] Nama & email sudah diisi di README
- [x] Dashboard Grafana sudah ada nama pengguna
- [x] Model trained lokal (model.pkl, metrics.json)
- [x] Struktur project lengkap (CI/CD, monitoring, alerting)

---

## ⏳ YANG HARUS DILAKUKAN

### 1. Setup Docker Hub & GitHub Secrets
**Status:** ⏳ MENUNGGU

**Langkah:**
1. Daftar Docker Hub: https://hub.docker.com/signup
2. Buat Access Token di Docker Hub Security settings
3. Tambahkan GitHub Secrets:
   - URL: https://github.com/nessaayusafitri2219/mlops-project/settings/secrets/actions
   - Secret 1: `DOCKER_USERNAME` (username Docker Hub)
   - Secret 2: `DOCKER_PASSWORD` (token dari Docker Hub)

**Hasil yang diharapkan:**
- ✅ 2 secrets tersimpan di GitHub
- ✅ Siap untuk trigger workflow

---

### 2. Jalankan GitHub Actions Workflow
**Status:** ⏳ MENUNGGU (setelah secrets setup)

**Langkah:**
1. Buka: https://github.com/nessaayusafitri2219/mlops-project/actions
2. Pilih workflow "MLOps CI/CD Pipeline"
3. Klik "Run workflow" → Run workflow
4. Tunggu sampai selesai (±5-10 menit)

**Screenshot yang dibutuhkan:**
- 📸 **SCREENSHOT #1:** Workflow success (semua step hijau)
- 📸 **SCREENSHOT #2:** Job details (train, evaluate, docker build, push)

---

### 3. Install Docker Desktop
**Status:** ⏳ BELUM

**Langkah:**
1. Download: https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe
2. Install dan restart komputer
3. Verify: `docker --version`

**Hasil yang diharapkan:**
- ✅ Docker Desktop berjalan
- ✅ `docker --version` menampilkan versi
- ✅ `docker-compose --version` menampilkan versi

---

### 4. Jalankan Monitoring Stack
**Status:** ⏳ MENUNGGU (setelah Docker terinstall)

**Langkah:**
```powershell
# Start semua service
docker-compose up -d

# Cek status
docker-compose ps

# Lihat logs jika ada error
docker-compose logs
```

**Service yang harus running:**
- api (port 8000)
- prometheus (port 9090)
- grafana (port 3000)
- alertmanager (port 9093)

---

### 5. Ambil Screenshots Monitoring
**Status:** ⏳ MENUNGGU (setelah monitoring running)

#### 📸 SCREENSHOT #3 - Grafana Dashboard
1. Buka: http://localhost:3000
2. Login: admin / admin
3. Import dashboard dari `grafana-dashboard.json`
4. **PENTING:** Screenshot harus menampilkan:
   - Title: "MLOps Monitoring Dashboard - Nessa ayu safitri"
   - Panels: Request rate, Duration, Predictions, etc.
   - Data metrics (jika ada)

#### 📸 SCREENSHOT #4 - Prometheus Targets
1. Buka: http://localhost:9090
2. Klik Status → Targets
3. Screenshot semua targets (harus UP)

#### 📸 SCREENSHOT #5 - API Response
```powershell
# Test API
python test_api.py
```
Screenshot output dari testing

#### 📸 SCREENSHOT #6 - Docker Images
```powershell
docker images
```
Screenshot list images yang sudah di-build

#### 📸 SCREENSHOT #7 - Model Metrics (Optional)
Screenshot file `models/metrics.json` atau MLflow UI

---

### 6. Upload Screenshots & Submit
**Status:** ⏳ MENUNGGU

**Langkah:**
1. Buat folder di Google Drive: "MLOps Screenshots - Nessa Ayu Safitri"
2. Upload semua screenshot (minimal 6 screenshot)
3. Set sharing: "Anyone with the link can view"
4. Copy link folder

**Submit ke Dicoding:**
- Repository URL: https://github.com/nessaayusafitri2219/mlops-project
- Google Drive: [link screenshots]
- Username Dicoding: Nessa ayu safitri

---

## 📊 KRITERIA PENILAIAN

### Kriteria 3: CI/CD ✅
- [x] Repository GitHub public
- [x] Workflow dibuat dari nol (bukan template)
- [ ] Secrets dikonfigurasi
- [ ] Workflow berhasil dijalankan
- [ ] Training → Evaluation → Docker Build → Docker Push
- [ ] Model uploaded ke storage

### Kriteria 4: Serving & Monitoring ✅
- [x] Dashboard Grafana dengan username Dicoding
- [x] Model serving (FastAPI)
- [x] Prometheus metrics (minimal 3)
- [x] Grafana visualization
- [x] Alerting system

**Level yang dicapai:** 
- Basic: ✅ (Serving + Training + Evaluation)
- Skilled: ✅ (+ Docker Build)
- Advanced: ✅ (+ Docker Push + Alerting)

---

## 🚀 PRIORITAS LANGKAH BERIKUTNYA

**PRIORITAS 1 (HARI INI):**
1. ⏳ Setup Docker Hub account
2. ⏳ Setup GitHub Secrets
3. ⏳ Trigger GitHub Actions workflow
4. ⏳ Screenshot workflow success

**PRIORITAS 2 (BESOK - jika Docker belum ready):**
1. ⏳ Install Docker Desktop
2. ⏳ Restart komputer
3. ⏳ Jalankan `docker-compose up -d`
4. ⏳ Ambil semua screenshots monitoring

**PRIORITAS 3 (SUBMIT):**
1. ⏳ Upload screenshots ke Google Drive
2. ⏳ Submit ke Dicoding

---

## 📞 BANTUAN

Jika ada error:
1. Cek log: `docker-compose logs -f`
2. Restart service: `docker-compose restart`
3. Rebuild: `docker-compose up -d --build`

**Questions?** Open issue di GitHub atau contact via email.

---

**Last Updated:** 2025-11-24  
**Status:** 40% Complete - Perlu Docker Hub setup & workflow execution
