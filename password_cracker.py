import subprocess
import os

# Paths to wordlists and hash files
HASH_FILE = "hash.txt"  # Path to the hash file containing the password hash only (e.g., $y$j9T...)
WORDLIST = "/usr/share/wordlists/rockyou.txt"  # Path to rockyou.txt or another wordlist
HASHCAT_MODE = "9100"  # 9100 = yescrypt hash mode

# Function to run Hashcat
def run_hashcat():
    print("[*] Running Hashcat...")
    try:
        # Execute the Hashcat command
        hashcat_cmd = [
            "hashcat", "-m", HASHCAT_MODE, HASH_FILE, WORDLIST, "--force"
        ]
        # Run the command and capture the output
        subprocess.run(hashcat_cmd)
    except Exception as e:
        print(f"[!] Error running Hashcat: {e}")

# Function to run John the Ripper
def run_john():
    print("[*] Running John the Ripper...")
    try:
        # Execute the John the Ripper command
        john_cmd = ["john-jumbo/run/john", "--wordlist=" + WORDLIST, HASH_FILE]
        subprocess.run(john_cmd)
    except Exception as e:
        print(f"[!] Error running John the Ripper: {e}")

# Function to check the cracked passwords from John the Ripper
def check_john_results():
    print("[*] Checking John the Ripper results...")
    try:
        # Command to display cracked passwords
        subprocess.run(["john-jumbo/run/john", "--show", HASH_FILE])
    except Exception as e:
        print(f"[!] Error showing John the Ripper results: {e}")

# Main function to orchestrate the password cracking
if __name__ == "__main__":
    print("[*] Starting password cracking automation script.")
    
    # Check if hash.txt file exists
    if not os.path.exists(HASH_FILE):
        print(f"[!] Error: Hash file {HASH_FILE} not found.")
        exit(1)

    # Optionally run Hashcat first if needed
    # run_hashcat()

    # Run John the Ripper
    run_john()

    # Check John results to see if any passwords were cracked
    check_john_results()

    print("[*] Finished cracking process.")
