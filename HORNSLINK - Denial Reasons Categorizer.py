import re

# Define simple categorization rules based on keywords
def categorize_comment(comment):
    reasons = []
    if re.search(r"membership|roster", comment, re.IGNORECASE):
        reasons.append("Roster Issue")
    if re.search(r"constitution|compliance|hazing|elections|amendments", comment, re.IGNORECASE):
        reasons.append("Constitution Missing")
    if re.search(r"trademark|hook|horns|tower|UT\b|Texas", comment, re.IGNORECASE):
        reasons.append("Trademark Violation")
    return reasons if reasons else ["Other"]

# Apply categorization
df["ReasonsList"] = df["Comment"].apply(categorize_comment)

# Convert for exporting dataset to SQL
sql_ready = df[["Submissionid", "ReasonsList"]].explode("ReasonsList")
sql_ready = sql_ready.rename(columns={"ReasonsList": "Reason"})

# Show preview
import caas_jupyter_tools
caas_jupyter_tools.display_dataframe_to_user("SQL-Ready Denial Reasons", sql_ready.head(20))