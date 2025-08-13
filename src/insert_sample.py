from sqlalchemy.orm import Session
from models import Document
from database import SessionLocal

db: Session = SessionLocal()

try:
    # Create a new document object
    new_document = Document(
        title="Sample Document Title",
        content="This is a test document content.",
        summary="This is a summary of the test document."
    )

    # Add and commit the new document to the database
    db.add(new_document)
    db.commit()  # Commit the transaction

    # Query the database to check if the document was added
    document = db.query(Document).filter(Document.title == "Sample Document Title").first()

    if document:
        print(f"Document added: {document}")
    else:
        print("No document found.")

except Exception as e:
    print(f"An error occurred: {e}")
    db.rollback()  # Rollback the transaction if there's an error

finally:
    db.close() 
