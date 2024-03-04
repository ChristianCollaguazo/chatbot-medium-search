from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings


class SingletonBase(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBase, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class LoadData(metaclass=SingletonBase):
    def __init__(self, path="src/dataset/input_2.csv"):
        # Carga del data set
        self._path = path

        loader = CSVLoader(file_path=self._path, source_column="link")

        documents = loader.load()

        # Division en chunks y uso de un embeddings
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.split_documents(documents)
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2"
        )
        self._vector_db = FAISS.from_documents(docs, embeddings)

    @property
    def vector_db(self):
        return self._vector_db

    def similarity_search(self, query):
        docs = self.vector_db.similarity_search(query)
        return docs
