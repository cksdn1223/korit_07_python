from prettytable import PrettyTable
from prettytable import TableStyle

from pokemon_data import pokemon_data
table = PrettyTable()
table.field_names = ["번호", "이름", "타입"]
for pokemon in pokemon_data:
    table.add_row(pokemon)
# table.add_rows(pokemon_data)
print(table)

# # 표에 padding 주는거
# table.padding_width=4
# # 표 스타일 정해주는거 TableStyle 도 import 해야함
# table.set_style(TableStyle.DOUBLE_BORDER)
# # 테이블 이름이랑 자동 번호 설정해줌 1부터
# table.add_autoindex("번호")
# # 테이블을 각종 format 으로 문자열로 뽑아줌
# print(table.get_formatted_string(out_format="html"))

# pokemon_num = []
# pokemon_name = []
# pokemon_type = []
# for pokemon in pokemon_data:
#     pokemon_num.append(pokemon[0])
#     pokemon_name.append(pokemon[1])
#     pokemon_type.append(pokemon[2])
# table.add_column("번호",pokemon_num,"c","t")
# table.add_column("이름",pokemon_name,"c","t")
# table.add_column("타입",pokemon_type,"c","t")

