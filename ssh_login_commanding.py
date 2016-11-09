import subprocess
proc=subprocess.Popen(["ssh","-t","shobhit@172.16.60.129","df -h ;","bash"],stdout=subprocess.PIPE)
while True:
    output=proc.stdout.readline()
    if output=='':
        break
    if output:
        print (output.strip())
