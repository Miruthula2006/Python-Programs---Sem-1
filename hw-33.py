def student_details(name,age,s_depart):
    print(f"Student Name:{name}")
    print(f"Student age:{age}")
    print(f"Student department:{s_depart}")
student_details(name="miruthula",age=17,s_depart="CS with AI")


def food_items(food):
   print(f"Food Type: {food['food_type']}")
   print(f"Item Name: {food['item_name']}")
   print(f"Item Cost: {food['item_cost']}")
food={"food_type": "Ice cream","item_name": "Chocolate","item_cost":100}
food_items(food)
    
    
