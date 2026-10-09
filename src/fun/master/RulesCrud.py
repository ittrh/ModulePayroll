from db.SqliteDb import get_db_session
from db.models.Masters import Rules, SalaryComponents

class RulesCrud:
    def create_rules(self, data: dict) -> None:
        with get_db_session() as session:
            existing_rule = session.query(Rules).get(data['id'])
            if existing_rule:
                raise ValueError(f"Rule dengan ID '{data['id']}' sudah ada!")
            
            rule = Rules(
                id=data['id'],
                name=data['name'],
                config=data['config']
            )
            session.add(rule)
            session.commit()        
            
    def update_rules(self, data: dict) -> None:
        """Memperbarui data rule berdasarkan ID."""
        with get_db_session() as session:
            rule = session.query(Rules).get(data['id'])
            if rule:
                rule.name = data.get('name', rule.name)
                rule.config = data.get('config', rule.config)
                session.commit()
            else:
                raise ValueError(f"Rule dengan ID '{data['id']}' tidak ditemukan.")
    
    def delete_rules(self, id: str):
        with get_db_session() as session:
            rule = session.query(Rules).get(id)
            
            if not rule:
                raise ValueError(f"Rule dengan ID '{id}' tidak ditemukan.")
            
            is_used = session.query(SalaryComponents).filter(SalaryComponents.rules_id == id).first()
            
            if is_used:
                raise ValueError(
                    f"Rule '{rule.name}' tidak dapat dihapus karena masih digunakan."
                )
            session.delete(rule)
            session.commit()