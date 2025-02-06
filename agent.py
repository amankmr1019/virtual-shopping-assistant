# agent.py

import random
from tools import search_products, estimate_shipping, apply_promo_code, compare_competitor_prices, check_return_policy

class VirtualShoppingAssistant():
    def __init__(self):
        self.available_tools = {
            "search": search_products,
            "shipping": estimate_shipping,
            "discount": apply_promo_code,
            "competitor_price": compare_competitor_prices,
            "return_policy": check_return_policy,
        }
    
    return_policies = {
        "Amazon": "30 days return policy. Full refund if the product is unused and in original packaging.",
        "eBay": "Returns accepted within 14 days. Buyer pays return shipping.",
        "Zalando": "Returns within 30 days for a full refund. Free returns for all items.",
        "Myntra": "7 days return policy. Refunds processed after item is returned in unused condition.",
        "Flipkart": "10 days return policy. No return on used or opened products."
    }
    
    def process_query(self, query):
        """
        Process the user query to decide which tool(s) to invoke and then return the integrated response.
        """
        # Sample decision-making logic based on simple keywords

        if "search" in query:
            product = query.split("search for ")[1]
            results = self.available_tools["search"](product)
            return f"Found products: {results}"
        
        if "shipping" in query:
            product = query.split("shipping for ")[1].split(" on ")
            shipping_details = self.available_tools["shipping"]("user_location", "desired_date")
            return f"Shipping details: {shipping_details}"
        
        if "discount" in query:
            code, price = query.split("apply discount ")[1].split(" to ")
            price = float(price)
            final_price = self.available_tools["discount"](code, price)
            return f"Final price after discount: ${final_price:.2f}"
        
        if "competitor price" in query:
            product = query.split("competitor prices for ")[1]
            prices = self.available_tools["competitor_price"](product)
            return f"Competitor prices: {prices}"
        
        if "return policy" in query:
            platform = random.choice(list(self.return_policies.keys()))
            return_policy = self.available_tools["return_policy"](platform)
            return f"Return policy: {return_policy}"
        
        return "Sorry, I could not understand your request."

if __name__ == "__main__":

    # Iniatiate the agent
    assistant = VirtualShoppingAssistant()

    # Task A: Basic Item Search + Price Constraint
    query = "search for floral skirt under $40 in size S"
    print(assistant.process_query(query))

    # Task B: Shipping Deadline
    query = "shipping for white sneakers size 8 on Amazon"
    print(assistant.process_query(query))

    # Task C: Competitor Price Comparison
    query = "competitor prices for floral skirt"
    print(assistant.process_query(query))

    # Task D: Returns & Policies
    query = "return policy"
    print(assistant.process_query(query))

    # Task E: Combined Tools
    query = "search for floral skirt under $40 and apply discount SAVE10"
    print(assistant.process_query(query))
