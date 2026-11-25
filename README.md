# SmartPlantCare

Sistem monitoring dan penyiraman tanaman otomatis berbasis konteks (ESP32, MQTT, Telegram).

## Struktur

- `firmware/`  kode ESP32 (PlatformIO)
- `backend/`   MQTT subscriber, validasi, aturan, database, bot Telegram
- `dashboard/` tampilan web
- `scripts/`   simulasi data tanpa hardware
- `docs/`      proposal, skema rangkaian, hasil uji, screenshot
- `poster/`    poster A1/A2

## Setup

    cp firmware/include/config.example.h firmware/include/config.h
    cp backend/.env.example backend/.env
    cd backend && python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
