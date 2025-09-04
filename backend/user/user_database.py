import sqlite3
import json
from backend.user.user_class import User   # Importing the User class
#from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
import textwrap


class UserDatabase:
    def __init__(self, db_name="users.db"):
        # Initialize database connection
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create the users table if it doesn't already exist"""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            userID TEXT PRIMARY KEY,
            username TEXT,
            semantic_domains TEXT,
            data JSON
        )
        """)
        self.conn.commit()

    # ---------------- Save / Update ----------------
    def save_user(self, user_obj: User):
        """
        Save a new user to the database. 
        If the userID already exists, update the existing row.
        """
        data = {
            "vocabulary_categories": user_obj.get_vocabulary_categories(),
            "weak_vocabulary_categories": user_obj.get_weak_vocabulary_categories(),
            "suggested_vocabulary_categories": user_obj.get_suggested_vocabulary_categories(),
            "weak_words": user_obj.get_weak_words(),
            "learned_grammar": user_obj.get_learned_grammar(),
            "next_grammar": user_obj.get_next_grammar(),
            "weak_grammar": user_obj.get_weak_grammar(),
            "unlearned_needed_grammar": user_obj.get_unlearned_needed_grammar(),     
            "reading_settings": user_obj.reading_settings.get_user_reading_settings(),
            "listening_settings": user_obj.listening_settings.get_user_listening_settings(),
            "writing_settings": user_obj.writing_settings.get_user_writing_settings(),
            "conversation_settings": user_obj.conversation_settings.get_user_conversation_settings(),
            "vocabulary_settings": user_obj.vocabulary_settings.get_user_vocab_learning_settings(),
            "grammar_settings": user_obj.grammar_settings.get_user_grammar_learning_settings(),    
        }

        self.cursor.execute("""
        INSERT INTO users (userID, username, semantic_domains, data)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(userID) DO UPDATE SET
            username=excluded.username,
            semantic_domains=excluded.semantic_domains,
            data=excluded.data
        """, (
            user_obj.get_userID(),
            user_obj.get_username(),
            json.dumps(user_obj.get_semantic_domains()),
            json.dumps(data)
        ))
        self.conn.commit()

    # ---------------- Load ----------------
    def load_user(self, userID: str) -> User | None:
        """
        Load a user from the database by userID.
        Returns a User object if found, otherwise None.
        """
        self.cursor.execute("SELECT * FROM users WHERE userID=?", (userID,))
        row = self.cursor.fetchone()
        if row:
            username = row[1]
            semantic_domains = json.loads(row[2])
            user_data = json.loads(row[3])

            # Create User object
            user = User(username, userID, semantic_domains)

            # Restore saved attributes into the User object
            user._User__vocabulary_categories = user_data.get("vocabulary_categories", {})
            user._User__weak_vocabulary_categories = user_data.get("weak_vocabulary_categories", [])
            user._User__suggested_vocabulary_categories = user_data.get("suggested_vocabulary_categories", [])
            user._User__weak_words = user_data.get("weak_words", [])

            user._User__learned_grammar = user_data.get("learned_grammar", {})
            user._User__next_grammar = user_data.get("next_grammar", {})
            user._User__weak_grammar = user_data.get("weak_grammar", {})
            user._User__unlearned_needed_grammar = user_data.get("unlearned_needed_grammar", {})

            # ---------------- Restore practice settings ----------------
        
            user.reading_settings.set_user_reading_settings(user_data["reading_settings"])      
            user.listening_settings.set_user_listening_settings(user_data["listening_settings"])       
            user.writing_settings.set_user_writing_settings(user_data["writing_settings"])       
            user.conversation_settings.set_user_conversation_settings(user_data["conversation_settings"])        
            user.vocabulary_settings.set_user_vocab_learning_settings(user_data["vocabulary_settings"])        
            user.grammar_settings.set_user_grammar_learning_settings(user_data["grammar_settings"])

            return user
        return None

    def close(self):
        """Close the database connection"""
        self.conn.close()

    # ---------------- Delete a single user ----------------
    def delete_user(self, userID: str):
        """Delete a user from the database by userID."""
        self.cursor.execute("DELETE FROM users WHERE userID=?", (userID,))
        self.conn.commit()

    # ---------------- Clear all users ----------------
    def clear_database(self):
        """Delete all users and their data from the database."""
        self.cursor.execute("DELETE FROM users")
        self.conn.commit()

    # ---------------- Show users ----------------
    def list_users(self) -> dict:
        """
        Return all users as a dictionary {userID: username}.
        """
        self.cursor.execute("SELECT userID, username FROM users")
        rows = self.cursor.fetchall()
        return {user_id: username for user_id, username in rows}    