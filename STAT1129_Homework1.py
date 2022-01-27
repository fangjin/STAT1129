#!/usr/bin/env python
# coding: utf-8

# In[121]:


nums = list(range(30, 61, 5))    # Generate a list of numbers from 30 to 60 with interval 5, using range
print (nums)

print (nums[::-1])               # Order your list in reversed order

nums.append(65)
print (nums[::-1])               # Insert 65 to the beginning of your new list


# In[122]:


nums = []                # Create an empty list.
for n in range (21):
    nums.append(n)       # Append integers 0-20 to the list
print (nums)

del nums[0]              # Delete item 0
print (nums)

print(len(nums))         # Return the length, maximal and minimal values of the newest list.
print(max(nums))
print(min(nums))

Sum = sum(nums)          # Sum up all items.
print(Sum)


# In[123]:


weatherList = {"sunny": "play", "rainy": "watch TV", "cloudy": "walk"}      # Create a weather dictionary
print(weatherList)


for weather in weatherList:                                                 # Using for loop, print out all the keys and values in the same line.
    print("When", weather, "let us", weatherList[weather])
    
weatherList["snowy"] = "ski"                                                # Then add a new pair (“snowy”, “ski”) to your dictionary.
print(weatherList)

