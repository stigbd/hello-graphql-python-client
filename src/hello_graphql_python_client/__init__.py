from gql import Client, gql
from gql.transport.httpx import HTTPXTransport


transport = HTTPXTransport(url="http://localhost:8000/graphql")

# Using `async with` on the client will start a connection on the transport
# and provide a `session` variable to execute queries on this connection
client = Client(
    transport=transport,
    fetch_schema_from_transport=True,
)

# Create the books query
query_books = gql(
    """
    query {
        books {
            title
            author
            year
            publisher
        }
    }
"""
)

# Create the authors query
query_authors = gql(
    """
    query {
        authors {
            name
        }
    }
"""
)


def main() -> int:
    # Execute the queries
    result = client.execute(query_authors)
    print(f"Authors:\n{result}")
    result = client.execute(query_books)
    print(f"Books:\n{result}")

    return 0
