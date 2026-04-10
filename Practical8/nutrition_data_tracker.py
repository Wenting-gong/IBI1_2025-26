class food_item:
    def __init__(self,name,calories,protein,carbohydrates,fat):
        self.name=name
        self.calories=calories
        self.protein=protein
        self.carbohydrates=carbohydrates
        self.fat=fat

def calculate_nutrition(food_list):
    total_cal=0
    total_protein=0
    total_carb=0
    total_fat=0
    for food in food_list:
        total_cal+=food.calories
        total_protein+=food.protein
        total_carb+=food.carbohydrates
        total_fat+=food.fat
    print('The total calories are:',total_cal,'. The total protein is',total_protein,'. The total carbohydrates are',total_carb,'. The total fats are',total_fat,'.')

food_list=[]
flag=True
while flag:
    food_name=input('Please input what you have eaten in 24 h (if no more to add, please input "quit"):')
    if food_name=='quit':
        flag=False
    else:
        calories=float(input('calories the food contain:'))
        protein=float(input('protein:'))
        carbohydrates=float(input('carbohydrates:'))
        fat=float(input('fat:'))
        food_things=food_item(food_name,calories,protein,carbohydrates,fat)
        food_list.append(food_things)
calculate_nutrition(food_list)

