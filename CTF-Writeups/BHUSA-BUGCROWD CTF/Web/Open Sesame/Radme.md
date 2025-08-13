# 2. OpenSesame
## Challenge Description

You've discovered a new note-taking service. The developer claims it's secure because each user can only access their own notes. However, rumors suggest there's a special note that only admins can see, containing a secret flag. Can you find a way to access it?

### **Step 1 – Initial Exploration**

I registered a new user account and logged in. The service allowed me to:

- **Upload new notes**
- **View my own notes**

Everything seemed normal, but I suspected there might be a way to access **admin’s notes**.

### **Step 2 – Investigating Cookies**

While refreshing the page and inspecting the browser’s developer tools (`Application` tab in Chrome / `Storage` tab in Firefox), I noticed a cookie named:

### **Step 3 – Testing Insecure Direct Object Reference (IDOR)**

I modified the value of `user_id` to:

```
admin
```

<img width="1850" height="844" alt="image" src="https://github.com/user-attachments/assets/e7c2aed8-1966-452c-be82-615243524e26" />


### **Vulnerability Explanation**

This is a classic example of **Insecure Direct Object Reference (IDOR)**:

- The application uses user-controlled values (like `user_id` in a cookie) to determine which data to show.
- There is no proper **server-side authorization check** to confirm whether the logged-in user is allowed to access that object.

---

### **Key Takeaways**

- **Never trust client-side data** — cookies, local storage, form inputs can be tampered with.
- Always enforce **authorization** on the server side.
- IDOR vulnerabilities are common and can lead to major data breaches.
