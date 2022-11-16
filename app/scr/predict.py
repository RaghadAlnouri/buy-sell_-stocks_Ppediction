from model import predict_tabular_classification_sample


def predict(ticker: str) -> str:
    return predict_tabular_classification_sample(
        project="571677384943",
        endpoint_id="3280243407888318464",
        location="us-central1",
        instances=[{"formatted_date": "2022-11-16",
                "high": "116.80999755859376",
                "low":"113.2300033569336",
                "open":"115.0",
                "close":"115.01000213623048",
                "volume":"2081600.0",
                "ticker":ticker }]           
    )