# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

def fun(s):
    # return True if s is a valid email, else return False
    username = s.split("@")[0]
    domain = s.split("@")[-1]
    website = domain.split(".")[0]
    extension = domain.split(".")[-1]
    
    if "@" in s and "." in s and s.count("@") <=1 and s.count(".") <= 1:  
        if username.isalnum() or "_" in username or "-" in username:
            if website.isalnum():
                if extension.isalpha() and len(extension) <= 3:
                    return True
    else: return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
