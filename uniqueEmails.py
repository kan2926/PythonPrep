def numUniqueEmails(numUniqueEmails) -> int:
    res = set()
    for email in emails:
        emailL, emailR = email.split('@')        
        emailL = emailL.replace('.','')
        emailL = emailL.split('+')[0]
        res.add(emailL+'@'+emailR)
    return len(res)


if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(numUniqueEmails(emails))