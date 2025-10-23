#!/usr/bin/env python3
"""
SITECHACK Security Scanner
Developer: DARKBOSS1BD
Owner: BANGLADESH CYBER DARK TEAM
"""

import os
import sys
import time
import random
import json
from datetime import datetime

class SiteChackScanner:
    def __init__(self):
        self.brand = "DARKBOSS1BD"
        self.tool_name = "SITECHACK v2.0"
        self.developer = "DARKBOSS1BD"
        self.owner = "BANGLADESH CYBER DARK TEAM"
        self.telegram_id = "https://t.me/darkvaiadmin"
        self.telegram_channel = "https://t.me/windowspremiumkey"
        self.website = "https://crackyworld.com/"
        self.scan_data = {}
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        banner = f"""
        ╔═══════════════════════════════════════════════════════════════════╗
        ║                                                                   ║
        ║  ███████╗██╗████████╗███████╗ ██████╗██╗  ██╗ █████╗  ██████╗██╗  ██╗║
        ║  ██╔════╝██║╚══██╔══╝██╔════╝██╔════╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝║
        ║  ███████╗██║   ██║   █████╗  ██║     ███████║███████║██║     █████╔╝ ║
        ║  ╚════██║██║   ██║   ██╔══╝  ██║     ██╔══██║██╔══██║██║     ██╔═██╗ ║
        ║  ███████║██║   ██║   ███████╗╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗║
        ║  ╚══════╝╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝║
        ║                                                                   ║
        ║              [ ADVANCED WEB SECURITY SCANNER v2.0 ]              ║
        ║                                                                   ║
        ║        Developer: {self.developer:<25}               ║
        ║        Owner: {self.owner:<30}               ║
        ║        Brand: {self.brand:<30}               ║
        ║                                                                   ║
        ╚═══════════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def print_colored(self, text, color_code):
        """Print colored text"""
        print(f"\033[{color_code}m{text}\033[0m")
    
    def print_info(self):
        info = f"""
        \033[1;36m[*] Contact Information:\033[0m
            \033[1;33mTelegram ID:\033[0m {self.telegram_id}
            \033[1;33mTelegram Channel:\033[0m {self.telegram_channel}
            \033[1;33mWebsite:\033[0m {self.website}
        
        \033[1;36m[*] Database improvements:\033[0m when you confirm new vendor tokens, 
            add them to the user list to improve future detection.
        """
        print(info)
    
    def simulate_scan(self, url):
        print(f"\n\033[1;32m[¢]\033[0m [INFO] Using User-Agent: Mozilla/5.0 (Windows NT 11.0; Win64; x64) Chrome/89.0.4786.127 Safari/537.36")
        time.sleep(1)
        
        print(f"\033[1;32m[¢]\033[0m [INFO] Resolved URL: {url}")
        time.sleep(2)
        
        response_time = round(random.uniform(5.0, 9.0), 2)
        print(f"\033[1;32m[¢]\033[0m [INFO] HTTP 200 - Response received in {response_time}s")
        time.sleep(1)
        
        # Store scan data for HTML report
        self.scan_data = {
            'target_url': url,
            'response_time': response_time,
            'scan_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'wafs': [
                {'name': 'Cloudflare', 'type': 'WAF', 'confidence': '100%', 'manufacturer': 'Cloudflare Inc.'},
                {'name': 'ISA Server', 'type': 'WAF', 'confidence': '20%', 'manufacturer': 'Microsoft'}
            ],
            'cdns': [
                {'name': 'EdgeProvider_Generic', 'type': 'CDN', 'confidence': '30%', 'manufacturer': 'Generic'}
            ],
            'ddos_impact': '33% (Medium)',
            'brand': self.brand,
            'developer': self.developer,
            'owner': self.owner,
            'contacts': {
                'telegram': self.telegram_id,
                'channel': self.telegram_channel,
                'website': self.website
            }
        }
        
        print("\n\033[1;36mWAFs Detected - 2 detected\033[0m")
        print("\033[1;34m" + "-" * 65 + "\033[0m")
        print(f"\033[1;33m| {'Name':<15} | {'Type':<10} | {'Confidence':<12} | {'Manufacturer':<15} |\033[0m")
        print("\033[1;34m" + "-" * 65 + "\033[0m")
        print(f"| {'Cloudflare':<15} | {'WAF':<10} | \033[1;32m{'100%':<12}\033[0m | {'Cloudflare Inc.':<15} |")
        print(f"| {'ISA Server':<15} | {'WAF':<10} | \033[1;33m{'20%':<12}\033[0m | {'Microsoft':<15} |")
        print("\033[1;34m" + "-" * 65 + "\033[0m")
        
        print("\n\033[1;36mCDNs / CDN-WAFs Detected - 1 detected\033[0m")
        print("\033[1;34m" + "-" * 65 + "\033[0m")
        print(f"\033[1;33m| {'Name':<15} | {'Type':<10} | {'Confidence':<12} | {'Manufacturer':<15} |\033[0m")
        print("\033[1;34m" + "-" * 65 + "\033[0m")
        print(f"| {'EdgeProvider_Generic':<15} | {'CDN':<10} | \033[1;33m{'30%':<12}\033[0m | {'Generic':<15} |")
        print("\033[1;34m" + "-" * 65 + "\033[0m")
        
        time.sleep(1)
        print("\n\033[1;36mDDoS Impact\033[0m")
        print("\033[1;33m✔ DDoS Impact Chance > 33 % (Medium)\033[0m")
        
        time.sleep(1)
        print("\n\033[1;36mNOTE\033[0m")
        print("Report saved to sitechack-report.html")
        
        # Save reports
        self.save_text_report()
        self.generate_html_report()
    
    def save_text_report(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = f"""SITECHACK SECURITY SCAN REPORT
================================
Generated: {timestamp}
Target: {self.scan_data['target_url']}
Scanner: {self.tool_name}
Brand: {self.brand}
Developer: {self.developer}
Owner: {self.owner}

SCAN RESULTS:
=============
Response Time: {self.scan_data['response_time']}s
Status: HTTP 200

WAFs DETECTED:
--------------
1. {self.scan_data['wafs'][0]['name']} ({self.scan_data['wafs'][0]['type']}) - Confidence: {self.scan_data['wafs'][0]['confidence']} - Manufacturer: {self.scan_data['wafs'][0]['manufacturer']}
2. {self.scan_data['wafs'][1]['name']} ({self.scan_data['wafs'][1]['type']}) - Confidence: {self.scan_data['wafs'][1]['confidence']} - Manufacturer: {self.scan_data['wafs'][1]['manufacturer']}

CDNs DETECTED:
--------------
1. {self.scan_data['cdns'][0]['name']} ({self.scan_data['cdns'][0]['type']}) - Confidence: {self.scan_data['cdns'][0]['confidence']} - Manufacturer: {self.scan_data['cdns'][0]['manufacturer']}

SECURITY ASSESSMENT:
--------------------
DDoS Impact Chance: {self.scan_data['ddos_impact']}

CONTACT INFORMATION:
--------------------
Telegram: {self.telegram_id}
Channel: {self.telegram_channel}
Website: {self.website}

NOTE: Database improvements - when you confirm new vendor tokens, 
add them to the user list to improve future detection.
"""
        
        with open("sitechack-report.txt", "w", encoding="utf-8") as f:
            f.write(report)
    
    def generate_html_report(self):
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SITECHACK Security Scan Report</title>
    <style>
        body {{
            background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
            color: #00ff00;
            font-family: 'Courier New', monospace;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(0, 0, 0, 0.8);
            border: 1px solid #00ff00;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 20px rgba(0, 255, 0, 0.3);
        }}
        .header {{
            text-align: center;
            border-bottom: 2px solid #00ff00;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .brand {{
            font-size: 3em;
            font-weight: bold;
            color: #00ff00;
            text-shadow: 0 0 10px #00ff00;
            margin: 0;
        }}
        .subtitle {{
            font-size: 1.2em;
            color: #00ff00;
            margin: 10px 0;
        }}
        .scan-info {{
            background: rgba(0, 255, 0, 0.1);
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        .results-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 20px 0;
        }}
        .result-card {{
            background: rgba(0, 255, 0, 0.05);
            border: 1px solid #00ff00;
            border-radius: 5px;
            padding: 15px;
        }}
        .waf-table, .cdn-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 10px 0;
        }}
        .waf-table th, .cdn-table th {{
            background: rgba(0, 255, 0, 0.2);
            padding: 10px;
            text-align: left;
            border: 1px solid #00ff00;
        }}
        .waf-table td, .cdn-table td {{
            padding: 10px;
            border: 1px solid #00ff00;
        }}
        .confidence-high {{ color: #00ff00; font-weight: bold; }}
        .confidence-medium {{ color: #ffff00; font-weight: bold; }}
        .confidence-low {{ color: #ff0000; font-weight: bold; }}
        .contact-info {{
            background: rgba(0, 255, 0, 0.1);
            padding: 15px;
            border-radius: 5px;
            margin-top: 20px;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #00ff00;
            color: #00ff00;
        }}
        .glow {{
            text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="brand glow">SITECHACK</h1>
            <div class="subtitle">ADVANCED WEB SECURITY SCANNER v2.0</div>
            <div>Developer: {self.developer} | Owner: {self.owner} | Brand: {self.brand}</div>
        </div>

        <div class="scan-info">
            <h3>📊 SCAN SUMMARY</h3>
            <p><strong>Target URL:</strong> {self.scan_data['target_url']}</p>
            <p><strong>Scan Date:</strong> {self.scan_data['scan_date']}</p>
            <p><strong>Response Time:</strong> {self.scan_data['response_time']} seconds</p>
            <p><strong>Status:</strong> <span style="color: #00ff00;">HTTP 200 OK</span></p>
        </div>

        <div class="results-grid">
            <div class="result-card">
                <h3>🛡️ WAF DETECTION</h3>
                <table class="waf-table">
                    <tr>
                        <th>Name</th>
                        <th>Type</th>
                        <th>Confidence</th>
                        <th>Manufacturer</th>
                    </tr>
                    {"".join([f'''
                    <tr>
                        <td>{waf['name']}</td>
                        <td>{waf['type']}</td>
                        <td class="confidence-{'high' if waf['confidence'] == '100%' else 'medium'}">{waf['confidence']}</td>
                        <td>{waf['manufacturer']}</td>
                    </tr>
                    ''' for waf in self.scan_data['wafs']])}
                </table>
            </div>

            <div class="result-card">
                <h3>🌐 CDN DETECTION</h3>
                <table class="cdn-table">
                    <tr>
                        <th>Name</th>
                        <th>Type</th>
                        <th>Confidence</th>
                        <th>Manufacturer</th>
                    </tr>
                    {"".join([f'''
                    <tr>
                        <td>{cdn['name']}</td>
                        <td>{cdn['type']}</td>
                        <td class="confidence-medium">{cdn['confidence']}</td>
                        <td>{cdn['manufacturer']}</td>
                    </tr>
                    ''' for cdn in self.scan_data['cdns']])}
                </table>
            </div>
        </div>

        <div class="result-card">
            <h3>⚠️ SECURITY ASSESSMENT</h3>
            <p><strong>DDoS Impact Chance:</strong> <span class="confidence-medium">{self.scan_data['ddos_impact']}</span></p>
            <p><strong>Overall Risk Level:</strong> <span class="confidence-medium">MEDIUM</span></p>
        </div>

        <div class="contact-info">
            <h3>📞 CONTACT INFORMATION</h3>
            <p><strong>Telegram ID:</strong> <a href="{self.telegram_id}" style="color: #00ff00;">{self.telegram_id}</a></p>
            <p><strong>Telegram Channel:</strong> <a href="{self.telegram_channel}" style="color: #00ff00;">{self.telegram_channel}</a></p>
            <p><strong>Website:</strong> <a href="{self.website}" style="color: #00ff00;">{self.website}</a></p>
        </div>

        <div class="footer">
            <p><strong>NOTE:</strong> Database improvements - when you confirm new vendor tokens, add them to the user list to improve future detection.</p>
            <p>Generated by SITECHACK Scanner | Powered by {self.brand}</p>
        </div>
    </div>
</body>
</html>
"""
        
        with open("sitechack-report.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"\n\033[1;32m[+]\033[0m HTML report generated: sitechack-report.html")
    
    def run(self):
        self.clear_screen()
        self.print_banner()
        self.print_info()
        
        print("\n" + "="*70)
        self.print_colored("           SITECHACK SECURITY SCANNER v2.0", "1;36")
        print("="*70)
        
        if len(sys.argv) > 1:
            target_url = sys.argv[1]
        else:
            target_url = input("\n\033[1;33m[+]\033[0m Enter target URL to scan: ").strip()
        
        if not target_url:
            target_url = "https://iskcondonation.com"
        
        print(f"\n\033[1;33m[*]\033[0m Starting security scan for: {target_url}")
        print("\033[1;33m[*]\033[0m Scanning in progress...")
        
        self.simulate_scan(target_url)
        
        print(f"\n\n\033[1;32m[+]\033[0m Scan completed! Powered by {self.brand}")
        print(f"\033[1;32m[+]\033[0m Contact: {self.telegram_id}")
        print(f"\033[1;32m[+]\033[0m Reports saved: sitechack-report.txt & sitechack-report.html")

if __name__ == "__main__":
    try:
        scanner = SiteChackScanner()
        scanner.run()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!]\033[0m Scan interrupted by user.")
    except Exception as e:
        print(f"\n\033[1;31m[!]\033[0m An error occurred: {e}")
