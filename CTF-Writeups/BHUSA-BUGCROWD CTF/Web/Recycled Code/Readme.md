# Recycled Code

## Challenge Description

We've set up a new secure login system using Time-based One-Time Passwords (TOTP) for our admin panel.

We've also got a test user account that might have some leftover debug features enabled.

Can you leverage this to get into the admin panel?

- **Credentials**:
    - Test User: `testuser` / `password123`
    - Admin User: `admin` / `supersecretadminpass`

**Access the challenge at:**

### **Step 1 – Understanding the Flow**

The login process had **two steps**:

1. **Username & Password** authentication.
2. **TOTP verification** — a 6-digit code generated based on time.

The key weakness: **all users were receiving the same OTP at the same time**, meaning the code for `testuser` would also work for `admin`.

### **Step 2 – Logging in as Test User**

I first logged in with:

```jsx
Username: testuser
Password: password123
```

After successful authentication, the site displayed the current **TOTP code** for this account.

### **Step 3 – Exploiting TOTP Reuse**

In a second browser tab:

1. I logged in as:

```
username: admin
password: supersecretadmin
```

1. When prompted for the OTP, I entered the **same code** shown for `testuser`.

Since the OTP was **not user-specific**, the system accepted it and logged me in as `admin`

<img width="1886" height="543" alt="image" src="https://github.com/user-attachments/assets/59f94798-6fa2-40fb-b105-1451c2191a7d" />

### **Vulnerability Explanation**

- Proper TOTP implementation requires **unique secrets per user**.
- In this system, all users shared the same TOTP seed, meaning one user could generate valid codes for any other account.
- This allowed **privilege escalation** from a low-privileged account (`testuser`) to the administrator account.

---

### **Key Takeaways**

- Always use a **per-user TOTP secret** stored securely in the database.
- Never share a single OTP seed across multiple accounts.
- Even in testing environments, avoid shortcuts that could become production vulnerabilities.
