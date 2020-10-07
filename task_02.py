s = int(input()) % (3600 * 24)

hh = s // 3600
mm = (s % 3600) // 60
ss = s % 60

print(f"{hh:02}:{mm:02}:{ss:02}")
