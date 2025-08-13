# Dependency Dilemma

## Challenge Description

We've gained access to the logs of a hastily deployed web application. It's failing to start, throwing errors about a missing external component.

However, knowing the maintainer's sometimes chaotic development practices, we suspect something might have been left behind in the component's history. Maybe an old debug message? Or perhaps something more... interesting?

Your mission is to trace the source of the error and dive into the history of the problematic dependency to see what secrets it holds.

### **Step 1 – Investigating the Error**

When visiting the homepage, the application failed to load. Checking the browser console and server logs revealed that the error was related to a missing Node.js dependency:

```jsx
Cannot find module '@tobiasredfield/simple-web-app-package'
```

<img width="897" height="559" alt="image" src="https://github.com/user-attachments/assets/21cf990d-0c77-477a-b23c-93f082db1e58" />



### **Step 2 – Identifying the Dependency**

Looking at the HTML source code, I found a reference to:

```
@tobiasredfield/simple-web-app-package
```

This indicated it was an npm package.

<img width="1620" height="526" alt="image" src="https://github.com/user-attachments/assets/2a39c203-32f8-4ac7-8fa7-ca57938bcefb" />

### **Step 3 – OSINT on the Package**

I searched for the package on **npmjs.com** and confirmed it existed. The npm page linked to the **GitHub repository** of the package, maintained by the same username (`tobiasredfield`).

### **Step 4 – Diving into Git History**

Once on GitHub, I opened the repository and explored the commit history.

In one of the older commits, I found **a debug message left in the code** that contained the **flag**.

It was likely forgotten during development and later removed — but Git preserves history.

<img width="1618" height="593" alt="image" src="https://github.com/user-attachments/assets/985ef94d-76d0-4de5-9b4e-784ec45a1650" />

### **Step 5 – Flag Retrieved**

From that commit diff, I extracted the flag.

---

<img width="784" height="587" alt="image" src="https://github.com/user-attachments/assets/4300c732-46d3-40d3-a8db-2ba14e6a418b" />

### **Vulnerability Explanation**

- The developer mistakenly committed sensitive information to a public repository.
- Even if it’s later removed, **Git history preserves old commits** unless explicitly purged.
- Attackers can retrieve secrets, API keys, or flags by reviewing the commit history.

---

### **Key Takeaways**

- Never commit secrets (flags, API keys, passwords) to public repos.
- Use tools like `git filter-repo` or GitHub’s BFG Repo-Cleaner to permanently remove sensitive data from history.
- Perform code reviews before pushing changes to public repositories.
