from database import Database


class Note:
    def __init__(self, note_id, title, content):
        self.note_id = note_id
        self.title = title
        self.content = content

    def json(self):
        return{
            'note_id' : self.note_id,
            'title' : self.title,
            'content': self.content
        }

    def save_to_db(self):
        Database.insert(collection='notes', data=self.json())

    @classmethod
    def from_mongo(cls, note_id):
        post_data = Database.find_one(collection='notes', query={'note_id': note_id})
        print(post_data)
        return Database.find_one(collection='notes', query={'note_id': note_id})
