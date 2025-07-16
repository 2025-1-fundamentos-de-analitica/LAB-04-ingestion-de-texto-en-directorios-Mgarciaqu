# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa

import pandas as pd
import os
import zipfile

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    
    with zipfile.ZipFile('files/input.zip', 'r') as z:
        z.extractall('files')

    input_dir = 'files/input'
    output_dir = 'files/output'

    os.makedirs(output_dir, exist_ok=True)

    for data in ['train', 'test']:
        
        frases = []
        etiquetas = []
        
        s_path = os.path.join(input_dir, data)
        
        for sent in ['negative', 'positive', 'neutral']:
            
            carpeta = os.path.join(s_path, sent)
            
            for file in os.listdir(carpeta):
                filepath = os.path.join(carpeta, file)
                
                with open(filepath, encoding='utf-8') as f:
                    frases.append(f.read().strip())
                    etiquetas.append(sent)
        
        df = pd.DataFrame({'phrase': frases, 'target': etiquetas})
        df.to_csv(os.path.join(output_dir, f'{data}_dataset.csv'), index=False)
