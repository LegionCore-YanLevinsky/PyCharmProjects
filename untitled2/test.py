# int count = 0;
#             for (int i = 1, sum = 0; i <= repeats; i++, sum = 0)
#             {
#                 foreach (char n in i.ToString()) sum += int.Parse(n.ToString());
#                 if (i % sum == 0) count++;
#             }
#             return count;

count = 0

i = 1
while i <= 1000000:
    sum = 0
    for n in str(i):
        sum += int(n)
    if i % sum == 0:
        count += 1

    i += 1
print('-'*10)
print(count)
