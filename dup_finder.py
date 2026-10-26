import hashlib, os, sys
from collections import defaultdict
def find_duplicates(root):
    by_hash = defaultdict(list)
    for r, _, files in os.walk(root):
        for fn in files:
            p = os.path.join(r, fn)
            h = hashlib.sha256(open(p, "rb").read()).hexdigest()
            by_hash[h].append(p)
    return {h: sorted(v) for h, v in by_hash.items() if len(v) > 1}
if __name__ == "__main__":
    dups = find_duplicates(sys.argv[1])
    print(f"{len(dups)} duplicate groups found.")
    for paths in dups.values(): print(" + ".join(paths))
