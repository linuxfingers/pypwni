def get_emails(email_file):
    f = open(email_file, "r")
    lines = f.readlines()
    clean_emails = []
    for line in lines:
        clean_emails.append(line.strip())
    f.close()
    return clean_emails
