import random
import requests
import concurrent.futures
import string
import time


todo_url = "http://localhost:8000/todos"


def get_todo_request():
    response = requests.get(todo_url)
    return response.status_code

i = 2
def post_todo_reuqest():
    global i
    random_number = random.random()
    data = {
        'id': i,
        'item': generate_random_word()
        }
    i = i+1
    response = requests.post(todo_url, json=data)
    return response.status_code, i

def generate_random_word():
    length = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def put_todo_request(int = i):
    data = {
        'id': i,
        'item': generate_random_word()
    }
    response = requests.put(f"{todo_url}/{i}", json=data)
    return response.status_code



# Function to generate random traffic
def generate_traffic(num_requests):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for _ in range(num_requests):
            random_number = random.random()
            if random_number > 0.9:
                futures.append(executor.submit(put_todo_request))
            elif random_number < 0.4:
                futures.append(executor.submit(post_todo_reuqest))
            else:
                futures.append(executor.submit(get_todo_request))

        concurrent.futures.wait(futures)

        results = [future.result() for future in futures]
        return results
p= True
while p == True:
    traffic_results = generate_traffic(10)
    time.sleep(10)
    print(traffic_results)

