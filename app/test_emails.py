import pandas as pd

class TestEmails:
    def __init__(self):
        self.df = pd.read_csv('/data/test_emails.csv')

    def get_all(self):
        return {k: v
                for k, v in
                zip(
                    self.df.title.tolist(),
                    self.df.email.tolist(),
                )
            }
