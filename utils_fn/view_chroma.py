import argparse
import chromadb
import pandas as pd 
import streamlit as st


parser = argparse.ArgumentParser(description='Set the Chroma DB path to view collections')
parser.add_argument('db')

def view_chroma_collections(db_dir):
    st.markdown(f"### DB Path: {db_dir}")

    client = chromadb.PersistentClient(path=db_dir)

    st.header("Collections")

    for collection in client.list_collections():
        data = collection.get(include=["documents", "metadatas", "embeddings"])
        
        data_dict = {
            "id": data["ids"],
            "text": data["documents"],
            "metadata": data["metadatas"],
            "embedding": data["embeddings"]
        }

        df = pd.DataFrame.from_dict(data_dict)
        st.markdown(f"### Collection: **{collection.name}**")
        st.dataframe(df)


if __name__ == "__main__":
    args = parser.parse_args()
    print(f"Opening database: {args.db}")
    view_chroma_collections(args.db)
