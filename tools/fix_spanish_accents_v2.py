"""
Normalize Spanish accents across all es.json values.
Efficient single-pass approach using compiled alternation regex.
"""
import json
import re
import time

with open('Localization/es.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# === ALL WORD REPLACEMENTS (lowercase -> accented) ===
word_map = {}

# ñ words
word_map.update({
    'ano': 'año', 'anos': 'años', 'dano': 'daño', 'danos': 'daños',
    'companero': 'compañero', 'companeros': 'compañeros',
    'companera': 'compañera', 'companeras': 'compañeras',
    'montana': 'montaña', 'montanas': 'montañas',
    'espanol': 'español', 'espanola': 'española',
    'manana': 'mañana', 'mananas': 'mañanas',
    'enganar': 'engañar', 'engano': 'engaño',
    'pequeno': 'pequeño', 'pequena': 'pequeña',
    'pequenos': 'pequeños', 'pequenas': 'pequeñas',
    'senor': 'señor', 'senora': 'señora',
    'senores': 'señores', 'senoras': 'señoras',
    'sueno': 'sueño', 'suenos': 'sueños',
    'ensenanza': 'enseñanza', 'ensenar': 'enseñar', 'ensena': 'enseña',
    'nino': 'niño', 'nina': 'niña', 'ninos': 'niños', 'ninas': 'niñas',
    'banarse': 'bañarse', 'bano': 'baño',
    'punalada': 'puñalada', 'puno': 'puño', 'punos': 'puños',
    'lena': 'leña', 'canon': 'cañón', 'castano': 'castaño',
    'arana': 'araña', 'aranas': 'arañas', 'carino': 'cariño',
    'extrano': 'extraño', 'extrana': 'extraña',
    'extranos': 'extraños', 'extranas': 'extrañas',
    'empunar': 'empuñar', 'vinedo': 'viñedo', 'otono': 'otoño',
    'panuelo': 'pañuelo', 'cabana': 'cabaña',
    'hazana': 'hazaña', 'hazanas': 'hazañas',
    'compania': 'compañía',
})

# Common adverbs/conjunctions/always-accented words
word_map.update({
    'tambien': 'también',
    'aqui': 'aquí',
    'asi': 'así',
    'despues': 'después',
    'ademas': 'además',
    'detras': 'detrás',
    'jamas': 'jamás',
    'quiza': 'quizá', 'quizas': 'quizás',
    'atras': 'atrás',
    'dificil': 'difícil', 'dificiles': 'difíciles',
    'facil': 'fácil', 'faciles': 'fáciles',
    'util': 'útil', 'utiles': 'útiles',
    'inutil': 'inútil',
    'debil': 'débil', 'debiles': 'débiles',
    'rapido': 'rápido', 'rapida': 'rápida',
    'rapidos': 'rápidos', 'rapidas': 'rápidas',
    'rapidamente': 'rápidamente',
    'unico': 'único', 'unica': 'única',
    'unicos': 'únicos', 'unicas': 'únicas',
    'ultimo': 'último', 'ultima': 'última',
    'ultimos': 'últimos', 'ultimas': 'últimas',
    'publico': 'público', 'publica': 'pública',
    'musica': 'música',
    'magico': 'mágico', 'magica': 'mágica',
    'magicos': 'mágicos', 'magicas': 'mágicas',
    'tragico': 'trágico', 'tragica': 'trágica',
    'clasico': 'clásico', 'clasica': 'clásica',
    'mitico': 'mítico', 'mitica': 'mítica',
    'mistico': 'místico', 'mistica': 'mística',
    'historico': 'histórico', 'historica': 'histórica',
    'espiritu': 'espíritu', 'espiritus': 'espíritus',
    'capitulo': 'capítulo', 'capitulos': 'capítulos',
    'circulo': 'círculo', 'circulos': 'círculos',
    'simbolo': 'símbolo', 'simbolos': 'símbolos',
    'proposito': 'propósito',
    'ejercito': 'ejército', 'ejercitos': 'ejércitos',
    'numero': 'número', 'numeros': 'números',
    'pagina': 'página', 'paginas': 'páginas',
    'victima': 'víctima', 'victimas': 'víctimas',
    'angel': 'ángel', 'angeles': 'ángeles',
    'arbol': 'árbol', 'arboles': 'árboles',
    'carcel': 'cárcel',
    'cesped': 'césped',
})

# Past tenses -ó
word_map.update({
    'perdio': 'perdió', 'murio': 'murió', 'cayo': 'cayó',
    'huyo': 'huyó', 'recibio': 'recibió', 'encontro': 'encontró',
    'alcanzo': 'alcanzó', 'destruyo': 'destruyó',
    'descubrio': 'descubrió', 'convirtio': 'convirtió',
    'decidio': 'decidió', 'consiguio': 'consiguió',
    'cumplio': 'cumplió', 'ofrecio': 'ofreció',
    'prometio': 'prometió', 'resistio': 'resistió',
    'sobrevivio': 'sobrevivió', 'sucedio': 'sucedió',
    'traiciono': 'traicionó', 'derroto': 'derrotó',
    'desperto': 'despertó', 'escapo': 'escapó',
    'gano': 'ganó', 'llego': 'llegó',
    'regreso': 'regresó', 'salvo': 'salvó',
    'supero': 'superó', 'volvio': 'volvió',
})

# First person past -é
word_map.update({
    'encontre': 'encontré', 'llegue': 'llegué', 'busque': 'busqué',
})

# -ción/-sión nouns (individual words, suffix rule handles the rest)
word_map.update({
    'corazon': 'corazón', 'razon': 'razón',
    'cancion': 'canción', 'mision': 'misión',
    'decision': 'decisión', 'traicion': 'traición',
    'prision': 'prisión', 'explosion': 'explosión',
    'ilusion': 'ilusión', 'bendicion': 'bendición',
    'maldicion': 'maldición', 'pocion': 'poción',
    'cuestion': 'cuestión', 'religion': 'religión',
    'region': 'región', 'habitacion': 'habitación',
    'posicion': 'posición', 'informacion': 'información',
    'direccion': 'dirección', 'proteccion': 'protección',
    'destruccion': 'destrucción', 'construccion': 'construcción',
    'condicion': 'condición', 'reputacion': 'reputación',
    'resurreccion': 'resurrección', 'creacion': 'creación',
    'puntuacion': 'puntuación', 'salvacion': 'salvación',
    'negociacion': 'negociación', 'confrontacion': 'confrontación',
    'aceptacion': 'aceptación', 'separacion': 'separación',
    'liberacion': 'liberación', 'bonificacion': 'bonificación',
    'clasificacion': 'clasificación', 'combinacion': 'combinación',
    'comparacion': 'comparación', 'comunicacion': 'comunicación',
    'concentracion': 'concentración', 'configuracion': 'configuración',
    'continuacion': 'continuación', 'contribucion': 'contribución',
    'conversacion': 'conversación', 'curacion': 'curación',
    'dedicacion': 'dedicación', 'definicion': 'definición',
    'descripcion': 'descripción', 'desaparicion': 'desaparición',
    'educacion': 'educación', 'elevacion': 'elevación',
    'eliminacion': 'eliminación', 'emocion': 'emoción',
    'encarnacion': 'encarnación', 'excepcion': 'excepción',
    'explicacion': 'explicación', 'generacion': 'generación',
    'identificacion': 'identificación', 'imaginacion': 'imaginación',
    'instalacion': 'instalación', 'interaccion': 'interacción',
    'investigacion': 'investigación', 'invocacion': 'invocación',
    'justificacion': 'justificación', 'legislacion': 'legislación',
    'localizacion': 'localización', 'meditacion': 'meditación',
    'modificacion': 'modificación', 'motivacion': 'motivación',
    'navegacion': 'navegación', 'obligacion': 'obligación',
    'observacion': 'observación', 'operacion': 'operación',
    'organizacion': 'organización', 'orientacion': 'orientación',
    'percepcion': 'percepción', 'poblacion': 'población',
    'preparacion': 'preparación', 'presentacion': 'presentación',
    'produccion': 'producción', 'profesion': 'profesión',
    'programacion': 'programación', 'proporcion': 'proporción',
    'reaccion': 'reacción', 'realizacion': 'realización',
    'recepcion': 'recepción', 'recomendacion': 'recomendación',
    'recuperacion': 'recuperación', 'reduccion': 'reducción',
    'relacion': 'relación', 'renovacion': 'renovación',
    'repeticion': 'repetición', 'representacion': 'representación',
    'restauracion': 'restauración', 'restriccion': 'restricción',
    'revelacion': 'revelación', 'revolucion': 'revolución',
    'sancion': 'sanción', 'satisfaccion': 'satisfacción',
    'seleccion': 'selección', 'sensacion': 'sensación',
    'situacion': 'situación', 'solucion': 'solución',
    'tentacion': 'tentación', 'tradicion': 'tradición',
    'transaccion': 'transacción', 'transformacion': 'transformación',
    'ubicacion': 'ubicación', 'version': 'versión',
    'violacion': 'violación', 'vocacion': 'vocación',
})

# -ía words
word_map.update({
    'energia': 'energía', 'categoria': 'categoría',
    'filosofia': 'filosofía', 'valentia': 'valentía',
    'sabiduria': 'sabiduría', 'armonia': 'armonía',
    'melodia': 'melodía', 'garantia': 'garantía',
    'fantasia': 'fantasía', 'herejia': 'herejía',
    'alegria': 'alegría', 'agonia': 'agonía', 'ironia': 'ironía',
})

# Adjectives
word_map.update({
    'fertil': 'fértil', 'esteril': 'estéril', 'fragil': 'frágil',
    'movil': 'móvil', 'habil': 'hábil', 'volatil': 'volátil',
    'automatico': 'automático', 'automatica': 'automática',
    'economico': 'económico', 'economica': 'económica',
    'fisico': 'físico', 'fisica': 'física',
    'quimico': 'químico', 'quimica': 'química',
    'tecnico': 'técnico', 'tecnica': 'técnica',
    'politico': 'político', 'politica': 'política',
    'critico': 'crítico', 'critica': 'crítica',
    'practico': 'práctico', 'practica': 'práctica',
    'logico': 'lógico', 'logica': 'lógica',
    'basico': 'básico', 'basica': 'básica',
    'comico': 'cómico', 'comica': 'cómica',
    'cosmico': 'cósmico', 'cosmica': 'cósmica',
    'demoniaco': 'demoníaco', 'demoniaca': 'demoníaca',
    'diabolico': 'diabólico', 'diabolica': 'diabólica',
    'dinamico': 'dinámico', 'dinamica': 'dinámica',
    'electrico': 'eléctrico', 'electrica': 'eléctrica',
    'epico': 'épico', 'epica': 'épica',
    'exotico': 'exótico', 'exotica': 'exótica',
    'fantastico': 'fantástico', 'fantastica': 'fantástica',
    'genetico': 'genético', 'genetica': 'genética',
    'geografico': 'geográfico', 'geografica': 'geográfica',
    'maximo': 'máximo', 'maxima': 'máxima',
    'minimo': 'mínimo', 'minima': 'mínima',
    'optimo': 'óptimo', 'optima': 'óptima',
    'pacifico': 'pacífico', 'pacifica': 'pacífica',
    'romantico': 'romántico', 'romantica': 'romántica',
    'sarcastico': 'sarcástico', 'sarcastica': 'sarcástica',
    'satirico': 'satírico', 'satirica': 'satírica',
    'simpatico': 'simpático', 'simpatica': 'simpática',
})

# Conditional verb forms -ía
word_map.update({
    'podria': 'podría', 'podrias': 'podrías',
    'tendria': 'tendría', 'tendrias': 'tendrías',
    'deberia': 'debería', 'deberias': 'deberías',
    'haria': 'haría', 'harias': 'harías',
    'vendria': 'vendría', 'diria': 'diría',
    'sabria': 'sabría', 'querria': 'querría',
    'estaria': 'estaría', 'daria': 'daría',
    'iria': 'iría', 'pondria': 'pondría',
    'saldria': 'saldría', 'habria': 'habría',
    'valdria': 'valdría',
})

# Words with ú (esdrújulas)
word_map.update({
    'musculo': 'músculo', 'musculos': 'músculos',
    'obstaculo': 'obstáculo', 'obstaculos': 'obstáculos',
    'vehiculo': 'vehículo',
    'articulo': 'artículo', 'articulos': 'artículos',
    'calculo': 'cálculo', 'catalogo': 'catálogo',
    'curriculo': 'currículo', 'estimulo': 'estímulo',
    'pendulo': 'péndulo', 'titulo': 'título', 'titulos': 'títulos',
    'vinculo': 'vínculo', 'brujula': 'brújula',
    'formula': 'fórmula', 'formulas': 'fórmulas',
    'clausula': 'cláusula', 'celula': 'célula', 'celulas': 'células',
    'capsula': 'cápsula',
})

# -ón words
word_map.update({
    'dragon': 'dragón', 'campeon': 'campeón',
    'patron': 'patrón', 'ladron': 'ladrón',
    'limon': 'limón', 'jabon': 'jabón', 'rincon': 'rincón',
    'salon': 'salón', 'baston': 'bastón', 'marron': 'marrón',
    'boton': 'botón', 'cajon': 'cajón',
    'escalon': 'escalón', 'melon': 'melón',
    'monton': 'montón', 'peaton': 'peatón',
    'perdon': 'perdón', 'sermon': 'sermón',
    'tiburon': 'tiburón', 'varon': 'varón',
})

# -és words
word_map.update({
    'ingles': 'inglés', 'interes': 'interés',
    'marques': 'marqués', 'traves': 'través', 'cortes': 'cortés',
})

# "mas" -> "más" (very common, "mas" as "but" is archaic/literary)
word_map['mas'] = 'más'

# Remove identity mappings and already-accented words
word_map = {k: v for k, v in word_map.items() if k != v}

print(f"Total word mappings: {len(word_map)}")

# === BUILD EFFICIENT SINGLE-PASS REGEX ===
# Build a map that includes lowercase, Capitalized, and UPPERCASE variants
all_variants = {}
for old, new in word_map.items():
    all_variants[old] = new
    # Capitalized
    cap_old = old[0].upper() + old[1:]
    cap_new = new[0].upper() + new[1:]
    all_variants[cap_old] = cap_new
    # ALL CAPS
    upper_old = old.upper()
    upper_new = new.upper()
    if upper_old != old:
        all_variants[upper_old] = upper_new

# Sort by length (longest first) to avoid partial matches
sorted_keys = sorted(all_variants.keys(), key=len, reverse=True)

# Build single alternation pattern
# Use \b word boundaries
pattern = r'\b(' + '|'.join(re.escape(k) for k in sorted_keys) + r')\b'
regex = re.compile(pattern)

def replacer(match):
    return all_variants[match.group(0)]

# Suffix rules: only singular -cion/-sion get accent (plural -ciones/-siones do NOT)
suffix_cion = re.compile(r'(?<=[a-záéíóúñA-ZÁÉÍÓÚÑ])cion\b')
suffix_sion = re.compile(r'(?<=[a-záéíóúñA-ZÁÉÍÓÚÑ])sion\b')

# === APPLY ===
start = time.time()
changed = 0
changes_detail = {}

for key in sorted(data):
    if key.startswith('_'):
        continue
    old_val = data[key]
    new_val = old_val

    # Single-pass word replacement
    new_val = regex.sub(replacer, new_val)

    # Suffix rules: singular -cion -> -ción, singular -sion -> -sión
    new_val = suffix_cion.sub('ción', new_val)
    new_val = suffix_sion.sub('sión', new_val)

    if new_val != old_val:
        data[key] = new_val
        changed += 1

elapsed = time.time() - start

with open('Localization/es.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"es.json: normalized accents in {changed} values ({elapsed:.1f}s)")
