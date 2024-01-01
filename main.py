from collections import namedtuple, defaultdict, deque
from classes import Composition, Elementary, Composite, Product

# Elementary instances
apple = Elementary("Apple", "FRT1", 10)
orange = Elementary("Orange", "FRT2", 8.5)
banana = Elementary("Banana", "FRT3", 7)

# Composition instances
apple_comp = Composition(apple, 3)
orange_comp = Composition(orange, 2)

# Composite instance
fruit_basket_components = [apple_comp, orange_comp]
fruit_basket = Composite("Fruit Basket", "BASK1", 5, fruit_basket_components)

# List of elementary and composite products created
products_list = [apple, orange, banana, fruit_basket]


def info():
    for product in products_list:
        if isinstance(product, Elementary):
            print(f"{product.get_name}, Price: {product.get_price}\n")
        elif isinstance(product, Composite):
            T = []
            for constituent in product.get_constituents:
                info = f"{constituent.get_product.get_name}(Price: {constituent.get_product.get_price})"
                T.append(info)
            constituents_info = " and ".join(T)
            print(f"{product.get_name} composed of {constituents_info}\n")

info()

# Define a namedtuple for Description
Description = namedtuple('Description', ['Product', 'Detail'])

# Create defaultdict to store descriptions
descriptions = defaultdict(dict)

# Create a deque to store description dictionaries
descriptions_deque = deque()

# Generate Description for each product and convert to dictionary
for product in products_list :
    if isinstance(product, Composite):
        constituents_info = " and ".join([constituent.get_product.get_name for constituent in product.get_constituents])
        detail = f"{product.get_name} is a Composite Product of {constituents_info}"
    else:
        detail = f"{product.get_name} is an Elementary Product"

    # Create Description namedtuple
    product_description = Description(Product=product.get_name, Detail=detail)

    # Convert Description namedtuple to dictionary
    description_dict = product_description._asdict()
    
    # Add dictionary to defaultdict with product name as key
    descriptions[product.get_name] = description_dict
    
# Display the descriptions (stored in defaultdict)
for product_name, desc in descriptions.items():
    print(f"{product_name}: {desc}")

# Extend the deque with description dictionaries from defaultdict
descriptions_deque.extend(descriptions.values())



