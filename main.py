import argparse, csv, requests, sys
import json
from time import sleep

# local modules
from menu import menu
from readline import get_emails
from style import bg,fg,style

url = "https://haveibeenpwned.com/api/v3/breachedaccount/"
full_breach = "?truncateResponse=false"
hibp_api_key = 'YOUR_KEY_HERE'
headers = {
    'user-agent':'pypwni',
    'hibp-api-key':str(hibp_api_key),
    'format': 'application/json',
    'timeout': '2.5',
}

response = requests.request("GET", url, headers=headers)

print("""\

╔══════════════════════════════════════════════════════╗
║                                                      ║
║   ██████╗ ██╗   ██╗██████╗ ██╗    ██╗███╗   ██╗██╗   ║
║   ██╔══██╗╚██╗ ██╔╝██╔══██╗██║    ██║████╗  ██║██║   ║
║   ██████╔╝ ╚████╔╝ ██████╔╝██║ █╗ ██║██╔██╗ ██║██║   ║
║   ██╔═══╝   ╚██╔╝  ██╔═══╝ ██║███╗██║██║╚██╗██║██║   ║
║   ██║        ██║   ██║     ╚███╔███╔╝██║ ╚████║██║   ║
║   ╚═╝        ╚═╝   ╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚═╝   ║
║                        v1.0                          ║
╚══════════════════════════════════════════════════════╝ 

Now checking the provided list of emails against the 'Have I Been Pwned?' database.
""") 

# 1. start program with filename
args_filename, output_file = menu()

# 2. read the emails from file
emails = get_emails(args_filename)

# 3. make API call for each email
results = []

for email in emails:
    base_URL = url + email + full_breach
    response = requests.request("GET", base_URL, headers=headers)
    print("Checking " + fg.blue + email + style.RESET + " for known breaches...")

    if response.status_code == 404:
        results.append("No breach.")
        #print("No breach found for " + fg.blue + email + ".")
    else:
        response_dict = response.json()
        results.append(response_dict)
        #print("Breach found for " + fg.blue + email + ".")
        #print(response_dict)
    sleep(7)

# 4. CSV setup
output = "sep=,\nEmail, Title, Domain, Date, Breach Type, Malware, Sensitive\n"

print("""\
=======================================
✭   🐎 Breached Account Results 🐎   ✭
========================================
""")

# 5. process results
for email in range(len(emails)):

    if results[email] == "No breach.":
        print(fg.green + "[ ♡ ] " + style.RESET + " No breach found for " + fg.blue + emails[email] + style.RESET)
    else:
        for breach in results[email]:
            title = "\"" + breach["Title"] + "\""
            domain = breach["Domain"]
            breach_date = breach["BreachDate"]
            data_classes = "|"
            breach_type = breach["DataClasses"]
            breach_type = data_classes.join(breach_type)
            malware = breach["IsMalware"]
            sensitive = breach["IsSensitive"]
            print(fg.red + "[ ⚠ ] " + style.RESET + " Breach " + fg.yellow + title + style.RESET + " found for " + fg.blue + emails[email] + style.RESET)
            breach_email = emails[email]
            row = breach_email + "," + title + "," + domain + "," + breach_date + "," + breach_type + "," + str(malware) + "," + str(sensitive) + "\n"
            output = output + row

with open(output_file, mode="wt") as f:
    f.write(output)
