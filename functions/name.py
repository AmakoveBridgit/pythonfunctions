print("Bree is tall")
#

# adding multiple numbers
def add_items(*nums):
    sum=0
    for num in nums:
        sum+=num

        print(sum)

add_items(10,12,30,12)       