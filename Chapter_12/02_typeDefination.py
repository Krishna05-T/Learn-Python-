
n2 : int = 5

n2.as_integer_ratio

#by this we can us the integer property without is we can also use 
# it is mainly use in fuction for the readability

def sum(a: int, b: int) -> int:
    return a+b

print(sum(3,3))


# for advance data


from typing import  List, Tuple, Dict,  Union 

number : List[int] = [1,2,3,4]

person : Tuple[str, int] = ("Alice", 23)

score : Dict[str, int] = {"Alice": 67, "Bob":78}

identifier : Union[int, str] = "12DS"
identifier = 12333 #also valid

