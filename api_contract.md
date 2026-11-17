# Lab 5 API contract

The frontend reads the task feed with `GET http://localhost:8080/frontend_feed.json`.
The local Python HTTP server returns `200 OK` with `Content-Type: application/json`.
The request has no body and requires no token.

The response is a JSON array. Each task has exactly three required fields.

| Field | Type | Meaning |
| --- | --- | --- |
| `task_id` | integer | Task ID from `id` |
| `label` | string | Task title from `title` |
| `is_done` | boolean | Completion status from `completed` |

Example response shape with one task from the feed.

```json
[
  {
    "task_id": 1,
    "label": "delectus aut autem",
    "is_done": false
  }
]
```

`api_client.py` fetches tasks from `https://jsonplaceholder.typicode.com/todos`,
keeps records with `userId == 1`, and writes `frontend_feed.json`.
