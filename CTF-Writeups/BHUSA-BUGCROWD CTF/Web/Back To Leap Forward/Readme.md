# Setp Back To Leap Forward

## Challenge Description

You've discovered a simple document viewer application called "DocView" that allows users to access various public documents stored on the server. Can you find a way to access the hidden flag?

### **Step 1 – Exploring the Application**

The interface listed several public documents.

When clicking on a document, the URL looked like:

```jsx
/view?file=public_docs/note.txt
```

This indicated the application was likely reading files from the filesystem based on the `file` parameter.

### **Step 2 – Suspecting Path Traversal**

The challenge mentioned that files are stored in `public_docs/`, but the **flag** would be in a different, private directory.

I suspected a **path traversal** vulnerability where `../` could escape the `public_docs` folder.

<img width="747" height="174" alt="image" src="https://github.com/user-attachments/assets/0b920815-1b80-4d37-b82f-2a2ec39628a5" />

### **Step 3 – Attempting Directory Traversal**

I modified the URL to:

```
/view?file=../private_docs/flag.txt
```

The `../` moves up one directory, allowing access to `private_docs/`.

### **Step 4 – Success**

The server returned the contents of `flag.txt`, revealing the **flag**.

<img width="1196" height="146" alt="image" src="https://github.com/user-attachments/assets/fa596b64-0939-406c-b1fb-a2d0dc35a2b7" />

### **Vulnerability Explanation**

- The application directly used user input (`file` parameter) to read files from the server.
- Without sanitization or path validation, attackers could escape the intended directory and read arbitrary files.
- This is a **Directory Traversal / Local File Inclusion (LFI)** vulnerability.

---

### **Key Takeaways**

- Always validate and sanitize file paths before reading files from disk.
- Use **allowlists** of permitted files rather than directly trusting user input.
- Prevent `../` sequences in user-supplied paths by normalizing and validating paths server-side.
