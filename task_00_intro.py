import os
import logging

# Configure logger
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        logging.error("Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if template.strip() == "":
        logging.error("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if len(attendees) == 0:
        logging.info("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        personalized = template
        for field in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(field)
            if value is None:
                value = "N/A"
            personalized = personalized.replace("{" + field + "}", str(value))

        # Output file name
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(personalized)
            logging.info(f"Generated file: {filename}")
        except Exception as e:
            logging.error(f"Error writing file {filename}: {e}")

