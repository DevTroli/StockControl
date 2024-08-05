import csv

# Dados dos produtos com códigos de barras definidos como zero
def create_products_csv():
    with open("docs/produtosAdega.csv", "w", newline='') as f:
        csv_writer = csv.writer(f)
        
        # Cabeçalhos das colunas
        csv_writer.writerow(
            [
                "produto",
                "preco_custo",
                "preco_venda",
                "margem_venda",
                "estoque",
                "estoque_minimo",
                "codigo_de_barra",
                "categoria"
            ]
        )

        # Dados dos produtos com códigos de barras definidos como zero
        rows = [
            ["Flauta de bisel", 5.13, 12.0, 20, 3, 5, "00000000", "Instrumentos Musicais"],
            ["AGUA BUONA VITA 5L", 6.59, 12.0, 82.09, 22, 8, "00000000", "Águas"],
            ["BALLY MAÇÃ VERDE 2L", 7.49, 12.5, 66.89, 12, 8, "00000000", "Refrigerantes"],
            ["BALLY MORANGO & PÊSSEGO", 7.49, 12.5, 66.89, 13, 10, "00000000", "Refrigerantes"],
            ["MONSTER ULTRA WATERMELON 473ML", 7.39, 11.9, 61.03, 31, 6, "00000000", "Energéticos"],
            ["MONSTER ABSOLUT ZERO 473ML", 7.39, 11.9, 61.03, 29, 6, "00000000", "Energéticos"],
            ["MONSTER PACÍFIC PUNCH 473ML", 7.39, 11.9, 61.03, 26, 4, "00000000", "Energéticos"],
            ["GUARAVITON 500ML", 1.99, 4.0, 101.01, 32, 81, "00000000", "Refrigerantes"],
            ["BALLY MELANCIA 2L", 7.49, 12.5, 66.89, 11, 15, "00000000", "Refrigerantes"],
            ["SUCO PONCHITO MARACUJA 450ML", 1.79, 3.0, 67.6, 48, 12, "00000000", "Sucos"],
            ["SUCO MAGUARY GOIABA 1L", 4.79, 7.5, 56.58, 37, 3, "00000000", "Sucos"],
            ["SUCO MAGUARY ABACAXI 1L", 4.79, 7.5, 56.58, 38, 3, "00000000", "Sucos"],
            ["SUCO DEL VALLE LATA UVA 290ML", 3.29, 5.5, 67.17, 39, 6, "00000000", "Sucos"],
            ["SUCO DEL VALLE LATA GOIABA 290ML", 3.30, 5.5, 66.67, 41, 6, "00000000", "Sucos"],
            ["SUCO DEL VALLE LATA PESSÊGO 290ML", 3.30, 5.5, 66.67, 42, 6, "00000000", "Sucos"],
            ["SUCO DEL VALLE LATA LARANJA 290ML", 3.30, 5.5, 66.67, 40, 6, "00000000", "Sucos"],
            ["SUCO DEL VALLE LATA MARACUJÁ 290ML", 3.30, 5.5, 66.67, 43, 6, "00000000", "Sucos"],
            ["SUCO DEL VALLE FRUIT UVA 450ML", 2.89, 4.5, 55.71, 44, 5, "00000000", "Sucos"],
            ["SUCO DEL VALLE LARANJA 450ML", 2.89, 4.5, 55.71, 45, 6, "00000000", "Sucos"],
            ["VODKA PINACLE 1L", 0.0, 120.0, 0.0, 52, 1, "00000000", "Destilados"],
            ["VODKA WYBAROWA 1L", 0.0, 90.0, 0.0, 53, 2, "00000000", "Destilados"],
            ["VODKA ABSOLUT ELYX 750ML", 0.0, 215.0, 0.0, 54, 1, "00000000", "Destilados"],
            ["VODKA ABSOLUT CITRON 750ml", 0.0, 135.0, 0.0, 55, 1, "00000000", "Destilados"],
            ["VODKA ABSOLUT RASPBERRY 750ML", 0.0, 135.0, 0.0, 56, 1, "00000000", "Destilados"],
            ["VODKA ABSOLUT 1L", 0.0, 120.0, 0.0, 57, 2, "00000000", "Destilados"],
            ["VODKA SKYY 750ml", 0.0, 37.0, 0.0, 58, 2, "00000000", "Destilados"],
            ["VODKA BURLONE 950ML", 0.0, 50.0, 0.0, 59, 2, "00000000", "Destilados"],
            ["SUCO PONCHITO FRUTAS CITRICAS 450ML", 1.79, 3.0, 67.6, 46, 14, "00000000", "Sucos"],
            ["RED BULL MELANCIA 250ML", 7.29, 11.9, 63.24, 3, 16, "00000000", "Energéticos"],
            ["RED BULL TRADICIONAL 250ML", 6.89, 10.0, 45.14, 2, 16, "00000000", "Energéticos"],
            ["AGUA DE COCO 1L", 5.89, 8.9, 51.1, 33, 4, "00000000", "Águas"],
            ["RED BULL SUGAR FREE 250ML", 7.29, 11.9, 63.24, 5, 8, "00000000", "Energéticos"],
            ["GORDON'S GIN LONDON DRY", 0.0, 90.0, 0.0, 60, 2, "00000000", "Destilados"],
            ["RED BULL PITAYA 250ML", 7.29, 11.9, 63.24, 6, 16, "00000000", "Energéticos"],
            ["RED BULL MORANGO & PÊSSEGO 250ML", 7.29, 11.9, 63.24, 7, 21, "00000000", "Energéticos"],
            ["RED BULL TROPICAL 250ML", 7.29, 11.9, 63.24, 4, 24, "00000000", "Energéticos"],
            ["BALLY TRADICIONAL 2L", 7.49, 12.5, 66.89, 8, 11, "00000000", "Refrigerantes"],
            ["BALLY ABACAXI COM HORTELÃ 2L", 7.49, 12.5, 66.89, 9, 5, "00000000", "Refrigerantes"],
            ["SUCO PONCHITO LARANJA COM ACEROLA 450ML", 1.79, 3.0, 67.6, 47, 10, "00000000", "Sucos"],
            ["BALLY TROPICAL 2L", 7.49, 12.5, 66.89, 10, 8, "00000000", "Refrigerantes"],
            ["GATORADE BLUE BERRY", 5.19, 6.5, 25.24, 14, 5, "00000000", "Energéticos"],
            ["GATORADE UVA", 5.19, 6.5, 25.24, 15, 6, "00000000", "Energéticos"],
            ["GATORADE LARANJA", 5.19, 6.5, 25.24, 16, 6, "00000000", "Energéticos"],
            ["GATORADE MORANGO & MARACUJÁ", 5.19, 6.5, 25.24, 17, 6, "00000000", "Energéticos"],
            ["GATORADE LIMÃO", 5.19, 6.5, 25.24, 18, 6, "00000000", "Energéticos"],
            ["MONSTER TRADICIONAL 473ML", 6.99, 10.0, 43.06, 24, 7, "00000000", "Energéticos"],
            ["MONSTER ULTRA 473ML", 7.39, 11.9, 61.03, 25, 6, "00000000", "Energéticos"],
            ["MONSTER MANGO LOUCO 473ML", 7.39, 11.9, 61.03, 27, 3, "00000000", "Energéticos"],
            ["MONSTER PIPELINE PUNCH 473ML", 7.39, 11.9, 61.03, 30, 6, "00000000", "Energéticos"],
            ["COCA-COLA 350ML", 2.89, 4.5, 55.71, 49, 64, "00000000", "Refrigerantes"],
            ["VODKA CIROC REDBERRY 750ML", 0.0, 215.0, 0.0, 51, 1, "00000000", "Destilados"],
            ["AGUA BUONA VITA 500ml", 0.69, 2.0, 189.86, 20, 40, "00000000", "Águas"],
            ["AGUA FRESCCA 1,5L", 1.79, 3.5, 95.53, 19, 21, "00000000", "Águas"],
            ["AGUA COM GAS 510ML", 1.19, 2.5, 110.08, 21, 40, "00000000", "Águas"],
            ["AGUA TONICA ZERO 350ML", 3.0, 4.5, 50.0, 62, 6, "00000000", "Águas"],
            ["AGUA TONICA 350ml", 2.89, 4.0, 38.41, 23, 11, "00000000", "Águas"],
            ["GROSELHA G'NUTRE 900ML", 5.9, 9.0, 52.54, 34, 3, "00000000", "Bebidas Diversas"],
            ["SUCO MAGUARY MORANGO 1L", 4.79, 7.5, 56.58, 35, 4, "00000000", "Sucos"],
            ["SUCO MAGUARY UVA 1L", 4.79, 7.5, 56.58, 36, 3, "00000000", "Sucos"],
            ["VODKA CIROC 750ML", 0.0, 215.0, 0.0, 50, 1, "00000000", "Destilados"]
        ]
        
        # Escrever as linhas no arquivo CSV
        csv_writer.writerows(rows)

create_products_csv()
