import redis

# Подключение к Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0)


def save_agent(user_id, agent_name, agent_scientific_article, agent_description):
    # Формируем ключ для хранения данных агента
    agent_key = f"user:{user_id}:agent:{agent_name}"
    # Сохраняем данные агента в Redis хеш
    redis_client.hset(agent_key, "name", agent_name)
    redis_client.hset(agent_key, "scientific_article", agent_scientific_article)
    redis_client.hset(agent_key, "description", agent_description)


def delete_agent(user_id, agent_name):
    # Формируем ключ для хранения данных агента
    user_id = str(user_id)
    agent_key = f"user:{user_id}:agent:{agent_name}"
    redis_client.delete(agent_key)


def check_agent_exists(user_id, agent_name):
    agent_key = f"user:{user_id}:agent:{agent_name}"
    # Проверяем существование ключа в Redis хеш
    return redis_client.exists(agent_key)


def get_agent_info(user_id, agent_name):
    agent_info = {}
    agent_key = f"user:{user_id}:agent:{agent_name}"
    agent_info["name"] = redis_client.hget(agent_key, "name").decode("utf-8")
    agent_info["scientific_article"] = redis_client.hget(
        agent_key, "scientific_article"
    ).decode("utf-8")
    agent_info["description"] = redis_client.hget(agent_key, "description").decode(
        "utf-8"
    )
    return agent_info


def delete_agent(user_id, agent_name):
    # Формируем ключ для данных агента
    agent_key = f"user:{user_id}:agent:{agent_name}"
    # Удаляем данные агента из Redis
    redis_client.delete(agent_key)


def set_agent_for_user(user_id, agent_name):
    redis_client.set(user_id, agent_name)


def get_agent_for_user(user_id):
    agent_name = redis_client.get(user_id).decode("utf-8")
    return agent_name


def get_agent_names(user_id):
    agent_keys = redis_client.keys(f"user:{user_id}:agent:*")
    agent_names = []
    for key in agent_keys:
        _, _, agent_name = key.partition(b"user:")
        _, _, agent_name = agent_name.partition(b":agent:")
        agent_names.append(agent_name.decode("utf-8"))
    return agent_names
