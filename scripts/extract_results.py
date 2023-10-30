import os

heuristic = "heuristic3"

def extract_values_from_file(file_path):
    """
    Abre o arquivo, extrai os valores de interesse e os retorna.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Encontrar a linha que contém 'Bitrate'
        for idx, line in enumerate(lines):
            if "Bitrate" in line:
                data_line = lines[idx + 1].split()
                bitrate = data_line[2]
                y_psnr = data_line[3]
                y_wspsnr = data_line[7]
                return bitrate, y_psnr, y_wspsnr
    return None, None, None

def main():
    base_path = f"C:\\Users\\otavi\\OneDrive\\Ambiente de Trabalho\\TCC\\VTM360-19.0_Lib13.4_ResultsTCC\\{heuristic}"
    names = ["ChairliftRide", "Gaslamp", "Harbor", "KiteFlite", "SkateboardInLot", "SkateboardTrick", "Train", "Trolley"]
    qps = [22, 27, 32, 37]

    # Arquivo de saída
    output_file = f"output_{heuristic}.txt"
    with open(output_file, 'w') as out_file:
        for name in names:
            for qp in qps:
                dir_path = os.path.join(base_path, name, str(qp))
                file_path = os.path.join(dir_path, "VTM-ISPnoVerticalModes.txt")
                if os.path.exists(file_path):
                    bitrate, y_psnr, y_wspsnr = extract_values_from_file(file_path)
                    if bitrate and y_psnr and y_wspsnr:
                        # Escrever no arquivo de saída
                        out_file.write(f"{bitrate}, {y_psnr}, {y_wspsnr}\n")
                else:
                    print(f"Arquivo {file_path} não encontrado!")

if __name__ == "__main__":
    main()
