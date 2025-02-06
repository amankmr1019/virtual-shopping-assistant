# tools.py

import random

"""
    Initialize the virtual assistant with mock e-commerce data.
"""
mock_database = [
    {"name": "Red T-Shirt", "color": "Red", "price": 15.99, "size": "M", "platform": "Amazon"},
    {"name": "Blue Jeans", "color": "Blue", "price": 39.99, "size": "L", "platform": "eBay"},
    {"name": "White Sneakers", "color": "White", "price": 59.99, "size": "9", "platform": "Zalando"},
    {"name": "Black Jacket", "color": "Black", "price": 89.99, "size": "XL", "platform": "Myntra"},
    {"name": "Green Hoodie", "color": "Green", "price": 49.99, "size": "M", "platform": "Flipkart"}
]

# Mock promo_codes for different discounts
promo_codes = {
    "DISCOUNT10": 0.10,  # 10% discount
    "SAVE20": 0.20,  # 20% discount
    "FREESHIP": 0.00  # No discount but free shipping logic can be implemented
}

# Mock return policies for different platforms
return_policies = {
    "Amazon": "30 days return policy. Full refund if the product is unused and in original packaging.",
    "eBay": "Returns accepted within 14 days. Buyer pays return shipping.",
    "Zalando": "Returns within 30 days for a full refund. Free returns for all items.",
    "Myntra": "7 days return policy. Refunds processed after item is returned in unused condition.",
    "Flipkart": "10 days return policy. No return on used or opened products."
}

def search_products(name=None, color=None, price_range=None, size=None):
    """
    Search for products based on the given criteria.
    
    :param name: (str) Name or keyword related to the product.
    :param color: (str) Desired color of the product.
    :param price_range: (tuple) Price range as (min_price, max_price).
    :param size: (str) Desired size of the product.
    :return: (list) A list of matching products.
    """
    
    results = []
    
    for product in mock_database:
        if name and name.lower() not in product["name"].lower():
            continue
        if color and color.lower() != product["color"].lower():
            continue
        if price_range:
            min_price, max_price = price_range
            if not (min_price <= product["price"] <= max_price):
                continue
        if size and size.lower() != product["size"].lower():
            continue
        
        results.append(product)
    
    return results

def estimate_shipping(location, delivery_date):
    """
    Estimate shipping cost and feasibility based on user location and desired delivery date.
    
    :param location: (str) User's delivery location.
    :param delivery_date: (str) Desired delivery date (YYYY-MM-DD).
    :return: (dict) Shipping cost, feasibility, and estimated delivery time.
    """
    import random
    
    shipping_cost = random.uniform(5, 20)  # Simulating shipping cost between $5 and $20
    estimated_days = random.randint(2, 7)  # Simulating delivery between 2 to 7 days
    
    return {
        "location": location,
        "requested_delivery_date": delivery_date,
        "estimated_delivery_time": f"{estimated_days} days",
        "shipping_cost": f"${shipping_cost:.2f}",
        "feasibility": "Possible" if estimated_days <= 7 else "Not Possible"
    }

def apply_promo_code(base_price, promo_code):
    """
    Apply a discount or promo code to adjust the final price.
    
    :param base_price: (float) Original price of the product.
    :param promo_code: (str) Discount or promo code entered by the user.
    :return: (dict) Adjusted price and discount applied.
    """
    
    if promo_code in promo_codes:
        discount = promo_codes[promo_code] * base_price
        final_price = base_price - discount
    else:
        discount = 0.00
        final_price = base_price
    
    return {
        "original_price": f"${base_price:.2f}",
        "discount": f"-${discount:.2f}" if discount > 0 else "$0.00",
        "final_price": f"${final_price:.2f}",
        "promo_code_applied": promo_code if discount > 0 else "Invalid Code"
    }

def compare_competitor_prices(product_name):
    """
    Compare prices of a specific product across different online stores.
    
    :param product_name: (str) Name of the product to compare.
    :return: (list) A list of price comparisons from various competitors.
    """
    
    results = [product for product in mock_database if product_name.lower() in product["name"].lower()]
    
    return sorted(results, key=lambda x: x["price"])  # Sorting by price (lowest first)

def check_return_policy(platform):
    """
    Check the return policy for a specified e-commerce platform.
    
    :param platform: (str) The platform (e.g., Amazon, eBay).
    :return: (str) Return policy details.
    """
    return return_policies.get(platform, "Return policy information is not available for this platform.")
