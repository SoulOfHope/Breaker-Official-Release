import subprocess
result=subprocess.run(["python3","-m","pip","install","sly"])
print(result.stdout)
