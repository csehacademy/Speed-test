import speedtest

s = speedtest.Speedtest()

print("Test Basladi")

indirmehizi = s.download()
yuklemehizi = s.upload()
ping = round(s.results.ping)

print(f"indirme hizi = {indirmehizi:.2f} Mbps  ")
print(f"yukleme hizi = {yuklemehizi:.2f} Mbps  ")
print(f"Ping = {ping:.2f} ms  ")
