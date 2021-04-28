from past.builtins import raw_input


def remove(string, n):
      first = string[:n]
      last = string[n+1:]
      return first + last
string=raw_input("Enter sring:")
n=int(input("Enter the index of the character to remove:"))
print("Final string:")
print(remove(string, n))