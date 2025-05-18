import requests

def test_simple_get():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    assert response.status_code == 200
    assert "userId" in response.json()

if __name__ == "__main__":
    test_simple_get()
    print("? API test executed successfully!")
