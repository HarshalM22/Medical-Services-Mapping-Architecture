from sqlalchemy import  text
from etl_app.db import engine

class DBAdapter:
    def __init__(self):
        self.db = DBOperations()

    def load_price_items(self):
        return self.db.fetch_price_items()

    def load_procedure_variants(self):
        return self.db.fetch_procedure_variants()

    def save_embeddings(self, rows: list[dict]):
        return self.db.insert_mrf_service_embeddings(rows)
    def load_procedure_variants_with_embeddings(self):
        return self.db.fetch_procedure_variants_with_embeddings()

    def bulk_update_variant_embeddings(self, rows):
        return self.db.bulk_update_variant_embeddings(rows)
    

class DBOperations:
    def __init__(self):
        self.engine = engine

    # ============================================================
    # READ OPERATIONS
    # ============================================================

    def fetch_price_items(self):
        with self.engine.begin() as conn:
            return conn.execute(text("""
                SELECT
                    id as price_item_aggregated_id,
                    hospital_id,
                    service_code,
                    code_type,
                    service_description,
                    payer_id,
                    plan_id,
                    negotiated_rate,
                    cash_price,
                    gross_charge,
                    min_price,
                    max_price,
                    currency
                FROM price_items_aggregated
                WHERE hospital_id=3
            """)).mappings().all()

    def fetch_procedure_variants(self):
        with self.engine.begin() as conn:
            return conn.execute(text("""
                select v.id,v.variant_name,v.variant_description,v.diagnosis_codes, c.code,c.code_type,c.component_type,c.condition_rule,c.is_primary
                from procedure_variants as v
                left join procedure_components as c 
                on c.variant_id = v.id 
                where c.is_primary = 1 and c.code_type='CPT' 
            """)).mappings().all()

    # ============================================================
    # WRITE OPERATIONS
    # ============================================================

    def insert_mrf_service_embeddings(self, rows: list[dict]):
        if not rows:
            return 0

        with self.engine.begin() as conn:
            conn.execute(
                text("""
                INSERT INTO mrf_service_embeddings (
                    price_item_aggregated_id,
                    hospital_id,
                    service_description,
                    variant_service_desc,
                    variant_id,
                    payer_id,
                    plan_id,
                    negotiated_rate,
                    cash_price,
                    gross_charge,
                    min_price,
                    max_price,
                    currency,
                    embedding,
                    variant_embedding,
                    created_at
                )
                VALUES (
                    :price_item_aggregated_id,
                    :hospital_id,
                    :service_description,
                    :variant_service_desc,
                    :variant_id,
                    :payer_id,
                    :plan_id,
                    :negotiated_rate,
                    :cash_price,
                    :gross_charge,
                    :min_price,
                    :max_price,
                    :currency,
                    :embedding,
                    :variant_embedding,
                    :created_at
                )
                """),
                rows
            )
        return len(rows)
    
    def bulk_update_variant_embeddings(self, rows):
        if not rows:
            return 0

        with self.engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE procedure_variants
                    SET
                        embedding_json = :embedding_json,
                        embedding_dim = :embedding_dim,
                        embedding_model = :embedding_model,
                        embedding_updated_at = NOW()
                    WHERE id = :id
                """),
                rows
            )

        return len(rows)
    
    def fetch_procedure_variants_with_embeddings(self):
        with self.engine.begin() as conn:
            return conn.execute(text("""
                SELECT
                    id,
                    variant_name,
                    variant_description,
                    embedding_json,
                    embedding_model,
                    embedding_dim
                FROM procedure_variants
            """)).mappings().all()