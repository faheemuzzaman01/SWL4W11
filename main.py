# def search_game():    
#     print("Hello Welcome to Guessing Game: ")
#     low = 1 # left
#     high = 100 # right    
#     count = 0 # mid     
#     while low <= high: #left <= right
#         guess = (low+high) //2        
#         count =+ 1
#         print(f"Guesses {count} Is this your Number: {guess}")

#         feedback = int(input("Enter the feedback('1=>Too High','2=>Too Low','3=>Correct'):"))

#         if feedback == 3:
#             print("Value is correct")
#         elif feedback == 1:
#             high = guess - 1
#         elif feedback == 2:
#             low = guess + 1
#         else:
#             print("Invalid Selection between 1 to 100")

# search_game()


# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i-1
#         while j>=0 and arr[j]>key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr
# valueKey = [5, 2, 9, 1, 6]
# result = insertion_sort(valueKey)
# print(result)


def insertion_sort(arr):
    i = 1    
    while i < len(arr):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        i += 1
    return arr
valueKey = [5, 2, 9, 1, 6]
result = insertion_sort(valueKey)
print(result)

