import subprocess
proc = subprocess.Popen('ls', stdout=subprocess.PIPE)
tmp = proc.stdout.read()
print(tmp)
