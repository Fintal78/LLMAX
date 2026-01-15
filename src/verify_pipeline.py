import json
from normalizer import Normalizer
from database_manager import DatabaseManager

# Mock data simulating a response from the scraper
mock_samsung_data = {
    "brand": "Samsung",
    "phone_name": "Galaxy S24 Ultra",
    "release_date": "Released 2024, January 24",
    "specifications": {
        "Network": {
            "Technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
            "2G bands": "GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (Dual SIM model only)",
            "5G bands": "1, 2, 3, 5, 7, 8, 12, 20, 25, 26, 28, 38, 40, 41, 66, 75, 77, 78 SA/NSA/Sub6 - International",
            "Speed": "HSPA, LTE-A (up to 7CA), 5G"
        },
        "Launch": {
            "Announced": "2024, January 17",
            "Status": "Available. Released 2024, January 24"
        },
        "Body": {
            "Dimensions": "162.3 x 79 x 8.6 mm (6.39 x 3.11 x 0.34 in)",
            "Weight": "232 g or 233 g (8.18 oz)",
            "Build": "Glass front (Corning Gorilla Armor), glass back (Corning Gorilla Armor), titanium frame",
            "SIM": "Nano-SIM and eSIM or Dual SIM (2 Nano-SIMs and eSIM, dual stand-by)"
        },
        "Display": {
            "Type": "Dynamic LTPO AMOLED 2X, 120Hz, HDR10+, 2600 nits (peak)",
            "Size": "6.8 inches, 113.5 cm2 (~88.5% screen-to-body ratio)",
            "Resolution": "1440 x 3120 pixels, 19.5:9 ratio (~505 ppi density)",
            "Protection": "Corning Gorilla Armor"
        },
        "Platform": {
            "OS": "Android 14, One UI 6.1",
            "Chipset": "Qualcomm SM8650-AC Snapdragon 8 Gen 3 (4 nm)",
            "CPU": "Octa-core (1x3.39GHz Cortex-X4 & 3x3.1GHz Cortex-A720 & 2x2.9GHz Cortex-A720 & 2x2.2GHz Cortex-A520)",
            "GPU": "Adreno 750 (1 GHz)"
        },
        "Memory": {
            "Card slot": "No",
            "Internal": "256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM"
        },
        "Main Camera": {
            "Modules": ["200 MP, f/1.7, 24mm (wide)", "50 MP, f/3.4, 111mm (periscope telephoto)", "10 MP, f/2.4, 67mm (telephoto)", "12 MP, f/2.2, 13mm, 120˚ (ultrawide)"],
            "Features": "LED flash, auto-HDR, panorama",
            "Video": "8K@24/30fps, 4K@30/60/120fps, 1080p@30/60/240fps, 1080p@960fps, HDR10+, stereo sound rec., gyro-EIS"
        },
        "Selfie camera": {
            "Modules": ["12 MP, f/2.2, 26mm (wide)"],
            "Features": "Dual video call, Auto-HDR, HDR10+",
            "Video": "4K@30/60fps, 1080p@30fps"
        },
        "Sound": {
            "Loudspeaker": "Yes, with stereo speakers",
            "3.5mm jack": "No"
        },
        "Comms": {
            "WLAN": "Wi-Fi 802.11 a/b/g/n/ac/6e/7, tri-band, Wi-Fi Direct",
            "Bluetooth": "5.3, A2DP, LE",
            "Positioning": "GPS, GLONASS, BDS, GALILEO, QZSS",
            "NFC": "Yes",
            "Radio": "No",
            "USB": "USB Type-C 3.2, DisplayPort 1.2, OTG"
        },
        "Features": {
            "Sensors": "Fingerprint (under display, ultrasonic), accelerometer, gyro, proximity, compass, barometer"
        },
        "Battery": {
            "Type": "Li-Ion 5000 mAh, non-removable",
            "Charging": "45W wired, PD3.0, 65% in 30 min (advertised)"
        },
        "Misc": {
            "Colors": "Titanium Black, Titanium Gray, Titanium Violet, Titanium Yellow, Titanium Blue, Titanium Green, Titanium Orange",
            "Models": "SM-S928B, SM-S928B/DS, SM-S928U, SM-S928U1, SM-S928W, SM-S928N, SM-S9280, SM-S928E, SM-S928E/DS",
            "Price": "$ 1,299.99 / € 1,449.00 / £ 1,249.00 / ₹ 129,999"
        }
    }
}

def run_verification():
    print("Starting verification...")
    
    # 1. Test Normalizer
    normalizer = Normalizer()
    normalized_data = normalizer.normalize_phone_data(mock_samsung_data)
    
    print("\nNormalized Data Sample:")
    print(json.dumps(normalized_data, indent=2))
    
    # Check critical fields
    assert normalized_data['id'] == "samsung_galaxy_s24_ultra"
    assert normalized_data['brand'] == "Samsung"
    assert normalized_data['specs']['display']['size_inches'] == 6.8
    assert normalized_data['specs']['battery']['type'] == "Li-Ion 5000 mAh, non-removable"
    assert normalized_data['price_approx_usd'] is not None
    
    print("\nNormalizer verification passed!")

    # 2. Test Database Manager
    db_manager = DatabaseManager(db_path="test_data")
    db_manager.save_phone(normalized_data)
    
    loaded_data = db_manager.load_phone(normalized_data['id'])
    assert loaded_data == normalized_data
    print("\nDatabase save/load verification passed!")
    
    print("\nAll verification steps completed successfully.")

if __name__ == "__main__":
    run_verification()
