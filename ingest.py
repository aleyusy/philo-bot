# ingest.py
import os
import chromadb
from sentence_transformers import SentenceTransformer

# Загружаем модель для эмбеддингов
print("Загружаем модель эмбеддингов...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Инициализируем Chroma
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="philosophy")

# Папка с текстами
DATA_PATH = "data"

def load_texts():
    texts = []
    for filename in os.listdir(DATA_PATH):
        filepath = os.path.join(DATA_PATH, filename)
        if filename.endswith(".txt"):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                # Разбиваем на абзацы
                chunks = [chunk.strip() for chunk in content.split("\n\n") if len(chunk.strip()) > 20]
                texts.extend(chunks)
    return texts

def ingest():
    texts = load_texts()
    print(f"Найдено {len(texts)} чанков. Начинаем индексацию...")

    # Генерируем эмбеддинги
    embeddings = model.encode(texts).tolist()

    # Сохраняем в Chroma
    collection.add(
        embeddings=embeddings,
        documents=texts,
        ids=[f"doc_{i}" for i in range(len(texts))]
    )

    print("✅ Данные успешно загружены в векторную базу!")

if __name__ == "__main__":
    ingest()