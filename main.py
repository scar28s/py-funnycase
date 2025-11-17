import subprocess

inp_string = input("type a string u make u funny: \n").lower()

# done_str = inp_string[1::2].lower() + inp_string[::2].upper()
# done_str = done_str + done_str[::2].upper()
# indx = 0
finished_str = []
for i, letter in enumerate(inp_string):
    if i % 2 == 1:
        print(letter.upper(), end="")
        finished_str.append(letter.upper())
    elif i % 2 == 0:
        print(letter.lower(), end="")
        finished_str.append(letter.lower())
    else:
        print("Safepoint")

finished_str = ''.join(finished_str)

# print(f"\n{finished_str}")

process = subprocess.run(['xclip', '-selection', 'clipboard'], input=finished_str.encode("utf-8"), check=True)
print("\nCopied")
