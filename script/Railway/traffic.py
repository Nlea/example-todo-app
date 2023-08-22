import requests
import random
import string
import concurrent.futures
import time

dns_name = "example-todo-app"
port = 8000
url = f"http://{dns_name}:{port}/todos"

def get_todo_request():
    response = requests.get(url)
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
    response = requests.post(url, json=data)
    return response.status_code, i

def generate_random_word():
    length = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def put_todo_request(int = i):
    data = {
        'id': i,
        'item': generate_random_word()
    }
    response = requests.put(f"{url}/{i}", json=data)
    return response.status_code


def main(num_requests):
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
 

if __name__ == "__main__":
    p = True
    n = 100
    while p == True:
       time.sleep(3)
       results = main(n)
       print(results)