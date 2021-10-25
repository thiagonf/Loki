import uuid
import random
import datetime

GET_EXAMPLE_SERVICE_JSON = {
    "id": "0056559d-b2e1-4299-9099-ffa33d42e22b",
    "name": "User Example",
    "age": "20",
    "email": "user_example@test.com"
}

GET_RANDOM_EXAMPLE_SERVICE_JSON = {
    "id": "",
    "order_id": str(uuid.uuid4()),
    "balance": round(random.uniform(1, 100), 2),
    "count_items": round(random.randint(0, 50)),
    "date": datetime.date.today()
}
