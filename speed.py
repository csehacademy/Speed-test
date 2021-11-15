import speedtest

s = speedtest.Speedtest()

print("Test Basladi")

indirmehizi = s.download() / 1048576
yuklemehizi = s.upload() / 1048576
ping = round(s.results.ping)

print(f"indirme hizi = {indirmehizi:.2f} Mbps  ")
print(f"yukleme hizi = {yuklemehizi:.2f} Mbps  ")
print(f"Ping = {ping:.2f} ms  ")