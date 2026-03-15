QUESTIONS 1: ES 6 (Convert the following code into promises instead of callbacks. )
ANSWER : 
          const f = firstName =>
          new Promise((resolve, reject) =>
          setTimeout(() => 
          firstName ? resolve(`${firstName} Turing`) : reject(new Error('firstName is required')), 
          2000
          )
          );
        
        
        f('Alan').then(console.log).catch(console.error); // Logs: Alan Turing
        f(null).then(console.log).catch(console.error);   // Logs: Error: firstName is required


---------------------------------------------------------------------------------------------------------------------------------------------------------------------
QUESTION 2: Python

using selenium

# --------------------------------------------------------------- code :--------------------- 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from collections import Counter
import re
import time

def count_words_on_page(url):
    """
    Fetches a URL rendered by JavaScript, extracts text, and counts word frequency.
    
    :param url: str, HTTP or HTTPS URL
    :return: dict {word -> frequency}
    """
    # Set up Selenium with headless Chrome
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)  # Make sure chromedriver is installed
    
    try:
        driver.get(url)
        time.sleep(5)  # Wait for JS to generate content 

        # Extract all visible text
        text = driver.find_element(By.TAG_NAME, "body").text

        # Normalize text: lowercase, split by words
        words = re.findall(r'\b\w+\b', text.lower())
        word_count = Counter(words)

        return dict(word_count)

    finally:
        driver.quit()

# Example usage
url = "https://loremipsum.io/generator/?n=5&t=p"
result = count_words_on_page(url)
print(result) 


# ----------------------------------------------------------result ----------------------


{'lorem': 9, 'ipsum': 9, 'font': 2, 'generator': 6, 'name': 2, 'plugins': 2, 'placeholders': 2, 'generators': 2, 'english': 2, 'quickly': 1, 'and': 2, 'easily': 1, 'generate': 2, 'placeholder': 1, 
'text': 1, 'select': 1, 'the': 1, 'number': 1, 'of': 1, 'characters': 1, 'words': 2, 'sentences': 2, 'or': 1, 'paragraphs': 2, 'hit': 1, 'copy': 1, 'dolor': 5, 'sit': 5, 'amet': 5, 'consectetur': 5, 
'adipiscing': 5, 'elit': 5, 'quisque': 5, 'faucibus': 5, 'ex': 5, 'sapien': 5, 'vitae': 5, 'pellentesque': 5, 'sem': 5, 'placerat': 5, 'in': 5, 'id': 5, 'cursus': 5, 'mi': 5, 'pretium': 5, 'tellus': 5,
'duis': 5, 'convallis': 5, 'tempus': 5, 'leo': 5, 'eu': 5, 'aenean': 5, 'sed': 5, 'diam': 5, 'urna': 5, 'tempor': 5, 'pulvinar': 5, 'vivamus': 5, 'fringilla': 5, 'lacus': 5, 'nec': 5, 'metus': 5, 
'bibendum': 5, 'egestas': 5, 'iaculis': 5, 'massa': 5, 'nisl': 5, 'malesuada': 5, 'lacinia': 5, 'integer': 5, 'nunc': 5, 'posuere': 5, 'ut': 5, 'hendrerit': 5, 'semper': 5, 'vel': 5, 
'class': 5, 'aptent': 5, 'taciti': 5, 'sociosqu': 5, 'ad': 5, 'litora': 5, 'torquent': 5, 'per': 5, 'conubia': 5, 'nostra': 5, 'inceptos': 5, 'himenaeos': 5, '2015': 1, '2026': 1, 'privacy': 1, 
'policy': 1, 'sitemap': 1, 'more': 1, 'tools': 1, 'glyphy': 1, 'language': 1, 'wa': 1, 'sai': 1}



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

QUESTION 4: Algorithms


def target_expression(nums, target):
    n = len(nums)
    
    def backtrack(i, current_sum, expr):
        if i == n:
            if current_sum == target:
                return expr
            return None
        
        # Try adding nums[i]
        add_expr = f"{expr} + {nums[i]}" if expr else f"{nums[i]}"
        res = backtrack(i + 1, current_sum + nums[i], add_expr)
        if res is not None:
            return res
        
        # Try subtracting nums[i]
        sub_expr = f"{expr} - {nums[i]}" if expr else f"{nums[i]}"
        res = backtrack(i + 1, current_sum - nums[i], sub_expr)
        if res is not None:
            return res
        
        return None
    
    result = backtrack(0, 0, "")
    if result:
        return f"{target} = {result}"
    return None

# -----------------------------
# Take input from the user
# -----------------------------
nums_input = input("Enter a list of integers separated by spaces or commas: ")

# Replace commas with spaces, then split
nums = list(map(int, nums_input.replace(',', ' ').split()))
target = int(input("Enter the target integer: "))

solution = target_expression(nums, target)
if solution:
    print("Solution:", solution)
else:
    print("No solution found.")
