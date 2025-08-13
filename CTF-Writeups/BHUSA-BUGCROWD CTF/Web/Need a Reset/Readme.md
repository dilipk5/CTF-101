# 4. Need a Reset

## Challenge Description

Your goal is to gain access to the system administration area.

The application allows viewing employee details and logging into an admin panel. However, no admin credentials are provided.

### **Step 1 – Reconnaissance**

After browsing the site, I found:

- **Employee Listing Table** – showing information such as:
    - Name
    - Username
    - Office city
    - Year joined
- **Login Page** – requires username/password for access.
- **Forgot Password Page** – asks for the username to reset the password.

<img width="930" height="567" alt="image" src="https://github.com/user-attachments/assets/e1899292-93f3-4cc6-a6e0-d4a455a894d6" />


<img width="822" height="462" alt="image" src="https://github.com/user-attachments/assets/aac39899-683a-480b-bae7-3cab24f34529" />


### **Step 2 – Targeting the Admin Account**

From the employee list, I found the **admin username**:

<img width="922" height="351" alt="image" src="https://github.com/user-attachments/assets/30039526-4f01-45d8-a1a5-5ccd9e57a2ab" />


### **Step 3 – Security Questions**

The reset form asked 3 questions:

1. What city is your office located in?
2. What year did you join the company?
3. What was the name of your first pet?

Interestingly, **only 2 correct answers** were required to proceed.

### **Step 4 – Finding the Answers**

The employee table already gave me:

- **City** – directly listed in the "Office Location" column.
- **Year Joined** – directly listed in the "Joined" column.

The "First Pet" answer was unknown, but it wasn’t needed.

### **Step 5 – Exploit**

I filled:

<img width="890" height="445" alt="image" src="https://github.com/user-attachments/assets/5f78b361-e1d9-4ede-b187-8b9ccd23a429" />


### **Step 6 – Logging in as Admin**

After resetting the password, I logged in as `admin` and gained access to the admin panel, where the **flag** was displayed.

<img width="633" height="94" alt="image" src="https://github.com/user-attachments/assets/880fc5c2-c5a6-4aca-b523-6c97832d346e" />


### **Vulnerability Explanation**

This was a combination of:

- **Information Disclosure** – sensitive data (answers to security questions) was publicly visible in the employee list.
- **Weak Security Question Implementation** – only two answers were required, making it easier to bypass.

---

### **Key Takeaways**

- Never use easily guessable or publicly available information for password recovery.
- Avoid partial matching security question systems.
- Treat password reset as a high-security action — require email verification or multi-factor authentication.

---
