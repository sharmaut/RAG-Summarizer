from transformers import pipeline

def summarize_text(text, max_length=150):
    """
    Summarizes the given text using a pre-trained transformer model.
    """
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]["summary_text"]

if __name__ == "__main__":
    # Example text for testing
    sample_text = (
        "COVID-19 is an infectious disease caused by the SARS-CoV-2 virus. Most people who fall sick with COVID-19 will experience "
        "mild to moderate symptoms and recover without special treatment. However, some will become seriously ill and require medical attention. "
        "Older people and those with underlying medical conditions are at higher risk of developing severe disease. Prevention includes vaccinations, "
        "wearing masks, and maintaining social distancing."
    )
    
    summary = summarize_text(sample_text)
    print("Summary:", summary)
