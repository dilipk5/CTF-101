# 3. Over Bank

## Challenge Description

Welcome to the Over Bank Secure Bank Deposit System! Our cutting-edge financial platform implements robust security measures that our engineering team guarantees will prevent any balance manipulation:

**Positive-only deposits** with strict validation preventing any withdrawal attempts

**Real-time balance tracking** with comprehensive overflow protection

**Advanced arithmetic safeguards** using industry-standard integer handling

Our security team has extensively tested the system and believes it's mathematically impossible to achieve a negative balance through deposits alone. The system only allows positive money additions and validates all arithmetic operations.

The goal: **View the flag, which only appears if your balance is negative.**

### **Step 1 – Understanding the Functionality**

The application had a simple interface:

- You can **add money** to your account.
- Withdrawals were blocked.
- The flag is shown only if the account balance is **less than 0**.

At first glance, this seemed impossible because we could only add positive amounts.

### **Step 2 – Thinking About Integer Overflow**

Even though the system “validates” positive-only deposits, it might be using a fixed-size integer to store balances.

If we deposit a **very large number**, it could exceed the maximum integer value, causing an **integer overflow** and wrapping the balance into the negative range.

### **Step 3 – Exploit**

I entered a very large deposit amount, for example:

```
999999999999999999
```

After submission, my balance wrapped around into a **negative value** due to overflow.

<img width="762" height="624" alt="image" src="https://github.com/user-attachments/assets/4f9bb6d6-bbef-4605-9c04-bbeeabfea5f3" />


### **Vulnerability Explanation**

- The application only validated that deposits were positive — but did not account for **overflow limits** of the integer type storing the balance.
- On exceeding the maximum storable value (e.g., 32-bit or 64-bit signed integer), the balance wrapped around into negative territory.
- This is a **logic flaw** and an **integer overflow vulnerability**.

---

### **Key Takeaways**

- Always validate **input ranges**, not just sign (positive/negative).
- Use **arbitrary-precision arithmetic** for financial calculations (e.g., BigInt in JS, GMP in PHP).
- Never assume “mathematically impossible” in programming — computers don’t do infinite math.
