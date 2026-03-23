from src.background_subtraction import AppConfig, run_application


def main() -> None:
    config = AppConfig()
    run_application(config)


if __name__ == "__main__":
    main()
