from collections import Counter        

def subdomainVisits(cpdomains):
    counter = Counter()
    for cpdomain in cpdomains:
        count, *domains = cpdomain.replace(" ",".").split('.')        
        for i in range(len(domains)):
            counter[".".join(domains[i:])] += int(count)      
        
    return [" ".join((str(v), k)) for k, v in counter.items()]
    
    

if __name__ == '__main__':
    v = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(subdomainVisits(v))

    