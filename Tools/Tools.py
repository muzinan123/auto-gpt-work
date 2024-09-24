import warnings

warnings.filterwarnings("ignore")

from langchain.tools import StructuredTool
from .FileQATool import ask_docment
from .WriterTool import write
from .EmailTool import send_email
from .ExcelTool import get_first_n_rows
from .FileTool import list_files_in_directory

document_qa_tool = StructuredTool.from_function(
    func=ask_document,
    name="AskDocument",
    description="Answer a question based on the content of a Word or PDF document. Consider contextual information and ensure complete definition of relevant concepts in the question.",
)

document_generation_tool = StructuredTool.from_function(
    func=write,
    name="GenerateDocument",
    description="Generate a formal document based on the requirement description",
)

email_tool = StructuredTool.from_function(
    func=send_email,
    name="SendEmail",
    description="Send an email to the specified email address. Ensure the email address is in the format xxx@xxx.xxx. Multiple email addresses should be separated by ';'.",
)

excel_inspection_tool = StructuredTool.from_function(
    func=get_first_n_rows,
    name="InspectExcel",
    description="Inspect the content and structure of an Excel file, displaying its column names and the first n rows, where n defaults to 3",
)

directory_inspection_tool = StructuredTool.from_function(
    func=list_files_in_directory,
    name="ListDirectory",
    description="Inspect the content and structure of a directory, displaying its file names and folder names",
)

finish_placeholder = StructuredTool.from_function(
    func=lambda: None,
    name="FINISH",
    description="A placeholder tool used to indicate task completion"
)
