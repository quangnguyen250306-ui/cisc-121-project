# cisc-121-final-project

# Linear Search

I chose to implement linear search as it is the most fundamental searching algorithm. While it is simpler than binary search, it provides a clear model to explain how search operations work step-by-step.

The linear search algorithm, given a list and a target value, is performed as follows:
- Start from the first element of the list.
- Compare each element with the target.
- If the target is equal to the current element, return the index.
- Otherwise, move to the next element.
- Repeat until the target is found or the end of the list is reached.
- If the end is reached without finding the target, return that the target is not in the list.

---

## Abstraction

The goal is to create an app which someone can use to understand linear search. The application is designed to be simple, readable, and informative.

The algorithm logic is separated from the UI logic to improve clarity. This allows users to focus on understanding how linear search works without understanding the interface implementation.

The user interface displays each step of the algorithm, showing:
- The index currently being checked
- The value at that index
- The result of the comparison

This makes it clear how linear search scans the list.

---

## Design

The program is designed to allow the user to generate a random array and pick a target element of any value, whether or not it exists in the array.

The user can then press a button to perform the search. The program outputs:
- The index of the target (if found)
- A step-by-step log of the search process

Each step includes:
- Step number
- Index checked
- Value at that index
- Decision made (match or continue)

---

# Problem Breakdown

We need an input array of some length with a range of elements. The length is set to 15 to keep the output manageable and easy to understand.

The array does not need to be sorted, since linear search works on any list.

We use Python’s `random.sample()` function to generate unique elements and avoid duplicates.

The algorithm iterates through the list and compares each element to the target until it finds a match or reaches the end.

Edge cases handled:
- Target exists in the list
- Target does not exist
- Invalid target input
- No list generated

---

## Testing

All possible cases were tested to ensure correct behavior:

- A valid target in the array  
→ returns correct index and stops early  

- A valid target not in the array  
→ searches entire list and returns not found  

- An invalid target  
→ displays an error message  

- No array  
→ prompts user to generate a list first  

- Execution log  
→ shows all steps clearly for user understanding  

*(You can insert screenshots here if needed)*

---

## How to run

Use this Hugging Face link to access the link: https://huggingface.co/spaces/Siu4Ronaldo/cisc-121-project/tree/main

## Acknowledgement

The implementation was in part coded by Grok and Gemini.
