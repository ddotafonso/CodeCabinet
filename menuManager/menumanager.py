import json
class Manager:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        print(f"Welcome to" + " " + self.name)
    
    # This function prints all categories including their menu item and price
    def print_allcategoriesmenu(self, menu):
        formatted = json.dumps(menu, indent=4)
        print(formatted)
        
    # Prints by specying a category
    def list_bycategory(self, category, categories_list):
        for categ_name, categ_info in categories_list.items():
            if category == categ_name:
                formatted = json.dumps(categ_info, indent=4)
                print(formatted)
        
    # This function prints only the categories name
    def print_onlycategories(self, categories):
        for categ_name, categ_info in categories.items():
                print('Category:',categ_name)
        
    # This function adds an Item in any of the categories
    def add_item(self, categories, category_name, item , item_price):
            for categ_name, categ_info in categories.items():
                categories[category_name][item] = item_price
            
    def inactivate_activate(self, categories_list, item, menu):
        for categ_name, categ_info in categories_list.copy().items():
            for key, value in categ_info.items():
                if item == key:
                    menu[categ_name][item] = value
                    del categories_list[categ_name]
                
                
                        
                    
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
            
categories = {
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




# colds['Cold Drinks']['Iced Tea'] = '5'
# print(hots)
kfc = Manager("KFC")
# # kfc.getName()
# kfc.add_item(categories, 'Hot Drinks', 'Muled whine', 10)
# kfc.add_item(categories, 'Hot Drinks', 'whine', 10)
# kfc.add_item(categories, 'Hot Drinks', 'Tea', 10)
# kfc.print_onlycategories(categories)
# kfc.inactivate_item(categories, 'Hot dog', inactive_menu)
# kfc.inactivate_item(categories, 'Cake', inactive_menu)
# kfc.inactivate_item(categories, 'Pizza', inactive_menu)
# kfc.print_allcategoriesmenu(categories)
kfc.list_bycategory('Fast Foods', categories)
# print(categories)