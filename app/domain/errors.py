class NotFoundError(Exception):
    def __init__(self, resource: str, resource_id: str) -> None:
        super().__init__(f"No such {resource}: '{resource_id}'")
        self.resource = resource
        self.resource_id = resource_id
