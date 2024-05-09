import threading


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        action, product, quantity = request
        if action == 'receipt':
            self.data[product] = self.data.get(product, 0) + quantity
        elif action == 'shipment':
            if product in self.data and self.data[product] > 0:
                self.data[product] -= quantity

    def run(self, requests):
        threads = []
        for request in requests:
            thread = threading.Thread(target=self.process_request, args=(request,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        print(self.data)


warehouse_manager = WarehouseManager()
requests = [
    ('receipt', 'product1', 100),
    ('receipt', 'product2', 150),
    ('receipt', 'product3', 300),
    ('shipment', 'product1', 30),
    ('shipment', 'product2', 50),
    ('shipment', 'product3', 90),
]

warehouse_manager.run(requests)

print(warehouse_manager.data)
