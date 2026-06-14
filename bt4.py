import logging

logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active"
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active"
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched"
    }
]


def calculate_actual_pay(player):
    """
    Tính lương thực nhận.

    Args:
        player (dict)

    Returns:
        float
    """
    if player.get("status") == "Benched":
        return player["salary"] * 0.5

    return player["salary"]


def display_roster(roster_list):
    """
    Hiển thị đội hình.
    """
    logging.info("Coach viewed the team roster.")

    if not roster_list:
        print("Đội hình hiện đang trống.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")

    for player in roster_list:

        status = player.get("status", "Unknown")

        name = player["name"]

        if status == "Benched":
            name += " [DỰ BỊ]"

        print(
            f"{player['player_id']} | "
            f"{name} | "
            f"{player['role']} | "
            f"{player['salary']} | "
            f"{status}"
        )


def sign_player(roster_list):
    """
    Chiêu mộ tuyển thủ.
    """
    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    for player in roster_list:
        if player["player_id"] == player_id:
            print(
                f"Lỗi: Mã tuyển thủ {player_id} đã tồn tại."
            )

            logging.warning(
                f"Failed to sign player - Duplicate player ID {player_id}"
            )
            return

    name = input(
        "Nhập tên tuyển thủ: "
    ).strip().title()

    role = input(
        "Nhập vị trí thi đấu: "
    ).strip().title()

    while True:

        try:
            salary = float(
                input(
                    "Nhập mức lương hàng tháng: "
                )
            )

            if salary <= 0:
                print(
                    "Lương phải là số dương. Vui lòng nhập lại."
                )
                continue

            break

        except ValueError:

            print(
                "Lương phải là số. Vui lòng nhập lại."
            )

            logging.warning(
                "Failed to sign player - Invalid salary input"
            )

    roster_list.append(
        {
            "player_id": player_id,
            "name": name,
            "role": role,
            "salary": salary,
            "status": "Active"
        }
    )

    logging.info(
        f"Signed new player {name} with salary {salary}"
    )

    print(
        f"Thành công: Đã chiêu mộ tuyển thủ {name}."
    )


def update_player_status(roster_list):
    """
    Cập nhật lương hoặc trạng thái.
    """
    player_id = input(
        "Nhập mã tuyển thủ cần cập nhật: "
    ).strip().upper()

    player = next(
        (
            item
            for item in roster_list
            if item["player_id"] == player_id
        ),
        None
    )

    if player is None:

        print(
            f"Không tìm thấy tuyển thủ mang mã {player_id}."
        )

        logging.warning(
            f"Failed to update player - Player ID {player_id} not found"
        )
        return

    print("1. Cập nhật lương")
    print("2. Cập nhật trạng thái")

    choice = input(
        "Chọn chức năng cập nhật (1-2): "
    )

    if choice == "1":

        while True:

            try:
                new_salary = float(
                    input(
                        "Nhập mức lương mới: "
                    )
                )

                if new_salary <= 0:
                    print(
                        "Lương phải là số dương."
                    )
                    continue

                old_salary = player["salary"]

                player["salary"] = new_salary

                logging.info(
                    f"Updated player {player_id} salary "
                    f"from {old_salary} to {new_salary}"
                )

                print(
                    f"Thành công: Đã cập nhật lương cho tuyển thủ {player_id}."
                )

                break

            except ValueError:
                print(
                    "Lương phải là số."
                )

    elif choice == "2":

        print("1. Active")
        print("2. Benched")

        status_choice = input(
            "Nhập lựa chọn trạng thái (1-2): "
        )

        if status_choice == "1":
            player["status"] = "Active"

        elif status_choice == "2":
            player["status"] = "Benched"

        logging.info(
            f"Updated player {player_id} status to {player['status']}"
        )

        print(
            f"Thành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}."
        )


def generate_payroll_report(roster_list):
    """
    Báo cáo quỹ lương.
    """
    print(
        "\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---"
    )

    if not roster_list:
        print(
            "Đội hình hiện đang trống. Tổng quỹ lương: 0.0"
        )
        return

    total_payroll = 0.0

    try:

        for player in roster_list:

            actual_pay = calculate_actual_pay(
                player
            )

            total_payroll += actual_pay

            print(
                f"{player['player_id']} | "
                f"{player['name']} | "
                f"{player['status']} | "
                f"{player['salary']} | "
                f"{actual_pay}"
            )

    except KeyError as error:

        print(
            "Lỗi: Một tuyển thủ đang bị thiếu dữ liệu."
        )

        logging.error(
            f"Missing key while generating payroll report: {error}"
        )

        total_payroll = 0.0

    print("-" * 80)

    print(
        f"Tổng quỹ lương hàng tháng: {total_payroll}"
    )

    logging.info(
        f"Generated monthly payroll report. Total: {total_payroll}"
    )
