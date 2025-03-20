
from app.core.database.repositories import SQLAlchemyCoreRepository
from app.orders.models import Order
from app.orders.tables import order_lines_table


class OrderRepository(SQLAlchemyCoreRepository[Order]):
    # override base method since logic is slightly different
    # we save 2 objects in a single transaction to keep consistency and atomicity
    def add_one(self, order_lines_data: list[dict]) -> Order:
        with self.session_factory() as sess:
            order = super().add_one(parent_session=sess)

            # add order lines
            order_lines_table.insert().values(order_lines_data)

        return order