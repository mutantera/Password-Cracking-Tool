# **Password Cracking Automation Tool**

This is a Python tool designed to automate the process of cracking password hashes using **John the Ripper Jumbo** version. It can crack various hash types, such as **yescrypt**, **SHA512crypt**, and others, by leveraging the **rockyou.txt** or any other wordlist.

---

## **Project Structure**

- **`password_cracker.py`**: The Python script that automates password cracking.
- **`hash.txt`**: A file containing the hash(es) you want to crack.
- **`john-jumbo`**: The folder containing the **John the Ripper Jumbo** version executable.
- **`rockyou.txt`**: The wordlist (this must be placed in the correct directory).

---

## **How It Works**

The script automates the following tasks:
1. **Loads the Hash**: It reads a hash from the `hash.txt` file.
2. **Runs John the Ripper**: It runs **John the Ripper** from the `john-jumbo` directory to crack the password using a wordlist like `rockyou.txt`.
3. **Displays Cracked Passwords**: After cracking, it shows the cracked passwords.

---

## **Requirements**

- **Python 3.x**
- **John the Ripper Jumbo** version (included in the `john-jumbo` folder)
- **rockyou.txt** or another wordlist

---

## **Installation Steps**

1. **Clone the Repository**:
   First, clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd your-repository
   ```

3. **Ensure John the Ripper Jumbo is Ready**:
   The **`john-jumbo`** folder must contain the compiled John the Ripper executable. If it's not compiled, follow these steps to compile it manually:

   ```bash
   cd john-jumbo/src
   ./configure && make -s clean && make -sj4
   ```

   After compilation, John the Ripper will be ready to use.

4. **Prepare the `hash.txt` file**:
   - Place the password hash you want to crack inside `hash.txt`. Make sure it contains only the hash, nothing else.

5. **Ensure the Wordlist is in Place**:
   - The `rockyou.txt` wordlist must be present in the path `/usr/share/wordlists/rockyou.txt` or any other wordlist you prefer.

---

## **Running the Script**

1. **Add the Hash**:
   - Ensure your `hash.txt` contains the hash you want to crack.

2. **Run the Python Script**:
   Run the Python script by executing:
   ```bash
   python3 password_cracker.py
   ```

   The script will:
   - Load the hash from `hash.txt`.
   - Run **John the Ripper** from the **`john-jumbo`** directory.
   - Attempt to crack the hash using the **rockyou.txt** wordlist or another wordlist you specify.

3. **Check Cracked Passwords**:
   After the cracking process completes, the script will automatically display the cracked passwords. If needed, you can manually run the following command to check cracked passwords:

   ```bash
   ./john-jumbo/run/john --show hash.txt
   ```

---

### **How the Script Works**:
- It calls **John the Ripper** from the `john-jumbo` folder.
- It uses the `rockyou.txt` wordlist or another wordlist specified.
- It cracks the password hash in `hash.txt`.
- After cracking, it checks for cracked passwords using the `--show` option.

---

## **Additional Commands**

### To Check Cracked Passwords Manually:
If you want to manually check the cracked passwords after running the script, you can do so with:
```bash
./john-jumbo/run/john --show hash.txt
```

### To View the Status of Cracking:
If John the Ripper is still running and you want to check its progress, send the **SIGUSR1** signal:
```bash
ps aux | grep '[j]ohn'  # Find the process ID of John
kill -USR1 <process-id>
```

This will display the current status without stopping the cracking process.

---

## **Requirements**

- **Python 3.x**
- **John the Ripper Jumbo** (included in the `john-jumbo` folder)
- A wordlist, such as **rockyou.txt** (must be present in `/usr/share/wordlists/rockyou.txt`)

---

## **License**

This project is licensed under the MIT License.

---

## **Contributing**

Feel free to submit pull requests and raise issues to improve the tool or add additional features. Contributions are welcome!

---

## **Acknowledgments**

- **John the Ripper** for its password-cracking capabilities.
- The **rockyou.txt** wordlist for common passwords.
- Special thanks to the open-source community for tools that make penetration testing easier.

---

By following these steps, you will be able to automate the password-cracking process using **John the Ripper Jumbo** with the provided Python script.

Let me know if you need any more changes or additions!
