from PySide6.QtWidgets import QComboBox
from db.models.Masters import Rules
from db.SqliteDb import get_db_session

class ComboBtnSetup:
    def rules_list(self) -> list[dict]:
        with get_db_session() as session:
            data = session.query(Rules).all()
            return [
                {
                    "id": r.id,
                    "name": r.name,
                    "config": r.config
                } for r in data
            ]

    def combo_btn_setup(self, combo: QComboBox, data_list: list[dict], display_key: str, placeholder: str):
        combo.clear()
        combo.addItem(f"-- {placeholder} --", None)
        
        for item in data_list:
            display_text = str(item.get(display_key, ""))
            combo.addItem(display_text, item)
            
        combo.setCurrentIndex(0)