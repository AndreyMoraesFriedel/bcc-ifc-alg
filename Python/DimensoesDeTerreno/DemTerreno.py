# Inicio

# Obter Largura do Terreno (lar_terreno)
lar_terreno = int(input())
# Obter Altura do Terreno (alt_terreno)
alt_terreno = int(input())

# Calcular a Area do Terreno (area_terreno = lar_terreno * alt_terreno)
area_terreno = lar_terreno * alt_terreno

# Obter Largura da Casa (lar_casa)
lar_casa = int(input())
# Obter Altura da Casa (alt_casa)
alt_casa = int(input())

# Calcular a Area da Casa (area_casa = lar_casa * alt_casa)
area_casa = lar_casa * alt_casa

# Calcular Area Livre em metros quadrados (area_livre_mq = area_terreno - area_casa)
area_livre_mq = area_terreno - area_casa

# Calcular Area Livre em porcentagem (area_livre_pc = 100 - ((area_casa * 100) / area_terreno))
area_livre_pc = 100 - ((area_casa * 100) / area_terreno)

# Mostrar total da area livre em metros quadrados e em porcentagem
print(f"""
      Area Livre do Terreno: 
        Em metros quadrados: {area_livre_mq};
        Em porcentagem: {area_livre_pc}
        """)

# Fim