from app.db.base import Base
import app.models  # noqa: F401


if __name__ == "__main__":
    print(sorted(Base.metadata.tables.keys()))
