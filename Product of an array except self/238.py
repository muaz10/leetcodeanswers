from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    left_products = []
    right_products = []
    
    left_prod = 1
    for num in nums:
        left_products.append(left_prod)
        left_prod *= num
    
    right_prod = 1
    for num in nums[::-1]:
        right_products.append(right_prod)
        right_prod *= num
        
    right_products = right_products[::-1]
    
    return [left * right for left, right in zip(left_products, right_products)]

nums = [1,2,3,4]
print(productExceptSelf(nums))
