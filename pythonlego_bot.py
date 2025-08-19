import requests

API_KEY = "cc8012b530ce88568ed187108d7c145f"
BASE_URL = "https://rebrickable.com/api/v3/lego/sets/"

def search_lego_set(query):
    url = f"{BASE_URL}?search={query}"
    headers = {"Authorization": f"key {API_KEY}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        if results:
            set_info = results[0]
            return f"Found: {set_info['name']} (Set Num: {set_info['set_num']})"
        else:
            return "No sets found."
    else:
        return "Error fetching data."

def chatbot():
    print("🤖 LEGO Bot: Tell me about the LEGO set you’re looking for!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("🤖 LEGO Bot: Goodbye!")
            break
        result = search_lego_set(user_input)
        print("🤖 LEGO Bot:", result)

if __name__ == "__main__":
    chatbot()
