import re
import json

class Normalizer:
    def __init__(self):
        pass

    def normalize_phone_data(self, raw_data):
        """
        Normalize raw phone data into the target schema.
        """
        normalized = {
            "id": self._generate_id(raw_data.get("brand"), raw_data.get("phone_name")),
            "brand": raw_data.get("brand"),
            "model_name": raw_data.get("phone_name"),
            "release_date": self._parse_date(raw_data.get("release_date")),
            "specs": {
                "network": self._parse_network(raw_data.get("specifications", {}).get("Network", {})),
                "launch": self._parse_launch(raw_data.get("specifications", {}).get("Launch", {})),
                "body": self._parse_body(raw_data.get("specifications", {}).get("Body", {})),
                "display": self._parse_display(raw_data.get("specifications", {}).get("Display", {})),
                "platform": self._parse_platform(raw_data.get("specifications", {}).get("Platform", {})),
                "memory": self._parse_memory(raw_data.get("specifications", {}).get("Memory", {})),
                "main_camera": self._parse_camera(raw_data.get("specifications", {}).get("Main Camera", {})),
                "selfie_camera": self._parse_camera(raw_data.get("specifications", {}).get("Selfie camera", {})),
                "sound": self._parse_sound(raw_data.get("specifications", {}).get("Sound", {})),
                "comms": self._parse_comms(raw_data.get("specifications", {}).get("Comms", {})),
                "features": self._parse_features(raw_data.get("specifications", {}).get("Features", {})),
                "battery": self._parse_battery(raw_data.get("specifications", {}).get("Battery", {})),
                "misc": self._parse_misc(raw_data.get("specifications", {}).get("Misc", {}))
            },
            "price_approx_usd": self._parse_price(raw_data.get("specifications", {}).get("Misc", {}).get("Price"))
        }
        return normalized

    def _generate_id(self, brand, model):
        if not brand or not model:
            return "unknown_id"
        # Simple slugification
        s = f"{brand}_{model}".lower()
        s = re.sub(r'[^a-z0-9]+', '_', s)
        return s.strip('_')

    def _parse_date(self, date_str):
        # Placeholder for date parsing logic
        # Should handle "Released 2024, January 24" etc.
        return date_str

    def _parse_network(self, data):
        return {
            "technology": data.get("Technology"),
            "bands_2g": data.get("2G bands"),
            "bands_3g": data.get("3G bands"),
            "bands_4g": data.get("4G bands"),
            "bands_5g": data.get("5G bands"),
            "speed": data.get("Speed")
        }

    def _parse_launch(self, data):
        return {
            "announced": data.get("Announced"),
            "status": data.get("Status")
        }

    def _parse_body(self, data):
        return {
            "dimensions": data.get("Dimensions"),
            "weight": data.get("Weight"),
            "build": data.get("Build"),
            "sim": data.get("SIM")
        }

    def _parse_display(self, data):
        # Extract size in inches, resolution, etc.
        return {
            "type": data.get("Type"),
            "size_inches": self._extract_inches(data.get("Size")),
            "resolution_pixels": data.get("Resolution"),
            "protection": data.get("Protection"),
            "refresh_rate_hz": self._extract_refresh_rate(data.get("Type")) # Often in Type
        }

    def _parse_platform(self, data):
        return {
            "os": data.get("OS"),
            "chipset": data.get("Chipset"),
            "cpu": data.get("CPU"),
            "gpu": data.get("GPU")
        }

    def _parse_memory(self, data):
        return {
            "card_slot": data.get("Card slot"),
            "internal_storage": data.get("Internal"), # Needs parsing for structured data
            "ram": self._extract_ram(data.get("Internal")) # Often combined
        }

    def _parse_camera(self, data):
        # This is complex as it can be Single, Dual, Triple, Quad etc.
        # For now, just dumping the raw values or simple extraction
        return {
            "modules": data.get("Modules", []), # Placeholder
            "features": data.get("Features"),
            "video": data.get("Video")
        }

    def _parse_sound(self, data):
        return {
            "loudspeaker": data.get("Loudspeaker"),
            "jack_3_5mm": data.get("3.5mm jack")
        }

    def _parse_comms(self, data):
        return {
            "wlan": data.get("WLAN"),
            "bluetooth": data.get("Bluetooth"),
            "positioning": data.get("Positioning"),
            "nfc": data.get("NFC"),
            "radio": data.get("Radio"),
            "usb": data.get("USB")
        }

    def _parse_features(self, data):
        return {
            "sensors": data.get("Sensors")
        }

    def _parse_battery(self, data):
        return {
            "type": data.get("Type"),
            "charging": data.get("Charging")
        }

    def _parse_misc(self, data):
        return {
            "colors": data.get("Colors"),
            "models": data.get("Models"),
            "sar": data.get("SAR")
        }

    def _parse_price(self, price_str):
        # Extract numeric value from string like "$ 1,299.00 / € 1,449.00"
        if not price_str:
            return None
        # Simple regex to find first dollar amount
        match = re.search(r'\$\s?([\d,]+)', price_str)
        if match:
            return float(match.group(1).replace(',', ''))
        return None

    def _extract_inches(self, size_str):
        if not size_str:
            return None
        match = re.search(r'([\d\.]+)\s*inches', size_str)
        if match:
            return float(match.group(1))
        return None

    def _extract_refresh_rate(self, type_str):
        if not type_str:
            return None
        match = re.search(r'(\d+)Hz', type_str)
        if match:
            return int(match.group(1))
        return None

    def _extract_ram(self, internal_str):
        # Very basic extraction, real world data is messy "256GB 12GB RAM, 512GB 12GB RAM"
        if not internal_str:
            return None
        # Just return the string for now or try to find max RAM
        return internal_str 
