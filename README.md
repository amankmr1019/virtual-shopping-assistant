# virtual-shopping-assistant
A virtual shopping assistant using multiple e-commerce tools

**Project Overview**

The Virtual Shopping Assistant is an AI-powered tool that helps users browse and shop products from multiple e-commerce platforms. It allows users to:
1. Search for products based on specific criteria (name, price range, size, etc.)
2. Apply discount codes
3. Estimate shipping costs and delivery times
4. Compare prices across various competitors
5. Check return policies of products
6. This assistant is designed to simulate the experience of browsing and shopping across multiple online stores by integrating several tools to perform specific tasks.


**Project Setup**

**Installation Requirements**

1.	Clone this repository:

      git clone https://github.com/amankmr1019/virtual-shopping-assistant.git
    
      cd virtual-shopping-assistant

2.	Install dependencies:

  	pip install -r requirements.txt
  	
    **Dependencies:**

      	Python 3.7+
    
      	random (for simulating shipping costs and delivery times)


**Directory Structure**

    virtual-shopping-assistant/
    
    ├── agent.py                # Main agent script that integrates all tools
    
    ├── tools.py                # Mock functions for different tools
    
    ├── requirements.txt        # List of required Python libraries
    
    └── README.md               # Project documentation


**Running the Project**

    To run the virtual shopping assistant, execute the agent.py script. This script will initialize the agent and demonstrate its functionality with sample queries.
    
    _python agent.py_


**Agent Functionality**

**1. Search Products**

The search_products method allows the user to search for products based on criteria such as product name, color, price range, and size.

**2. Estimate Shipping**

The estimate_shipping method provides an estimate for the shipping cost and delivery time based on the user's location and desired delivery date.

**3. Apply Promo Code**

The apply_promo_code method simulates the application of a discount code to adjust the final price of a product.

**4. Competitor Price Comparison**

The compare_competitor_prices method compares prices for a specific product across different online platforms to help the user find the best deal.

**5. Return Policy Checker**

The check_return_policy method provides a mock return policy for a given e-commerce site, helping users make informed decisions.

**System Design**

**Agent Architecture**

The virtual shopping assistant consists of several components that work together to provide the final answer:

    **1. Reasoning:** Based on the user's query, the agent determines which tools need to be invoked. For example, if the user asks about shipping costs, the agent invokes the estimate_shipping tool.
    
    **2. Tool Calls:** Once the reasoning is complete, the relevant tools are called with the appropriate parameters. Each tool performs a specific task, like searching products or calculating shipping costs.
    
    **3. Observation / Integration:** The agent integrates the outputs of the tools to generate a coherent response for the user. The tools return data that the agent uses to form the final answer, including product details, price comparisons, or shipping information.


**Prompt Structure**

    **1. System Prompt:** Defines the role and available tools for the agent (searching products, estimating shipping, applying promo codes, comparing prices, checking return policies).
    
    **2. User Queries:** Example queries are provided to guide the agent in performing the right tasks based on the user's needs.
    
    **3. Agent Output:** The agent should clearly explain what tools it used to arrive at the response, e.g., "I found the following products matching your criteria..." and "I applied the discount code 'SAVE10' to your order."


**Demonstration Tasks**

    **1. Task A: Basic Item Search + Price Constraint**
      **Query:** "Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code ‘SAVE10’?"
      **Agent Steps:** Invoke the product search and apply the promo code.
      
    **2. Task B: Shipping Deadline**
      **Query:** "I need white sneakers (size 8) for under $70 that can arrive by Friday."
      **Agent Steps:** Use the search and shipping estimator tools.
      
    **3. Task C: Competitor Price Comparison**
      **Query:** "I found a ‘casual denim jacket’ at $80 on SiteA. Any better deals?"
      **Agent Steps:** Compare prices across platforms.
      
    **4. Task D: Returns & Policies**
      **Query:** "I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?"
      **Agent Steps:** Check return policy for the specified site.
      
    **5. Task E: Complex Interaction**
      **Query:** "Find a red T-shirt under $30, that can be delivered by tomorrow, and can I use ‘DISCOUNT10’?"
      **Agent Steps:** Invoke search, shipping, and promo code tools.


**Challenges and Improvements**

**Challenges**

    **1. Handling Multiple Tools:** Combining outputs from different tools (e.g., search, shipping, and discount tools) into one coherent response required careful management of data.
    
    **2. Ambiguity in User Queries:** Handling queries that don’t explicitly specify details, like size or color, required building logic for default values or asking follow-up questions.

**Improvements**

    **1. Real-Time Integration:** Integrating with real e-commerce APIs for live product data instead of using mock data.
    
    **2. Better Error Handling:** Incorporating more robust error handling to deal with edge cases, like invalid promo codes or out-of-stock products.


**Comparative Conceptual Map**

    **Approach 1:** The agent uses a simple, rule-based approach to decide which tools to invoke based on the user’s query.
    
    **Approach 2:** The agent integrates NLP techniques to better understand and disambiguate user queries, possibly using a more complex decision-making framework (e.g., Reinforcement Learning).


**Design Decisions**

    **Modular Design:** Each tool (search, shipping, promo codes, etc.) is implemented in its own function, making the code easy to extend.
    
    **Mock Data:** Using mock data for the demonstration instead of integrating real-time e-commerce data, to simplify the development and testing process.


**Future Work**

    **1. NLP Integration:** Incorporating natural language processing for more intelligent query handling and better understanding of user intent.
    
    **2. Real Data Integration:** Connecting the system to actual e-commerce APIs like Amazon, eBay, or Flipkart for live product and price data.


**References**

1. ReAct: Synergizing Reasoning and Acting in Language Models - https://arxiv.org/abs/2205.03566
2. Toolformer: Language Models Can Teach Themselves to Use Tools - https://arxiv.org/abs/2203.07047
4. ReST meets ReAct: Self-Improvement for Multi-Step Reasoning LLM Agent - https://arxiv.org/abs/2305.05358
5. Chain of Tools: Large Language Model is an Automatic Multi-tool Learner - https://arxiv.org/abs/2302.07569
6. Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models - https://arxiv.org/abs/2205.14118

