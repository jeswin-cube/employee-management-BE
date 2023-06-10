from pydantic import BaseModel


class EmployeeListSchema:
    class Put(BaseModel):
        manager_id: int
