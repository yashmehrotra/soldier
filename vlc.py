import soldier
import time
a = soldier.run('vlc', background=True)

for i in range(5):
    time.sleep(2)
    print i

a.kill()

print 'VLC Killed'
