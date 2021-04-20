from datetime import datetime

data = datetime.now()
minha_data = f"a data de hoje é {data}"
minha_data_formatada = f"a data formatada é {data:%d/%m/%y}"

print(minha_data)
print(minha_data_formatada)