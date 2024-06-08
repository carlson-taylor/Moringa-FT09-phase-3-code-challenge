from database.setup import create_tables
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def main():
    try:
        # Create tables
        create_tables()
        print("Tables created successfully.")
        
        # Create an author
        author1 = Author(name="John Doe")
        print(f"Author created: ID={author1.id}, Name={author1.name}")

        # Create a magazine
        magazine1 = Magazine(name="Tech Weekly", category="Technology")
        print(f"Magazine created: ID={magazine1.id}, Name={magazine1.name}, Category={magazine1.category}")

        # Create an article
        article1 = Article(title="AI in 2024", content="Content about AI advancements in 2024", author=author1, magazine=magazine1)
        print(f"Article created: ID={article1.id}, Title={article1.title}, Author={article1.author.name}, Magazine={article1.magazine.name}")

        # Print additional information
        print("Author's Articles:", author1.articles())
        print("Author's Magazines:", author1.magazines())
        print("Magazine's Articles:", magazine1.articles())
        print("Magazine's Contributors:", magazine1.contributors())
        print("Magazine's Article Titles:", magazine1.article_titles())
        print("Magazine's Contributing Authors:", magazine1.contributing_authors())

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
