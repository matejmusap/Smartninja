from models.user import User

# Handles CRUD methods for User objects


class UserRepository():
    @staticmethod
    def create(first_name, email, date_of_birth):
        new_user = User(first_name=first_name, email=email,
                        date_of_birth=date_of_birth)
        user_key = new_user.put()
        return user_key

    @staticmethod
    def read(first_name):
        result = User.query(User.first_name == first_name).fetch(1)
        if result:
            return result[0]

    @staticmethod
    def readAll():
        return User.query().order(User.first_name)

    @staticmethod
    def update(first_name, changes):
        saved_user = UserRepository.read(first_name)
        if changes.first_name:
            saved_user.first_name = changes.first_name
        if changes.date_of_birth:
            saved_user.date_of_birth = changes.date_of_birth
        return saved_user.put()

    @staticmethod
    def delete(first_name):
        saved_user = UserRepository.read(first_name)
        saved_user.delete()
