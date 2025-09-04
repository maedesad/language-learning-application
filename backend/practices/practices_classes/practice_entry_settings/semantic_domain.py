from backend.user.user_class import User  # Importing the User class

class SemanticDomain:
    def __init__(self, user: User):
        self.__user = user
        self.__user_semantic_domains: list[str] = []
        self.__selected_semantic_domain: str | None = None
        self.__use_semantic_domain: bool = False

    # ------------------- Use Vocab ------------------- 
    def enable_semantic_domain(self):
        self.__use_semantic_domain = True

    def disable_semantic_domain(self):
        self.__use_semantic_domain = False

    def is_semantic_domain_enabled(self) -> bool:
        return self.__use_semantic_domain

    # ---------------- User ----------------
    def get_user(self) -> User:
        return self.__user

    def set_user(self, user: User):
        self.__user = user
        self.set_user_semantic_domains()  # Refresh semantic domains when user changes

    # ---------------- User Semantic Domains ----------------
    def get_user_semantic_domains(self) -> list[str] | str:
        """Return user's semantic domains. If list is empty, return placeholder text."""
        return self.__user_semantic_domains if self.__user_semantic_domains else "No semantic domains available."

    def set_user_semantic_domains(self):
        """Fetch semantic domains from the user object."""
        self.__user_semantic_domains = self.__user.get_semantic_domains()

    # ---------------- Selected Semantic Domain ----------------
    def get_selected_semantic_domain(self) -> str | None:
        return self.__selected_semantic_domain

    def set_selected_semantic_domain(self, domain: str):
        """Set the selected semantic domain if it exists in user's list."""
        if domain in self.__user_semantic_domains:
            self.__selected_semantic_domain = domain
        else:
            raise ValueError(f"'{domain}' is not a valid semantic domain for this user.")