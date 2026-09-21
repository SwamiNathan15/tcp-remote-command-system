import subprocess

result = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True
)

print(result.stdout)