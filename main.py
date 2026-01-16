from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health_check():
    """
    Endpoint to confirm api is running
    """
    return {"status": "ok"}


items = [
    {"id": 1, "name": "Foo Item 1"},
    {"id": 2, "name": "Bar Item 2"},
    {"id": 3, "name": "Baz Item 3"},
]


@app.get("/items")
async def read_items(page: int = 1, size: int = 10):
    """
    Endpoint to get list of items
    ?page: Page number for pagination
    ?size: Number of items per page
    """
    getItems = items[(page - 1) * size : page * size]
    return {
        "items": getItems,
        "page": page,
        "size": size,
        "total": len(items),
        "total_pages": (len(items) + size - 1) // size,
    }


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Endpoint to get a specific item by ID
    """
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


@app.post("/items")
async def create_item(item: dict):
    """
    Endpoint to create a new item
    """
    items.append(item)
    return item
