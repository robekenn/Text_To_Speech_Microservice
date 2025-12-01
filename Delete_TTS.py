import os

def delete(filename="output.wav"):
    """
    Delete the generated WAV file safely.
    Returns 'OK' if deleted, otherwise an error message.
    """
    if not os.path.exists(filename):
        return "File not found"

    try:
        os.remove(filename)
        return "OK"
    except Exception as e:
        return f"Error: {str(e)}"