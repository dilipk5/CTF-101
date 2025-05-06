section .data
    msg: db 'Hello World!'

section .text
    global _start

_start:
    ; printing hello world
    mov rax,1
    mov rdi,1
    mov rsi,msg
    mov rdx,12
    syscall

    ;exiting the code
    mov rax,60
    mov rdi,1
    syscall
