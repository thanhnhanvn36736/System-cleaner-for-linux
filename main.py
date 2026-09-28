import subprocess
subprocess.run("df -h /", shell=True)
print("Do you want to clean your system (y/n)")
answer=input()
if answer == "y":
	subprocess.run("rm -rf ~/.cache/*", shell=True)
	subprocess.run("sudo apt clean", shell=True)
	subprocess.run("sudo apt autoremove", shell=True)
	subprocess.run("rm -rf ~/.local/share/Trash/files/*", shell=True)
	subprocess.run("rm -rf ~/.local/share/Trash/info/*", shell=True)
	print("Done! This is result:")
	subprocess.run("df -h /", shell=True)

print("Do you want to update system (y/n)")
update_answer = input()
if update_answer == "y":
    subprocess.run("sudo apt update && sudo apt upgrade -y", shell=True)
    print("System update completed!")
    # Kiểm tra lại dung lượng ổ cứng
    subprocess.run("df -h /", shell=True)
    print("Press enter to close")
    input()
