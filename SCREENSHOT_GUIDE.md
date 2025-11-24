# 📸 PANDUAN SCREENSHOT UNTUK PENGUMPULAN TUGAS MLOPS

**Nama:** Nessa Ayu Safitri
**Username Dicoding:** Nessa ayu safitri
**Repository:** https://github.com/nessaayusafitri2219/mlops-project

---

## ✅ SCREENSHOT WAJIB:

### 1️⃣ GitHub Actions Workflow (KRITERIA 3 - WAJIB)

**URL:** https://github.com/nessaayusafitri2219/mlops-project/actions

**Yang harus terlihat:**
- ✅ Workflow name: "MLOps CI/CD Pipeline"
- ✅ Status: HIJAU/SUCCESS (centang hijau)
- ✅ Semua steps completed (Train, Show, Upload artifacts)
- ✅ Commit message terlihat
- ✅ Branch: main

**Cara screenshot:**
1. Buka link Actions di atas
2. Klik workflow yang HIJAU (centang hijau)
3. Screenshot FULL PAGE yang menampilkan:
   - Judul workflow
   - Status hijau
   - Semua steps expanded (Train, Show, Upload)
   - Timestamp

---

### 2️⃣ GitHub Repository Overview (WAJIB)

**URL:** https://github.com/nessaayusafitri2219/mlops-project

**Yang harus terlihat:**
- ✅ Repository name: "mlops-project"
- ✅ Owner: nessaayusafitri2219
- ✅ Status: Public
- ✅ README.md terbuka yang menampilkan:
  - Username Dicoding: "Nessa ayu safitri"
  - Struktur project
  - Deskripsi

**Cara screenshot:**
1. Buka repository
2. Scroll ke README
3. Screenshot yang menampilkan repo header + README dengan nama Anda

---

### 3️⃣ Model Artifacts (KRITERIA 3 - WAJIB)

**URL:** https://github.com/nessaayusafitri2219/mlops-project/actions (workflow yang sukses)

**Yang harus terlihat:**
- ✅ Artifacts section di workflow
- ✅ "trained-model" artifact uploaded
- ✅ Size file terlihat

**ATAU** screenshot local file:
```powershell
cat models/metrics.json
```

**Yang harus terlihat:**
- accuracy, precision, recall, f1_score dengan nilai

---

### 4️⃣ Workflow File (OPSIONAL - menunjukkan dibuat dari nol)

**URL:** https://github.com/nessaayusafitri2219/mlops-project/blob/main/.github/workflows/mlops-pipeline.yml

**Yang harus terlihat:**
- ✅ Workflow YAML file
- ✅ Jobs: train, install, upload
- ✅ Tidak menggunakan template

---

## 🐳 SCREENSHOT DOCKER/MONITORING (KRITERIA 4):

### 5️⃣ API Serving (BASIC LEVEL)

**Jika Docker BELUM terinstall:**

Option A - Test lokal dengan Python:
```powershell
# Terminal 1 - Start API
python app.py

# Terminal 2 - Test endpoint
Invoke-WebRequest http://localhost:8000/health
```

Screenshot response yang menampilkan status 200 OK

Option B - Screenshot code app.py:
```powershell
code app.py
```
Screenshot FastAPI code dengan endpoints

---

### 6️⃣ Grafana Dashboard (SKILLED LEVEL - jika Docker installed)

**URL:** http://localhost:3000 (setelah `docker-compose up -d`)

**Yang harus terlihat:**
- ✅ Dashboard title: "MLOps Monitoring Dashboard - Nessa ayu safitri"
- ✅ Metrics panels (API requests, duration, predictions)
- ✅ Grafana header dengan logo
- ✅ Time range selector

**Cara:**
1. Install Docker Desktop
2. Run: `docker-compose up -d`
3. Buka http://localhost:3000
4. Login: admin / admin
5. Import dashboard dari `grafana-dashboard.json`
6. Screenshot full dashboard

---

### 7️⃣ Prometheus Metrics (SKILLED LEVEL - jika Docker installed)

**URL:** http://localhost:9090

**Yang harus terlihat:**
- ✅ Prometheus UI
- ✅ Status → Targets (semua UP)
- ✅ Metrics terlihat (api_requests_total, dll)

---

### 8️⃣ Docker Compose Services (SKILLED LEVEL - jika Docker installed)

**Command:**
```powershell
docker-compose ps
```

**Yang harus terlihat:**
- ✅ Services running: api, prometheus, grafana, alertmanager
- ✅ Status: Up
- ✅ Ports terlihat

---

## 📝 SCREENSHOT ALTERNATIF (jika Docker TIDAK installed):

Karena Docker belum terinstall, Anda bisa screenshot:

### A. File Konfigurasi Monitoring:

1. **prometheus.yml**
   ```powershell
   cat prometheus.yml
   ```

2. **grafana-dashboard.json** (dengan nama Anda)
   ```powershell
   cat grafana-dashboard.json | Select-String "Nessa"
   ```

3. **alert_rules.yml**
   ```powershell
   cat alert_rules.yml
   ```

### B. Project Structure:
```powershell
tree /F
# ATAU
Get-ChildItem -Recurse | Select-Object FullName
```

Tunjukkan struktur folder lengkap dengan semua file monitoring.

---

## 📋 CHECKLIST SCREENSHOT MINIMAL (tanpa Docker):

- [ ] **1. GitHub Actions - Workflow HIJAU** ✅ WAJIB
- [ ] **2. GitHub Repository + README** ✅ WAJIB
- [ ] **3. Model Artifacts/Metrics** ✅ WAJIB
- [ ] **4. Workflow YAML file** ✅ WAJIB
- [ ] **5. app.py code** (pengganti API serving)
- [ ] **6. grafana-dashboard.json** (tunjukkan nama Anda)
- [ ] **7. prometheus.yml** (tunjukkan config)
- [ ] **8. Project structure** (tree/ls)

---

## 🚀 LANGKAH SUBMIT:

1. **Ambil semua screenshot** (minimal 4 wajib)
2. **Buat folder Google Drive:** "MLOps Screenshots - Nessa Ayu Safitri"
3. **Upload semua screenshot** dengan nama jelas:
   - `01-github-actions-success.png`
   - `02-repository-readme.png`
   - `03-model-metrics.png`
   - `04-workflow-yaml.png`
   - `05-app-code.png`
   - `06-grafana-dashboard.png`
   - `07-prometheus-config.png`
4. **Set sharing:** "Anyone with the link can view"
5. **Copy link Google Drive**
6. **Submit ke Dicoding:**
   - GitHub URL: https://github.com/nessaayusafitri2219/mlops-project
   - Google Drive: (link Anda)
   - Username: Nessa ayu safitri

---

## ⚠️ PENTING:

- **GitHub Actions HARUS HIJAU** - ini wajib!
- **Nama "Nessa ayu safitri" harus terlihat** di README atau dashboard
- Screenshot harus **jelas dan full page**
- Semua screenshot dalam **1 folder Google Drive**

---

**Mulai dari mana?**

1. Buka https://github.com/nessaayusafitri2219/mlops-project/actions
2. Cek apakah workflow sudah HIJAU
3. Jika HIJAU → Screenshot!
4. Jika MERAH → Kabari saya untuk perbaikan

**Good luck!** 🎉
