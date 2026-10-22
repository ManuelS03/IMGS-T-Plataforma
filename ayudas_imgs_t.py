"""Ayudas contextuales IMGS-T basadas en el documento de la profesora.
Los IDs siguen el orden de las 50 preguntas de la tabla preguntas.
"""

AYUDAS = {
    1: {
        "explicacion": 'Es tener un plan de negocio claro, por escrito y a largo plazo, que defina hacia dónde va la empresa y cómo va a lograr sus metas.',
        "ejemplo": 'Por ejemplo, si tienes un documento o plan de trabajo donde definiste cuántas prendas planeas producir, a qué nuevos mercados quieres venderles en los próximos 3 años y qué máquinas necesitas comprar para lograrlo.',
    },
    2: {
        "explicacion": 'Significa si al planear el futuro de tu negocio tienes en cuenta el cuidado del medio ambiente y el bienestar de los trabajadores, o si solo piensas en las ganancias económicas.',
        "ejemplo": 'Por ejemplo, si en tu plan de crecimiento para los próximos años incluiste metas para reducir el desperdicio de tela o para mejorar las condiciones de salud de tus operarias de confección.',
    },
    3: {
        "explicacion": 'Es un documento escrito y firmado por la gerencia donde la empresa declara públicamente su compromiso oficial con el cuidado ambiental y social.',
        "ejemplo": 'Por ejemplo, un texto breve publicado en las carteleras del taller o en la página web que diga: "En nuestra empresa nos comprometemos a reciclar el 100% de los retazos y a garantizar un trato justo a todo el personal".',
    },
    4: {
        "explicacion": 'Asignarle oficialmente a una persona o a un grupo de trabajadores la tarea de liderar y revisar los temas ambientales y sociales de la empresa.',
        "ejemplo": 'Por ejemplo, si nombraste formalmente al jefe de producción o al encargado de Talento Humano para que vigile el reciclaje de retazos y el uso del agua, reportando los avances directamente a la gerencia.',
    },
    5: {
        "explicacion": 'Saber si la persona encargada de estos temas tiene estudios, capacitaciones o cursos previos sobre medio ambiente, seguridad laboral o gestión social.',
        "ejemplo": 'Por ejemplo, evaluar si tu encargado ha hecho cursos en el SENA sobre manejo de residuos, diplomados universitarios en sostenibilidad o si aprende de forma empírica en el día a día.',
    },
    6: {
        "explicacion": 'Tener números y fechas claras para medir si estás mejorando. La meta es lo que quieres lograr y el indicador es la fórmula con la que mides el avance.',
        "ejemplo": 'Por ejemplo: Tu meta es bajar el consumo de luz en un 10% este año, y tu indicador es el número de kilovatios que registras mensualmente en la factura de energía.',
    },
    7: {
        "explicacion": 'Revisar de forma ordenada y cada cierto tiempo (mensual o semestral) si las metas ambientales y sociales se están cumpliendo o si hay problemas.',
        "ejemplo": 'Por ejemplo, si te sientas cada mes con tu equipo a revisar si disminuyó el desperdicio de rollos de tela o si se han presentado accidentes en las máquinas de coser.',
    },
    8: {
        "explicacion": 'Hacer un informe escrito que resuma los logros y fallas de la empresa en temas ambientales y con los trabajadores, y compartírselo a clientes o socios.',
        "ejemplo": 'Por ejemplo, armar una cartilla al final del año que muestre cuánta agua ahorró el taller y cuántas capacitaciones recibieron las costureras, para entregársela a tus clientes principales.',
    },
    9: {
        "explicacion": 'Usar guías, manuales o normas internacionales oficiales para organizar los procesos ambientales y sociales de la empresa.',
        "ejemplo": 'Por ejemplo, si organizas tus auditorías para cumplir con la norma de gestión ambiental ISO 14001 o si basas tus metas en los Objetivos de Desarrollo Sostenible (ODS).',
    },
    10: {
        "explicacion": 'Es un ejercicio básico para identificar cuáles son los problemas sociales o ambientales más críticos y prioritarios para tu tipo de negocio.',
        "ejemplo": 'Por ejemplo, entender que para un taller de confección textil, el residuo de retazos y la ergonomía de las costureras son temas vitales, mientras que para una lavandería industrial el tema crítico es el vertimiento de agua con químicos.',
    },
    11: {
        "explicacion": 'Analizar si un problema con el medio ambiente o con la comunidad puede hacer que tu empresa pierda dinero, clientes o sufra sanciones legales.',
        "ejemplo": 'Por ejemplo, si prevés que no tener un sistema de tratamiento de agua te puede costar una multa de la autoridad ambiental, o que usar empaques plásticos no reciclables haga que los clientes dejen de comprarte.',
    },
    12: {
        "explicacion": 'Guardar o presupuestar dinero pensando en las nuevas leyes del gobierno sobre el medio ambiente o en los cambios del clima que afecten el negocio.',
        "ejemplo": 'Por ejemplo, si incluyes en tus cuentas del año el dinero que vas a necesitar para pagar el nuevo impuesto al carbono en Colombia o la inversión para cambiar a motores más eficientes por el alza en las tarifas de energía.',
    },
    13: {
        "explicacion": 'Tener planes financieros para reaccionar ante la escasez o el aumento repentino de precios en los materiales esenciales para fabricar tus prendas.',
        "ejemplo": 'Por ejemplo, si calculas cómo te afectaría económicamente que suba el precio del algodón o de los tintes por problemas de importación, y buscas alternativas de proveedores locales para no frenar la producción.',
    },
    14: {
        "explicacion": 'Separar una cantidad fija de dinero de las ganancias de la empresa destinada únicamente a proyectos ambientales, sociales o de mejora técnica.',
        "ejemplo": 'Por ejemplo, si dejas un rubro de dinero exclusivo en tu flujo de caja para comprar iluminación LED para la planta, renovar las sillas ergonómicas o pagar los exámenes médicos ocupacionales de las operarias.',
    },
    15: {
        "explicacion": 'Calcular si el dinero que invertiste en un proyecto ambiental o social se recuperó a través de ahorros en facturas, menor desperdicio o aumento de ventas.',
        "ejemplo": 'Por ejemplo, si invertiste 5 millones en cambiar las calderas o planchas por unas de bajo consumo y calculas en cuántos meses se paga sola esa inversión gracias a la reducción en la factura del gas.',
    },
    16: {
        "explicacion": 'Significa que al elegir a quién comprarle las telas o insumos, no solo miras el precio barato, sino también si ellos cumplen las leyes laborales y cuidan el entorno.',
        "ejemplo": 'Por ejemplo, si prefieres comprarle rollos de hilo a una hilandería que cuenta con certificaciones ambientales o que garantiza que paga salarios justos y no tiene trabajadores informales.',
    },
    17: {
        "explicacion": 'Analizar si la forma en que tu empresa produce y vende hoy seguirá siendo rentable y aceptada por el mercado dentro de 5 o 10 años.',
        "ejemplo": 'Por ejemplo, si evalúas si seguir fabricando "moda rápida" de baja calidad será viable en el futuro, o si debes migrar hacia prendas de mayor duración y materiales reciclados porque los consumidores ya no quieren comprar productos altamente contaminantes.',
    },
    18: {
        "explicacion": 'Tener reglas estrictas y cuentas claras para asegurar que el dinero destinado a proyectos sociales o ambientales se use de forma honesta y transparente.',
        "ejemplo": 'Por ejemplo, si tienes un canal o buzón para reportar si se están cobrando comisiones ilegales a los proveedores, y si llevas una contabilidad separada y transparente de las donaciones o inversiones ambientales.',
    },
    19: {
        "explicacion": 'Medir cómo la operación de tu fábrica ayuda a mover la economía, el empleo y los negocios de los habitantes del barrio o municipio donde estás ubicado.',
        "ejemplo": 'Por ejemplo, si calculas cuántos empleos generas en la comunidad local o si priorizas contratar talleres satélites locales del mismo sector, beneficiando los ingresos de las familias vecinas.',
    },
    20: {
        "explicacion": 'Usar los datos de ahorros ambientales o costos sociales para decidir los próximos pasos comerciales o de inversión de la gerencia.',
        "ejemplo": 'Por ejemplo, si decides lanzar una nueva línea de ropa ecológica porque los datos de costos te muestran que usar algodón orgánico te abrirá mercado con clientes internacionales que pagan mejor.',
    },
    21: {
        "explicacion": 'Tener reglas escritas y oficiales que garanticen el respeto a los derechos de los trabajadores, el pago puntual de salarios y el cumplimiento de los contratos de ley.',
        "ejemplo": 'Por ejemplo, si tienes un reglamento interno de trabajo donde se especifica el pago legal de las horas extra a los operarios de confección, los descansos correspondientes y el pago completo de la seguridad social.',
    },
    22: {
        "explicacion": 'Contar con un plan organizado de prevención para proteger a los empleados de accidentes, lesiones y enfermedades causadas por las actividades del taller.',
        "ejemplo": 'Por ejemplo, si cuentas con un encargado del Sistema de Gestión de Seguridad y Salud en el Trabajo (SG-SST), llevas registro de las afiliaciones a la ARL y realizas las inspecciones obligatorias de los puestos de trabajo.',
    },
    23: {
        "explicacion": 'Entregar los elementos de protección adecuados y adecuar los espacios físicos para evitar riesgos mecánicos, ergonómicos o químicos en la planta.',
        "ejemplo": 'Por ejemplo, si los operarios de corte usan guantes de malla de acero, si las costureras tienen sillas ergonómicas con apoyo lumbar, si hay extractores para eliminar la mota del aire y si las máquinas tienen guardas de protección en las agujas.',
    },
    24: {
        "explicacion": 'Tener mecanismos estrictos de control para asegurar que ningún menor de edad trabaje en la empresa y garantizar que no se discrimine a nadie por su género, raza o procedencia al contratar.',
        "ejemplo": 'Por ejemplo, si en tu proceso de selección exiges obligatoriamente la cédula de ciudadanía para verificar la mayoría de edad y si los salarios se asignan por el puesto de trabajo (como operaria de plana o fileteadora) sin importar quién realice la labor.',
    },
    25: {
        "explicacion": 'Garantizar que tanto hombres como mujeres tengan las mismas oportunidades para acceder a puestos de liderazgo, salarios justos y capacitaciones dentro del taller.',
        "ejemplo": 'Por ejemplo, si promueves que las mujeres ocupen cargos de supervisión de planta, jefaturas de diseño o administración, rompiendo la tendencia de dejarlas exclusivamente en los puestos de costura básica.',
    },
    26: {
        "explicacion": 'Brindar espacios de estudio o entrenamiento técnico para que el personal mejore sus habilidades, aprenda sobre cuidado ambiental o reciba charlas de salud.',
        "ejemplo": 'Por ejemplo, si realizas talleres prácticos para enseñar técnicas de confección eficiente que reduzcan el desperdicio de tela, o si programas charlas sobre pausas activas y manejo del estrés laboral.',
    },
    27: {
        "explicacion": 'Revisar que los proveedores, talleres externos o satélites a los que les subcontratas producción operen de manera legal y traten con dignidad a sus trabajadores.',
        "ejemplo": 'Por ejemplo, si visitas los talleres satélites externos que te ayudan a armar las prendas para verificar que no utilicen mano de obra informal o en condiciones de hacinamiento.',
    },
    28: {
        "explicacion": 'Canales oficiales y seguros para que los empleados expresen sus opiniones, sugieran mejoras o reporten problemas internos sin temor a represalias.',
        "ejemplo": 'Por ejemplo, contar con un Comité de Convivencia Laboral activo, un buzón físico de sugerencias en la planta o reuniones periódicas entre los delegados de las mesas de confección y la gerencia.',
    },
    29: {
        "explicacion": 'Analizar si el funcionamiento diario de tu fábrica genera molestias, ruidos, congestión o si, por el contrario, beneficia directamente el entorno vecinal.',
        "ejemplo": 'Por ejemplo, evaluar si el ruido de las máquinas industriales o el cargue de mercancía en la calle incomoda a los residentes del barrio, y tomar acciones de aislamiento acústico o logística para solucionarlo.',
    },
    30: {
        "explicacion": 'Apoyar proyectos, donaciones o actividades organizadas por los vecinos, fundaciones o juntas de acción comunal del sector donde opera el negocio.',
        "ejemplo": 'Por ejemplo, si donas saldos de tela a fundaciones del barrio para que dicten cursos de manualidades, o si apoyas el mantenimiento de los parques y zonas verdes que rodean tu planta de producción.',
    },
    31: {
        "explicacion": 'Tener un registro escrito de cuáles actividades de tu producción ensucian el agua, gastan demasiada energía, generan humo o producen basura.',
        "ejemplo": 'Por ejemplo, si tienes una matriz donde mapeaste que el proceso de teñido contamina el agua con químicos, que el área de planchado consume altos niveles de gas y que el área de corte genera residuos de retales.',
    },
    32: {
        "explicacion": 'Llevar un registro exacto de cuántos litros o metros cúbicos de agua gasta la fábrica y correlacionarlo con el volumen de producción diaria o mensual.',
        "ejemplo": 'Por ejemplo, si anotas los datos del medidor de agua de forma semanal y calculas cuántos litros consumes específicamente por cada kilogramo de tela lavado o teñido.',
    },
    33: {
        "explicacion": 'Aplicar métodos técnicos para gastar menos agua limpia, capturando y volviendo a usar el agua sobrante de algunos procesos en lugar de botarla al desagüe.',
        "ejemplo": 'Por ejemplo, si tienes tanques para recolectar agua lluvia y usarla en los baños, o si instalaste sistemas informáticos de recirculación que filtran y reutilizan el agua del último enjuague de las prendas para el siguiente ciclo de lavado.',
    },
    34: {
        "explicacion": 'Registrar detalladamente el gasto de luz y combustibles (como gas o ACPM) para implementar medidas informáticas o de hardware que disminuyan el consumo energético.',
        "ejemplo": 'Por ejemplo, si revisas los kilovatios consumidos por la planta, programas el encendido por turnos de las máquinas de coser para evitar picos de consumo, o instalas motores electrónicos de bajo consumo (servomotores) en lugar de los motores de embrague tradicionales.',
    },
    35: {
        "explicacion": 'Almacenar, usar y desechar los tintes, solventes y productos químicos bajo estrictas normas de seguridad para proteger a los trabajadores y evitar derrames ambientales.',
        "ejemplo": 'Por ejemplo, si mantienes los químicos bajo llave en un área ventilada, con diques de contención para derrames, etiquetas claras de peligrosidad y hojas de seguridad técnica legibles para los operarios de lavandería o tintorería.',
    },
    36: {
        "explicacion": 'Clasificar, almacenar y buscar un destino final responsable (venta, reciclaje o reutilización) para la basura y retazos textiles sobrantes de la producción.',
        "ejemplo": 'Por ejemplo, si separas los retazos de algodón de los sintéticos en contenedores distintos, evitas mezclarlos con basura común y los entregas a empresas autorizadas que los desmechan o trituran.',
    },
    37: {
        "explicacion": 'Revisar de forma ordenada si el taller cumple con todas las leyes ambientales de Colombia vigentes (como el Decreto 1076 de 2015 sobre vertimientos industriales y residuos peligrosos).',
        "ejemplo": 'Por ejemplo, si contratas laboratorios certificados para que midan periódicamente la temperatura y los químicos del agua residual antes de que salga al alcantarillado, garantizando que cumples con la norma de vertimientos.',
    },
    38: {
        "explicacion": 'Controlar el humo o gases contaminantes que emiten tus equipos (como calderas de vapor) o calcular la cantidad total de gases de efecto invernadero que arroja tu negocio al aire.',
        "ejemplo": 'Por ejemplo, si realizas los mantenimientos técnicos y la revisión técnico-mecánica obligatoria a la caldera de vapor que calienta las planchas o las tinas de teñido para asegurar que los gases estén dentro del límite legal.',
    },
    39: {
        "explicacion": 'Diseñar prendas o planear la producción pensando en que nada se desperdicie, logrando que los materiales duren más o se reciclen al terminar su vida útil.',
        "ejemplo": 'Por ejemplo, si aplicas técnicas informáticas de trazo digital (moldería zero-waste) para aprovechar el 95% del ancho del rollo de tela, o si diseñas prendas usando hilos y botones del mismo material para que la prenda sea 100% reciclable en el futuro.',
    },
    40: {
        "explicacion": 'Exigir o verificar que las textileras o empresas logísticas con las que trabajas cumplan con normas ambientales y demuestren un comportamiento responsable con el entorno.',
        "ejemplo": 'Por ejemplo, si antes de firmar un contrato de compra de insumos, le solicitas a la tintorería externa el certificado vigente de vertimientos para asegurarte de que ellos no están contaminando ríos con sus colorantes.',
    },
    41: {
        "explicacion": 'Empezar a registrar y guardar de manera ordenada los números o información clave sobre tus consumos, desperdicios y personal, en lugar de dejar que se pierdan.',
        "ejemplo": 'Por ejemplo, si anotas diariamente los metros de tela que se desperdician en la mesa de corte, los metros cúbicos de agua que consume el área de lavado o las horas extra que registran las operarias en sus planillas.',
    },
    42: {
        "explicacion": 'Dejar de usar cuadernos o papeles sueltos y pasar la información de tus consumos e impactos a archivos o programas dentro de la computadora para que no se pierda.',
        "ejemplo": 'Por ejemplo, si digitas el gasto mensual de luz y agua en una hoja de Excel, o si usas un software contable o de producción para registrar los costos e inventarios de los retazos textiles.',
    },
    43: {
        "explicacion": 'Lograr que la información que recoge cada departamento de la fábrica se junte en una sola base de datos para poder analizar la empresa de forma completa.',
        "ejemplo": 'Por ejemplo, si los datos de residuos de tela que mide el jefe de producción se pueden cruzar fácilmente en la computadora con los costos de compra que maneja contabilidad y los registros de ausentismo de talento humano.',
    },
    44: {
        "explicacion": 'Revisar de forma matemática los números guardados para descubrir problemas, tendencias o ahorros que te ayuden a decidir el rumbo del negocio.',
        "ejemplo": 'Por ejemplo, si revisas los datos históricos de consumo de energía y descubres que las máquinas antiguas gastan el doble de luz, y usas ese análisis para decidir la compra de motores electrónicos nuevos más eficientes.',
    },
    45: {
        "explicacion": 'Crear informes escritos cada cierto tiempo basados en números reales y precisos para mostrar el desempeño social y ambiental de la planta.',
        "ejemplo": 'Por ejemplo, si generas un reporte semestral en PDF que muestre con gráficos exactos la reducción en el desperdicio de rollos de tela y el cumplimiento de las capacitaciones de seguridad laboral para presentarlo a la junta directiva.',
    },
    46: {
        "explicacion": 'Instalar programas informáticos o maquinaria moderna automatizada que te ayude directamente a gastar menos recursos y a controlar la contaminación.',
        "ejemplo": 'Por ejemplo, si implementas un software de diseño y trazo digital (Optitex, Audaces, Gerber) para acomodar los moldes y reducir el desperdicio de tela al mínimo, o si usas sensores digitales que cortan el flujo de agua en las tinas cuando el lavado termina.',
    },
    47: {
        "explicacion": 'Tener fórmulas matemáticas fijadas en un sistema informático que calculen de forma automática y constante el rendimiento social, ambiental o económico de la empresa.',
        "ejemplo": 'Por ejemplo, tener configurada en tu sistema la fórmula: (Kilogramos de retazos generados / Kilogramos de tela totales comprados) para vigilar automáticamente el indicador de eficiencia material mes a mes.',
    },
    48: {
        "explicacion": 'Usar pantallas interactivas con gráficos de barras, líneas o semáforos de colores digitales para entender la situación del negocio en un segundo, en lugar de leer hojas llenas de números.',
        "ejemplo": 'Por ejemplo, entrar a una plataforma web donde un tablero digital te muestra en color verde si cumpliste la meta de ahorro de agua del mes o en color rojo si el consumo de energía en los módulos de confección se disparó.',
    },
    49: {
        "explicacion": 'Hacer que las máquinas, sensores o sistemas informáticos guarden y organicen la información por sí solos, evitando que un trabajador tenga que anotar los datos manualmente.',
        "ejemplo": 'Por ejemplo, si las máquinas de teñido envían directamente el registro de los litros de agua consumidos a una base de datos centralizada en la nube mediante internet, sin necesidad de que el operario lo apunte en una hoja de papel.',
    },
    50: {
        "explicacion": 'Usar las bases de datos de la computadora para crear nuevos productos ecológicos, corregir fallas repetitivas o demostrarle legalmente a grandes clientes internacionales que tu planta es responsable.',
        "ejemplo": 'Por ejemplo, si exportas prendas y utilizas el registro digital de trazabilidad de tus telas para certificar ante un cliente extranjero que tu producción cumple con los estándares ambientales europeos, asegurando un contrato comercial de alto valor.',
    },
}
