from base_model import BaseModel

class Review(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id', "")
        self.rating = kwargs.get('rating', 0)

    def to_dict(self):
        review_dict = super().to_dict()
        review_dict.update({
            'user_id': self.user_id,
            'rating': self.rating
        })
        return review_dict