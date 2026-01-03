class EC2Instance:
    def __init__(self, instance_id, name):
        self.instance_id = instance_id
        self.name = name
        self.status = "stopped"

    def start(self):
        self.status = "running"
        print(f"{self.name} started")

    def stop(self):
        self.status = "stopped"
        print(f"{self.name} stopped")


class EC2Manager:
    def __init__(self):
        self.instances = []

    def add_instance(self, instance):
        self.instances.append(instance)

    def start_all(self):
        for instance in self.instances:
            instance.start()

    def stop_all(self):
        for instance in self.instances:
            instance.stop()

    def get_running_count(self):
        count = 0
        for instance in self.instances:
            if instance.status == "running":
                count += 1
        return count


# 인스턴스 생성
web = EC2Instance("i-001", "web-server")
db = EC2Instance("i-002", "db-server")
cache = EC2Instance("i-003", "cache-server")

# 매니저에 등록
manager = EC2Manager()
manager.add_instance(web)
manager.add_instance(db)
manager.add_instance(cache)

# 모두 시작
manager.start_all()
print(manager.get_running_count())  # 3

# 일부 중지
db.stop()
print(manager.get_running_count())  # 2