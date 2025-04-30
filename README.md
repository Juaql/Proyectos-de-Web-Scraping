# Web Scraping Proyects

Alcance del Documento

En este documento se presentan resúmenes teóricos y proyectos prácticos vinculados a los módulos de Python que permiten realizar Web Scraping. Si bien no se abordan la totalidad de los módulos disponibles para esta tarea, el enfoque está orientado a aquellos que resultan pertinentes para los proyectos aquí desarrollados.

La selección de módulos y herramientas responde a un criterio de aplicabilidad: se prioriza su utilidad en contextos relacionados con el trading algorítmico y áreas afines, como la economía y las finanzas. En este sentido, el propósito es construir soluciones prácticas que respondan a necesidades concretas dentro de estos campos.




#
Proyecto I: News Analysis

El objetivo de este proyecto es desarrollar un sistema de búsqueda y análisis de noticias, mediante técnicas de Web Scraping, que permita extraer contenidos relevantes a partir de palabras clave definidas por el usuario. La finalidad es facilitar el acceso a información actualizada proveniente de diversos portales de noticias, centrada en temáticas específicas de interés.

Para llevar a cabo esta tarea se emplearán los módulos requests y BeautifulSoup, fundamentales en la recolección y el procesamiento de contenido web en Python. Este enfoque no solo permite automatizar la obtención de datos informativos, sino que también contribuye al desarrollo de herramientas aplicables al análisis contextual en disciplinas como la economía, las finanzas y el trading algorítmico.



#
Proyecto II: Obtener información de las páginas oficiales del gobierno

El análisis de variables macroeconómicas requiere del acceso a datos confiables, actualizados y de carácter oficial. En Argentina, el portal de datos del Ministerio de Economía (economia.gob.ar/datos) constituye una fuente pública centralizada que pone a disposición indicadores clave sobre el funcionamiento de la economía nacional, tales como precios, balanza de pagos, deuda pública, cuentas fiscales, entre otros.

Este proyecto tiene como objetivo automatizar la recolección de información desde dicho portal, estructurando los datos para su posterior análisis. La extracción sistemática de estos recursos permitirá integrar indicadores macroeconómicos en modelos cuantitativos, facilitar el seguimiento de políticas públicas, y complementar estudios aplicados al ámbito del trading algorítmico y la economía aplicada.

Para ello aplicaremos el uso nuevamente de el módulo request y del módulo zipfile, este proyecto será relativamente corto ya que se trata de la descarga de un archivo solo en donde luego lo implementaremos para proyectos relacionados a SQL y pandas
