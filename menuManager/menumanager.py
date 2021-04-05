import json
class Manager:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        print(f"Welcome to" + " " + self.name)
        
    # This function prints only the categories names
    def print_onlycategories(self, menu_list):
        for categ_name, categ_info in menu_list.items():
                print('Category:',categ_name)
    
    # Exercise A: This function prints all categories including their menu item and price
    def print_allcategoriesmenuitems(self, menu_list):
        formatted = json.dumps(menu_list, indent=4)
        print(formatted)
        
    # Exercise D: Prints by specifying a category
    def list_bycategory(self, category, menu_list):
        for categ_name, categ_info in menu_list.items():
            if category == categ_name:
                formatted = json.dumps(categ_info, indent=4)
                print(formatted)
        
    # Exercise B: This function adds an Item in any of the categories
    def add_item(self, menu_list, category_name, item , item_price):
            for categ_name, categ_info in menu_list.items():
                menu_list[category_name][item] = item_price
                print(menu_list)
            
    # Exercise D, E: Activating and deactivating a menu item
    def inactivate_activate(self, menu_list, item, new_menu):
        for categ_name, categ_info in menu_list.copy().items():
            for key, value in categ_info.copy().items():
                if item == key:
                    new_menu[categ_name][item] = value
                    del menu_list[categ_name][item]
                    print(menu_list)
                    
    def remove_menu_item(self, item, menu_list):
        for categ_name, categ_info in menu_list.copy().items():
            for key, value in categ_info.copy().items():
                if item == key:
                    del menu_list[item]
                    print(menu_list)
                
                
                        
                    
inactive_menu = {
    'Hot Drinks':{
    },
    'Cold Drinks': {
    },
    'Fast Foods': {
    },
    'Desserts': {
    }
}
            
active_menu = {
    'Hot Drinks':{
        'Hot chocolate': '5', 
        'Cappucino': '3', 
        'Tea' :'2'},
    'Cold Drinks': {
        'Coca Cola': '3', 
        'Fanta' : '3', 
        'Cider' : '2'},
    'Fast Foods': {
        'Burger': '5', 
        'Hot dog': '3', 
        'Pizza': '12'},
    'Desserts': {
        'Cake': '5', 
        'Brownie': '3', 
        'Ice cream': '4'}
}


kfc = Manager("KFC")
kfc.inactivate_activate(active_menu, 'Cake', inactive_menu)
kfc.inactivate_activate(active_menu, 'Brownie', inactive_menu)
print(inactive_menu)