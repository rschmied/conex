import connexion


def main():
    app = connexion.AioHttpApp(__name__, specification_dir="swagger/")
    app.add_api("openapi.yaml")
    app.run(port=8080)


if __name__ == "__main__":
    main()
