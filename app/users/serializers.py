from datetime import datetime
from uuid import uuid4

from .models import User, UserOut


class UserSerializer:
    @staticmethod
    def to_mongo_entity(user: User):
        return {
            '$set': user.dict(),
            '$currentDate': {'date_modified': True},
            '$setOnInsert': {
                'date_created': datetime.utcnow(),
                'user_id': uuid4().hex[:12]
            }
        }

    @staticmethod
    def get_obj_from_db(entity) -> User:
        return User(**entity)


class UserOutSerializer(UserSerializer):
    @staticmethod
    def get_obj_from_db(entity) -> UserOut:
        return UserOut(**entity)
