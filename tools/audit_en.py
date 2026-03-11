import json, re

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

# 1. Find any remaining "dont", "cant", "wont" etc without apostrophes
# Use word boundary matching to be precise
print("=== REMAINING MISSING APOSTROPHES ===")
apostrophe_fixes = [
    (r'\bdont\b', "don't"), (r'\bcant\b', "can't"), (r'\bwont\b', "won't"),
    (r'\bisnt\b', "isn't"), (r'\barent\b', "aren't"), (r'\bwasnt\b', "wasn't"),
    (r'\bwerent\b', "weren't"), (r'\bhavent\b', "haven't"), (r'\bhasnt\b', "hasn't"),
    (r'\bdidnt\b', "didn't"), (r'\bcouldnt\b', "couldn't"), (r'\bshouldnt\b', "shouldn't"),
    (r'\bwouldnt\b', "wouldn't"), (r'\bIm\b', "I'm"), (r'\bIve\b', "I've"),
    (r'\bIll\b', "I'll"), (r'\bId\b(?! [A-Z])', "I'd"),
    (r'\bYoure\b', "You're"), (r'\bYouve\b', "You've"),
    (r'\bYoull\b', "You'll"), (r'\bYoud\b', "You'd"),
    (r'\bThats\b', "That's"), (r'\bTheres\b', "There's"),
    (r'\bTheyre\b', "They're"), (r'\bTheyve\b', "They've"),
    (r'\bTheyll\b', "They'll"), (r'\bTheyd\b', "They'd"),
    (r'\bHes\b', "He's"), (r'\bShes\b', "She's"),
    (r'\bIts\b(?!\s+[a-z])', "It's"),  # "Its" not followed by lowercase (possessive)
    (r'\bWhos\b', "Who's"), (r'\bWhats\b', "What's"),
    (r'\bLets\b(?!\s+[a-z])', "Let's"),
    (r'\bWeve\b', "We've"), (r'\bWere\b(?!wolves|\s+\w+ing)', "We're"),
]
found_keys = {}
for key in sorted(en):
    val = en[key]
    for pattern, fix in apostrophe_fixes:
        for m in re.finditer(pattern, val):
            if key not in found_keys:
                found_keys[key] = []
            found_keys[key].append((m.group(), fix, m.start()))

for key, issues in sorted(found_keys.items()):
    for word, fix, pos in issues:
        context = en[key][max(0,pos-10):pos+len(word)+10]
        print(f"  {key}: '{word}'->'{fix}' in ...{context}...")

# 2. Common misspellings
print("\n=== COMMON MISSPELLINGS ===")
misspellings = [
    (r'\brecieve\b', 'receive'), (r'\boccured\b', 'occurred'),
    (r'\bwierd\b', 'weird'), (r'\bseige\b', 'siege'),
    (r'\bthreshhold\b', 'threshold'), (r'\buntill\b', 'until'),
    (r'\bdefinate\b', 'definite'), (r'\bdefinately\b', 'definitely'),
    (r'\bseperate\b', 'separate'), (r'\bneccessary\b', 'necessary'),
    (r'\bexistance\b', 'existence'), (r'\boccurence\b', 'occurrence'),
    (r'\bindependant\b', 'independent'), (r'\bperseverence\b', 'perseverance'),
    (r'\brediculous\b', 'ridiculous'), (r'\bsuprise\b', 'surprise'),
    (r'\bteh\b', 'the'), (r'\badn\b', 'and'),
    (r'\bhte\b', 'the'), (r'\byuo\b', 'you'),
    (r'\btaht\b', 'that'), (r'\bwich\b', 'which'),
    (r'\bbeleive\b', 'believe'), (r'\bjudgement\b', 'judgment'),
    (r'\bacomplish\b', 'accomplish'), (r'\bagressive\b', 'aggressive'),
    (r'\bcommited\b', 'committed'),
    (r'\binnocense\b', 'innocence'), (r'\bknowledgable\b', 'knowledgeable'),
    (r'\bmischevious\b', 'mischievous'), (r'\bnoticable\b', 'noticeable'),
    (r'\bprivelege\b', 'privilege'),
    (r'\breferance\b', 'reference'), (r'\bsacrilige\b', 'sacrilege'),
    (r'\bsoveriegn\b', 'sovereign'), (r'\bvengance\b', 'vengeance'),
    (r'\bwarior\b', 'warrior'), (r'\bwarroir\b', 'warrior'),
    (r'\bassasin\b', 'assassin'), (r'\btheif\b', 'thief'),
    (r'\balchohol\b', 'alcohol'),
]
for pattern, fix in misspellings:
    if fix is None:
        continue
    for key in sorted(en):
        m = re.search(pattern, en[key], re.IGNORECASE)
        if m:
            print(f"  {key}: '{m.group()}'->'{fix}' -- {en[key][:80]}")

# 3. Double periods or other punctuation errors
print("\n=== PUNCTUATION ERRORS ===")
for key in sorted(en):
    val = en[key]
    if '..' in val and '...' not in val and '....' not in val:
        print(f"  {key} (double period): {val[:80]}")
    if ',,' in val:
        print(f"  {key} (double comma): {val[:80]}")
    if '!!' in val and '!!!' not in val:
        print(f"  {key} (double excl): {val[:80]}")
    if '??' in val:
        print(f"  {key} (double question): {val[:80]}")
    if '  .' in val or '  ,' in val or '  !' in val or '  ?' in val:
        stripped = val.lstrip()
        if '  .' in stripped or '  ,' in stripped:
            print(f"  {key} (space before punct): {val[:80]}")

print("\nDone.")
