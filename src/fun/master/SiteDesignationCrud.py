from db.SqliteDb import get_db_session
from db.models.Masters import Site, Employee

class SiteCrud:
    def create_site(self, data: dict) -> None:
        site_id = data.get("id")
        site_name = data.get("name")

        if not site_id or not site_name:
            raise ValueError("ID dan Nama Site wajib diisi!")

        with get_db_session() as session:
            # Menggunakan session.get untuk standar SQLAlchemy 2.0+
            existing_site = session.get(Site, site_id)
            if existing_site:
                raise ValueError(f"Site dengan ID '{site_id}' sudah ada!")

            site = Site(id=site_id, name=site_name)
            session.add(site)
            session.commit()

    def get_all_site(self) -> list[dict]:
        with get_db_session() as session:
            sites = session.query(Site).all()
            return [{"id": site.id, "name": site.name} for site in sites]

    def update_site(self, data: dict) -> None:
        site_id = data.get("id")
        if not site_id:
            raise ValueError("ID Site tidak valid untuk pembaharuan.")

        with get_db_session() as session:
            site = session.get(Site, site_id)
            if not site:
                raise ValueError(f"Site dengan ID '{site_id}' tidak ditemukan.")

            if "name" in data:
                site.name = data["name"]

            session.commit()

    def delete_site(self, site_id: str) -> None:
        with get_db_session() as session:
            site = session.get(Site, site_id)
            if not site:
                raise ValueError(f"Site dengan ID '{site_id}' tidak ditemukan.")

            is_used = session.query(Employee).filter(Employee.site_id == site_id).first()
            if is_used:
                raise ValueError(
                    f"Site '{site.name}' tidak dapat dihapus karena masih digunakan."
                )

            session.delete(site)
            session.commit()

    def search_site(self, keyword: str) -> list[dict]:
        if not keyword or not keyword.strip():
            return self.get_all_site()

        search_term = f"%{keyword.strip()}%"
        with get_db_session() as session:
            # Langsung querying pencarian ke DB (case-insensitive)
            results = (
                session.query(Site)
                .filter((Site.id.ilike(search_term)) | (Site.name.ilike(search_term)))
                .all()
            )
            return [{"id": site.id, "name": site.name} for site in results]