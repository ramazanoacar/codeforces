
x = list(input())
values = {
    ">" : "1000",
"<" : "1001",
"+" : "1010",
"-" : "1011",
"." : "1100",
"," : "1101",
"[" : "1110",
"]" : "1111"
}
string_x = ""
for i in x:
    string_x += values[i]
length = len(string_x)
two = 1
total = 0
for i in range(length-1, -1, -1):
    total += int(string_x[i]) * two
    two *= 2
print(total%1000003)
        

