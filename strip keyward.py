aa="              swaraj is small and good boy          "
print(aa)

# With The Help Of Strip Keyward We Can Remove Space Easily

print(aa.strip())


def remove_and_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
bb="      Me And My Friend Are Very Enjoy Sunday Trip     "
n=remove_and_split(bb,"My")
print(n)
