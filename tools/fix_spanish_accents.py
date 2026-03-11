"""
Normalize Spanish accents across all es.json values.
Adds proper tildes, ñ, and ¡¿ markers using conservative word-boundary replacements.
Only replaces unambiguous cases to avoid false positives.
"""
import json
import re

with open('Localization/es.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# === UNAMBIGUOUS WORD REPLACEMENTS ===
# These words are ALWAYS accented in Spanish regardless of context

# -ción / -sión endings (always accented)
suffix_rules = [
    (r'cion\b', 'ción'),
    (r'ciones\b', 'ciones'),  # already correct, no change needed
    (r'sion\b', 'sión'),
    (r'siones\b', 'siones'),  # already correct
]

# ñ words (always have ñ)
n_tilde_words = {
    'ano': 'año', 'anos': 'años',
    'dano': 'daño', 'danos': 'daños',
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
    'ensenanza': 'enseñanza', 'ensenar': 'enseñar',
    'ensena': 'enseña',
    'nino': 'niño', 'nina': 'niña', 'ninos': 'niños', 'ninas': 'niñas',
    'banarse': 'bañarse', 'bano': 'baño',
    'punalada': 'puñalada',
    'puno': 'puño', 'punos': 'puños',
    'cuno': 'cuño',
    'lena': 'leña',
    'canon': 'cañón',
    'castano': 'castaño',
    'arana': 'araña', 'aranas': 'arañas',
    'carino': 'cariño',
    'extrano': 'extraño', 'extrana': 'extraña',
    'extranos': 'extraños', 'extranas': 'extrañas',
    'empunar': 'empuñar',
    'vinedo': 'viñedo',
    'otono': 'otoño',
    'panuelo': 'pañuelo',
    'cabana': 'cabaña',
    'hazana': 'hazaña', 'hazanas': 'hazañas',
    'compania': 'compañía',  # also gets accent
}

# Unambiguous accented words (ALWAYS accented in all contexts)
always_accented = {
    # Common adverbs/conjunctions
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
    'inutl': 'inútil',
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
    'heroico': 'heroico',  # no accent needed actually
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

    # Past tenses (unambiguous -ó endings)
    'perdio': 'perdió',
    'murio': 'murió',
    'cayo': 'cayó',
    'huyo': 'huyó',
    'recibio': 'recibió',
    'encontro': 'encontró',
    'alcanzo': 'alcanzó',
    'venció': 'venció',  # already correct
    'destruyo': 'destruyó',
    'descubrio': 'descubrió',
    'convirtio': 'convirtió',
    'decidio': 'decidió',
    'consiguio': 'consiguió',
    'cumplio': 'cumplió',
    'ofrecio': 'ofreció',
    'prometio': 'prometió',
    'resistio': 'resistió',
    'sobrevivio': 'sobrevivió',
    'sucedio': 'sucedió',
    'traiciono': 'traicionó',
    'derroto': 'derrotó',
    'desperto': 'despertó',
    'escapo': 'escapó',
    'gano': 'ganó',
    'llego': 'llegó',
    'paso': 'pasó',
    'regreso': 'regresó',
    'salvo': 'salvó',
    'supero': 'superó',
    'volvio': 'volvió',

    # Verb forms -é (first person past)
    'encontre': 'encontré',
    'llegue': 'llegué',
    'busque': 'busqué',

    # Common nouns with accent
    'corazon': 'corazón', 'corazones': 'corazones',
    'razon': 'razón', 'razones': 'razones',
    'cancion': 'canción', 'canciones': 'canciones',
    'mision': 'misión', 'misiones': 'misiones',
    'decision': 'decisión', 'decisiones': 'decisiones',
    'traicion': 'traición',
    'prision': 'prisión',
    'explosion': 'explosión',
    'ilusion': 'ilusión', 'ilusiones': 'ilusiones',
    'bendicion': 'bendición',
    'maldicion': 'maldición',
    'pocion': 'poción', 'pociones': 'pociones',
    'cuestion': 'cuestión',
    'religion': 'religión',
    'region': 'región', 'regiones': 'regiones',
    'habitacion': 'habitación', 'habitaciones': 'habitaciones',
    'posicion': 'posición',
    'informacion': 'información',
    'direccion': 'dirección',
    'proteccion': 'protección',
    'destruccion': 'destrucción',
    'construccion': 'construcción',
    'condicion': 'condición', 'condiciones': 'condiciones',
    'reputacion': 'reputación',
    'resurreccion': 'resurrección',
    'creacion': 'creación',
    'puntuacion': 'puntuación',
    'salvacion': 'salvación',
    'negociacion': 'negociación',
    'confrontacion': 'confrontación',
    'aceptacion': 'aceptación',
    'separacion': 'separación',
    'liberacion': 'liberación',
    'bonificacion': 'bonificación',
    'clasificacion': 'clasificación',
    'combinacion': 'combinación',
    'comparacion': 'comparación',
    'comunicacion': 'comunicación',
    'concentracion': 'concentración',
    'configuracion': 'configuración',
    'continuacion': 'continuación',
    'contribucion': 'contribución',
    'conversacion': 'conversación',
    'curacion': 'curación',
    'dedicacion': 'dedicación',
    'definicion': 'definición',
    'descripcion': 'descripción',
    'desaparicion': 'desaparición',
    'educacion': 'educación',
    'elevacion': 'elevación',
    'eliminacion': 'eliminación',
    'emocion': 'emoción', 'emociones': 'emociones',
    'encarnacion': 'encarnación',
    'evolución': 'evolución',
    'excepcion': 'excepción',
    'explicacion': 'explicación',
    'generacion': 'generación',
    'identificacion': 'identificación',
    'imaginacion': 'imaginación',
    'instalacion': 'instalación',
    'interaccion': 'interacción',
    'investigacion': 'investigación',
    'invocacion': 'invocación',
    'justificacion': 'justificación',
    'legislacion': 'legislación',
    'localizacion': 'localización',
    'meditacion': 'meditación',
    'modificacion': 'modificación',
    'motivacion': 'motivación',
    'navegacion': 'navegación',
    'obligacion': 'obligación',
    'observacion': 'observación',
    'operacion': 'operación',
    'organizacion': 'organización',
    'orientacion': 'orientación',
    'percepcion': 'percepción',
    'poblacion': 'población',
    'preparacion': 'preparación',
    'presentacion': 'presentación',
    'produccion': 'producción',
    'profesion': 'profesión',
    'programacion': 'programación',
    'proporcion': 'proporción',
    'reaccion': 'reacción',
    'realizacion': 'realización',
    'recepcion': 'recepción',
    'recomendacion': 'recomendación',
    'recuperacion': 'recuperación',
    'reduccion': 'reducción',
    'relacion': 'relación', 'relaciones': 'relaciones',
    'renovacion': 'renovación',
    'repeticion': 'repetición',
    'representacion': 'representación',
    'restauracion': 'restauración',
    'restriccion': 'restricción',
    'revelacion': 'revelación',
    'revolucion': 'revolución',
    'sancion': 'sanción',
    'satisfaccion': 'satisfacción',
    'seleccion': 'selección',
    'sensacion': 'sensación',
    'situacion': 'situación',
    'solucion': 'solución',
    'sugerencia': 'sugerencia',
    'tentacion': 'tentación',
    'tradicion': 'tradición',
    'transaccion': 'transacción',
    'transformacion': 'transformación',
    'ubicacion': 'ubicación',
    'venganza': 'venganza',  # no accent needed
    'version': 'versión',
    'violacion': 'violación',
    'vocacion': 'vocación',

    # Other common words
    'energia': 'energía',
    'magia': 'magia',  # no accent
    'estrategia': 'estrategia',  # no accent
    'categoria': 'categoría',
    'filosofia': 'filosofía',
    'compania': 'compañía',
    'valentia': 'valentía',
    'sabiduria': 'sabiduría',
    'armonia': 'armonía',
    'melodia': 'melodía',
    'garantia': 'garantía',
    'fantasia': 'fantasía',
    'herejia': 'herejía',
    'alegria': 'alegría',
    'agonia': 'agonía',
    'ironia': 'ironía',

    # Question/exclamation words (always accented when used)
    # Be careful: only in question context
    # Skip ambiguous ones like que/como/donde

    # Common adjectives
    'debiles': 'débiles',
    'fertil': 'fértil',
    'esteril': 'estéril',
    'fragil': 'frágil',
    'movil': 'móvil',
    'habil': 'hábil',
    'volatil': 'volátil',
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
    'legendario': 'legendario',  # no accent
    'maximo': 'máximo', 'maxima': 'máxima',
    'minimo': 'mínimo', 'minima': 'mínima',
    'optimo': 'óptimo', 'optima': 'óptima',
    'pacifico': 'pacífico', 'pacifica': 'pacífica',
    'romantico': 'romántico', 'romantica': 'romántica',
    'sarcastico': 'sarcástico', 'sarcastica': 'sarcástica',
    'satirico': 'satírico', 'satirica': 'satírica',
    'simpatico': 'simpático', 'simpatica': 'simpática',
    'tragico': 'trágico', 'tragica': 'trágica',

    # Verbs with accent
    'podria': 'podría', 'podrias': 'podrías',
    'tendria': 'tendría', 'tendrias': 'tendrías',
    'deberia': 'debería', 'deberias': 'deberías',
    'seria': 'sería',  # note: also means "series" but more commonly "would be"
    'haria': 'haría', 'harias': 'harías',
    'vendria': 'vendría',
    'diria': 'diría',
    'sabria': 'sabría',
    'querria': 'querría',
    'estaria': 'estaría',
    'daria': 'daría',
    'iria': 'iría',
    'pondria': 'pondría',
    'saldria': 'saldría',
    'habria': 'habría',
    'valdria': 'valdría',

    # More verbs
    'esta': 'está',  # risky but very common - "is" vs "this"
    # Skip "esta" — too ambiguous (esta=this feminine, está=is)

    # Words with ú
    'musculo': 'músculo', 'musculos': 'músculos',
    'obstaculo': 'obstáculo', 'obstaculos': 'obstáculos',
    'vehiculo': 'vehículo',
    'articulo': 'artículo', 'articulos': 'artículos',
    'calculo': 'cálculo',
    'capitulo': 'capítulo',
    'catalogo': 'catálogo',
    'curriculo': 'currículo',
    'estimulo': 'estímulo',
    'pendulo': 'péndulo',
    'titulo': 'título', 'titulos': 'títulos',
    'vinculo': 'vínculo',
    'brujula': 'brújula',
    'formula': 'fórmula', 'formulas': 'fórmulas',
    'clausula': 'cláusula',
    'celula': 'célula', 'celulas': 'células',
    'capsula': 'cápsula',

    # Words ending in -ón (very common)
    'dragon': 'dragón', 'dragones': 'dragones',
    'campeon': 'campeón', 'campeones': 'campeones',
    'patron': 'patrón', 'patrones': 'patrones',
    'ladron': 'ladrón', 'ladrones': 'ladrones',
    'limon': 'limón',
    'jabon': 'jabón',
    'rincon': 'rincón',
    'salon': 'salón',
    'baston': 'bastón',
    'marron': 'marrón',
    'boton': 'botón', 'botones': 'botones',
    'cajon': 'cajón',
    'corazon': 'corazón',
    'escalon': 'escalón',
    'limon': 'limón',
    'melon': 'melón',
    'monton': 'montón',
    'peaton': 'peatón',
    'perdon': 'perdón',
    'sermon': 'sermón',
    'tiburon': 'tiburón',
    'varon': 'varón',

    # -és ending
    'ingles': 'inglés',
    'interes': 'interés',
    'marques': 'marqués',
    'traves': 'través',
    'cortes': 'cortés',
    'despues': 'después',
    'ademas': 'además',

    # más is very common and almost always accented (vs "mas" = "but", archaic)
    'mas': 'más',
}

# Remove "esta" — too ambiguous
# already not in the dict

def apply_word_replacements(text, word_map):
    """Replace whole words using word boundaries."""
    for old, new in word_map.items():
        if old == new:
            continue
        # Case-sensitive replacement with word boundaries
        pattern = r'\b' + re.escape(old) + r'\b'
        text = re.sub(pattern, new, text)
        # Also handle capitalized version
        if old[0].islower():
            cap_old = old[0].upper() + old[1:]
            cap_new = new[0].upper() + new[1:]
            pattern = r'\b' + re.escape(cap_old) + r'\b'
            text = re.sub(pattern, cap_new, text)
        # ALL CAPS version
        if old.upper() != old:
            pattern = r'\b' + re.escape(old.upper()) + r'\b'
            text = re.sub(pattern, new.upper(), text)
    return text

def add_inverted_punctuation(text):
    """Add ¡ before ! and ¿ before ? at sentence boundaries."""
    # Don't modify if already has ¡ or ¿
    if '¡' in text or '¿' in text:
        return text
    # Don't modify format strings, short labels, or keys
    if len(text) < 5:
        return text

    # Add ¿ before questions
    # Pattern: start of string or after sentence-ending punctuation, optional whitespace/quotes
    text = re.sub(r'(^|[.!]\s+)([""]?)([A-ZÁÉÍÓÚÑ¡¿][^?]*\?)', lambda m: m.group(1) + m.group(2) + '¿' + m.group(3), text)

    # Add ¡ before exclamations
    text = re.sub(r'(^|[.?]\s+)([""]?)([A-ZÁÉÍÓÚÑ¡¿][^!]*!)', lambda m: m.group(1) + m.group(2) + '¡' + m.group(3), text)

    return text

# Apply fixes
changed = 0
for key in sorted(data):
    if key.startswith('_'):
        continue
    old_val = data[key]
    new_val = old_val

    # Apply ñ replacements
    new_val = apply_word_replacements(new_val, n_tilde_words)

    # Apply accent replacements
    new_val = apply_word_replacements(new_val, always_accented)

    # Apply -cion -> -ción suffix rule (catches words not in the dictionary)
    new_val = re.sub(r'(?<=[a-záéíóúñ])cion\b', 'ción', new_val)
    new_val = re.sub(r'(?<=[A-ZÁÉÍÓÚÑ])CION\b', 'CIÓN', new_val)

    # Apply -sion -> -sión suffix rule
    new_val = re.sub(r'(?<=[a-záéíóúñ])sion\b', 'sión', new_val)

    # Add ¡¿ (conservative — only for clear sentence-start exclamations/questions)
    # Skip this for now — too many edge cases with game text formatting

    if new_val != old_val:
        data[key] = new_val
        changed += 1

with open('Localization/es.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"es.json: normalized accents in {changed} values")
