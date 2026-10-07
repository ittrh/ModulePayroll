from db.SqliteDb import get_db_session
from db.models.Masters import Rules

class RulesCrud:
    def __init__(self):
        self.rules_data: list[dict] = []
    
    def get_all_rules(self) -> list[dict]:
        with get_db_session() as session:
            query = session.query(Rules).all()
            self.rules_data = []
            for rules in query:
                item = {
                    "id": getattr(rules, 'id', None),
                    "name": rules.name,
                    "config": rules.config
                }
                self.rules_data.append(item)
        return self.rules_data
    
    def create_rules(self, data: dict) -> None:
        with get_db_session() as session:
            rule = Rules(
                id=data['id'],
                name=data['name'],
                config=data['config']
            )
            session.add(rule)
            session.commit()