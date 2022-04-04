import string
def save_lines(destpath,lines):
    with open(destpath, mode="w", encoding="utf-8") as fout:
        fout.writelines(lines)
def clean_punkts (srcpath, destpath):
    with open(srcpath, encoding="utf-8") as fin, open(destpath, mode="w", encoding="utf-8") as fout:
        for line in fin:  # for each line in incoming file
            for p in string.punctuation:
                line=line.replace(p,"")
            fout.write(line)  # write into outgoing file
fname="veidenbaums.txt"
with open(fname,encoding="utf-8") as f:
    lines = f.readlines()
    print(f"number of lines: {len(lines)}")
    filtered_lines=[l for l in lines if "***" not in l and l != '\n']
    print(filtered_lines)
save_lines("veid_poems.txt",filtered_lines)
clean_punkts ("veid_poems.txt", "cleaned_text.txt")


