from datetime import datetime
from sentence_transformers import SentenceTransformer
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    device=device
)


def generate_embeddings(
    texts: list[str],
    batch_size: int,
):

    return model.encode(
        texts,
        batch_size=batch_size,
        normalize_embeddings=True,
        show_progress_bar=True,
    )



def prepare_embedding_row(
    price_item,
    variant,
    service_embedding,
    variant_embedding
):
    return {
        "price_item_aggregated_id": price_item["id"],
        "hospital_id": price_item["hospital_id"],
        "service_description": price_item["service_description"],
        "variant_service_desc": variant["variant_description"],
        "variant_id": variant["id"],
        "payer_id": price_item["payer_id"],
        "plan_id": price_item["plan_id"],
        "negotiated_rate": price_item["negotiated_rate"],
        "cash_price": price_item["cash_price"],
        "gross_charge": price_item["gross_charge"],
        "min_price": price_item["min_price"],
        "max_price": price_item["max_price"],
        "currency": price_item["currency"],
        "embedding": service_embedding,
        "variant_embedding": variant_embedding,
        "created_at": datetime.utcnow()
    }