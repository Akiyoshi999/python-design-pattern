class User:
    pass


class UserController:
    def __init__(self):
        self.__user_service = UserService()

    def create(self, user: User) -> User:
        return self.__user_service.create(user)

    def find_by_id(self, id: str) -> User:
        return self.__user_service.find_by_id(id)


class UserService:
    def __init__(self):
        self.__user_repository = UserRdbRepository()

    def create(self, user: User) -> User:
        return self.__user_repository.create(user)

    def find_by_id(self, id: str) -> User:
        return self.__user_repository.find_by_id(id)


class UserRdbRepository:
    def create(self, user: User) -> User:
        print("RDBにUserを登録")
        return user

    def find_by_id(self, id: str) -> User:
        print(f"ID: {id}のユーザーを検索")
        return User()


if __name__ == "__main__":
    user_controller = UserController()
    user_controller.find_by_id("123")
