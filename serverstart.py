
import subprocess

subprocess.run("sudo systemctl enable --now libvirtd && sudo virsh net-list -all", shell = False)

print("[*]working magic........")

input("Press any key to continue")
