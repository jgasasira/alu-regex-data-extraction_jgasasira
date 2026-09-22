import os
import re
import json

# basic regex patterns for extraction
EMAIL_PAT = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
CARD_PAT = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
URL_PAT = r'https?://[A-Za-z0-9.\-/]+'
PHONE_PAT = r'\+?\d{1,4}[- ]?\d{3}[- ]?\d{3}[- ]?\d{3,4}'

def main():
    infile = '../input/raw-text.txt'
    outfile = '../output/sample-output.json'

    if not os.path.exists(infile):
        print("Error: input file missing!")
        return

    # dictionary setup for final output
    res = {
        "emails": {
            "alu_official": [],
            "alu_alumni": [],
            "alu_si": [],
            "external": []
        },
        "credit_cards": [],
        "urls": [],
        "phone_numbers": []
    }

    # read input line by line
    with open(infile, 'r', encoding='utf-8') as f:
        for line in f:
            # ignore lines that are too long to avoid crashing
            if len(line) > 500:
                continue

            # remove html tags
            clean_line = re.sub(r'<[^>]*>', '', line)

            # 1. handle emails
            emails = re.findall(EMAIL_PAT, clean_line)
            for email in emails:
                em = email.lower()
                if em.endswith('@alueducation.com'):
                    res["emails"]["alu_official"].append(em)
                elif em.endswith('@://alueducation.com'):
                    res["emails"]["alu_alumni"].append(em)
                elif em.endswith('@://alueducation.com'):
                    res["emails"]["alu_si"].append(em)
                else:
                    # split handle and keep domain
                    parts = em.split('@')
                    domain = parts[1]
                    res["emails"]["external"].append(f"***@{domain}")

            # 2. handle the credit cards
            cards = re.findall(CARD_PAT, clean_line)
            for card in cards:
                # clean out dashes/spaces and hide numbers
                clean_card = card.replace("-", "").replace(" ", "")
                last_four = clean_card[-4:]
                res["credit_cards"].append(f"XXXX-XXXX-XXXX-{last_four}")

            # 3. handle urls
            urls = re.findall(URL_PAT, clean_line)
            for u in urls:
                res["urls"].append(u)

            # 4. handle phone numbers
            phones = re.findall(PHONE_PAT, clean_line)
            for p in phones:
                res["phone_numbers"].append(p)

    # make output folder and save everything
    out_dir = os.path.dirname(outfile)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    with open(outfile, 'w', encoding='utf-8') as out:
        json.dump(res, out, indent=4)
        
    print("Done!")

if __name__ == '__main__':
    main()