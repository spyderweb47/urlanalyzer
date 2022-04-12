#!/usr/bin/env python3

import sys
import os
import subprocess
from termcolor import colored

filename=sys.argv[1]

DNULL=open(os.devnull,"w+")

subprocess.call("mkdir url_extract",shell=True,stdout=DNULL,stderr=DNULL)
# print(colored("[+] url_extract directory Created Succesfulll","green"))
# #https://example.com/path/is/here?url=https://xyznajnfca.com?ijaof


#parameter extractor
subprocess.call('''cat '''+filename+''' | awk -F "?" '{$1=""; print $0}' | sort -u | tee url_extract/parameters.txt ''',shell=True,stdout=DNULL,stderr=DNULL)
print(colored("[+] parameter.txt :: Parameters Extracted ","green"))


#only file path extractor without parameter
subprocess.call('''cat '''+filename+''' | awk -F "?" '{print $1}' | sort -u | tee url_extract/filepath.txt ''',shell=True,stdout=DNULL,stderr=DNULL)
print(colored("[+] filepath.txt :: File location Extracted","green"))


#domain name extractor
subprocess.call('''cat '''+filename+''' | awk -F "/" '{print $1"/"$2"/"$3}' | sort -u |tee url_extract/domain.txt ''',shell=True,stdout=DNULL,stderr=DNULL)
print(colored("[+] domain.txt :: Domain Names Extracted","green"))

#path extractor
subprocess.call('''cat '''+filename+''' | awk -F "/" 'OFS="/" {$1=$2=$3=""; print $0}' | sort -u |sed 's/\/\///g' | tee url_extract/path.txt ''',shell=True,stdout=DNULL,stderr=DNULL)
print(colored("[+] path.txt :: Path Extracted","green"))


#only file extractor
subprocess.call('''cat '''+filename+''' | awk -F "/" 'OFS="/" {$1=$2=$3=""; print $0}' |awk -F "?" '{print $1}' | sort -u |sed 's/\/\///g'|rev|cut -d "/" -f 1|rev|sort -u|tee url_extract/file.txt ''',shell=True,stdout=DNULL,stderr=DNULL)
print(colored("[+] file.txt ::Filenames Extracted","green"))


print(colored("\n[+] Output is Stored in url_extract folder","yellow"))
