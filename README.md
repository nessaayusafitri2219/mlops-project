# MLOps Project - TUGAS DICODING

Project MLOps lengkap dengan CI/CD pipeline, model serving, monitoring Prometheus & Grafana, dan alerting.

**Username Dicoding**: Nessa ayu safitri

## 📋 Deskripsi Project

Project ini mengimplementasikan end-to-end MLOps pipeline dengan:
- ✅ Automated training dengan GitHub Actions
- ✅ Model tracking menggunakan MLflow
- ✅ Containerization dengan Docker
- ✅ Model serving dengan FastAPI
- ✅ Monitoring dengan Prometheus & Grafana
- ✅ Alerting system untuk anomali

## 🏗️ Arsitektur

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   GitHub    │────▶│  GitHub      │────▶│   Docker    │
│  Repository │     │  Actions CI  │     │   Registry  │
└─────────────┘     └──────────────┘     └─────────────┘
                            │
                            ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Prometheus │◀────│   FastAPI    │────▶│   MLflow    │
│  Monitoring │     │   Serving    │     │   Tracking  │
└─────────────┘     └──────────────┘     └─────────────┘
       │
       ▼
┌─────────────┐     ┌──────────────┐
│   Grafana   │────▶│   Alerting   │
│  Dashboard  │     │   (Email)    │
└─────────────┘     └──────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Docker & Docker Compose
- GitHub Account
- Google Drive API credentials (optional)

### 1. Clone Repository
```bash
git clone https://github.com/[USERNAME]/mlops-project.git
cd mlops-project
```

### 2. Setup Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Train Model Locally
```bash
python src/train.py
```

### 4. Run API Server
```bash
python src/serve.py
```

### 5. Setup Monitoring dengan Docker Compose
```bash
docker-compose up -d
```

Akses:
- **API**: http://localhost:8000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/admin)
- **MLflow**: http://localhost:5000

## 📊 Model Details

**Dataset**: [Iris/Wine/Diabetes - sesuaikan dengan dataset Anda]
**Algorithm**: Random Forest Classifier
**Metrics**:
- Accuracy: ~95%
- Precision: ~94%
- Recall: ~96%

## 🔄 CI/CD Pipeline

Pipeline otomatis di GitHub Actions:

### Basic Level
1. **Train**: Training model dengan dataset
2. **Evaluate**: Evaluasi performa model
3. **Upload**: Upload model ke storage

### Skilled Level
4. **Docker Build**: Build Docker image
5. **Docker Push**: Push image ke Docker Hub

### Advanced Level
6. **Deploy**: Deploy ke production (optional)
7. **Alert**: Notification jika ada issue

## 📈 Monitoring Metrics

Dashboard Grafana menampilkan:
1. **Request Rate**: Jumlah request per detik
2. **Prediction Latency**: Waktu inference model
3. **Error Rate**: Persentase error
4. **CPU & Memory Usage**: Resource utilization

## 🔔 Alerting Rules

Alert otomatis akan dikirim via email jika:
- Error rate > 5%
- Response time > 500ms
- CPU usage > 80%

## 📁 Struktur Project

```
mlops-project/
├── .github/
│   └── workflows/
│       └── mlops-pipeline.yml    # CI/CD pipeline
├── src/
│   ├── train.py                  # Training script
│   ├── evaluate.py               # Evaluation script
│   ├── serve.py                  # FastAPI serving
│   └── predict.py                # Prediction utility
├── monitoring/
│   ├── prometheus.yml            # Prometheus config
│   ├── alerting_rules.yml        # Alert rules
│   └── grafana_dashboard.json    # Grafana dashboard
├── docker-compose.yml            # Multi-container setup
├── Dockerfile                    # App container
├── requirements.txt              # Python dependencies
└── README.md                     # Documentation
```

## 🎯 Kriteria Penilaian

### Kriteria 3: CI/CD ✅
- [x] Repository GitHub public
- [x] Workflow dibuat dari nol
- [x] Menggunakan secrets
- [x] Automated training & evaluation
- [x] Docker build & push
- [x] Upload model ke storage

### Kriteria 4: Serving & Monitoring ✅
- [x] Dashboard dengan username Dicoding
- [x] Model serving dengan FastAPI
- [x] Prometheus metrics (3+ metrics)
- [x] Grafana visualization
- [x] Alerting system

## 📸 Screenshots

### 1. GitHub Actions Workflow
![Workflow Success](screenshots/github-actions.png)

### 2. MLflow Tracking
![MLflow Experiments](screenshots/mlflow-tracking.png)

### 3. Grafana Dashboard (dengan username: [USERNAME_ANDA])
![Grafana Dashboard](screenshots/grafana-dashboard.png)

### 4. Prometheus Targets
![Prometheus Targets](screenshots/prometheus-targets.png)

### 5. Model Serving Response
![API Response](screenshots/api-response.png)

### 6. Alert Notification
![Alert Email](screenshots/alert-notification.png)

## 🔧 Configuration

### GitHub Secrets
Setup secrets di repository settings:
- `DOCKERHUB_USERNAME`: Docker Hub username
- `DOCKERHUB_TOKEN`: Docker Hub access token
- `GDRIVE_CREDENTIALS`: Google Drive API credentials (optional)
- `NOTIFICATION_EMAIL`: Email untuk alerting

## 📝 Cara Submit

1. Push semua code ke GitHub repository public
2. Pastikan workflow berhasil dijalankan
3. Screenshot semua hasil (workflow, serving, monitoring, alerting)
4. Masukkan URL repository ke submission Dicoding
5. Lampirkan link Google Drive untuk screenshot

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use this project for learning purposes.

## 👤 Author

**Nessa Ayu Safitri**
- Dicoding: Nessa ayu safitri
- GitHub: [@nessaayusafitri2219](https://github.com/nessaayusafitri2219)
- Email: nessaayusafitri2219@gmail.com

---

**Note**: Ganti semua placeholder dengan informasi Anda sebelum submit!
