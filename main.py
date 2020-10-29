import server

PORT = 8000

if __name__ == "__main__":
    try:
        server.run(PORT)
    except KeyboardInterrupt:
        print("Stopping server on port ", PORT)