ffuf -u http://$1 -ic -c -w /usr/share/wordlists/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt -H "HOST: FUZZ.$1" -fs $2 $3 $4 $5 $6 $7
