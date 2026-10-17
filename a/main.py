from pathlib import Path
from docling.document_converter import DocumentConverter

project_path = Path(__file__).parent.parent
pdf_path = project_path / "resource/pdf"
text_path = project_path / "resource/text"

text_path.mkdir(parents=True, exist_ok=True)


def save_markdown(
        converter: DocumentConverter,
        src_path: Path,
        out_path: Path,
):
    doc = converter.convert(src_path).document
    with out_path.open("w", encoding="utf-8") as f:
        f.write(doc.export_to_markdown())

converter = DocumentConverter()

save_markdown(
    converter,
    pdf_path/"sj_sutk.pdf",
    text_path/"sj_sutk.md"
)

# source = "https://arxiv.org/pdf/2408.09869"  # file path or URL
# converter = DocumentConverter()
# doc = converter.convert(source).document

# print(doc.export_to_markdown())  # output: "### Docling Technical Report[...]"