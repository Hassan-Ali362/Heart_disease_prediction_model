"""
Convert Jupyter Notebook (.ipynb) to Python script
Extract model training code from Colab notebook
"""
import json
import os

def convert_notebook_to_script(notebook_path, output_path='colab_model.py'):
    """
    Convert .ipynb notebook to .py script
    
    Args:
        notebook_path: Path to .ipynb file
        output_path: Output .py file path
    """
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Extract code cells
        code_cells = []
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
                source = cell.get('source', [])
                if isinstance(source, list):
                    code = ''.join(source)
                else:
                    code = source
                
                # Skip cells with magic commands or system commands
                if not code.strip().startswith(('!', '%', '%%')):
                    code_cells.append(code)
        
        # Write to Python file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('# Converted from Jupyter Notebook\n')
            f.write('# Original file: ' + notebook_path + '\n\n')
            
            for i, code in enumerate(code_cells):
                f.write(f'# Cell {i+1}\n')
                f.write(code)
                f.write('\n\n')
        
        print(f"✅ Converted notebook to {output_path}")
        print(f"📝 Extracted {len(code_cells)} code cells")
        return True
        
    except Exception as e:
        print(f"❌ Error converting notebook: {str(e)}")
        return False

def extract_model_info(notebook_path):
    """
    Analyze notebook to find model information
    """
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        info = {
            'model_type': None,
            'features': [],
            'libraries': set()
        }
        
        # Scan all code cells
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
                source = ''.join(cell.get('source', []))
                
                # Detect libraries
                if 'sklearn' in source or 'from sklearn' in source:
                    info['libraries'].add('sklearn')
                if 'tensorflow' in source or 'keras' in source:
                    info['libraries'].add('tensorflow')
                if 'torch' in source or 'pytorch' in source:
                    info['libraries'].add('pytorch')
                
                # Detect model types
                if 'RandomForest' in source:
                    info['model_type'] = 'RandomForestClassifier'
                elif 'LogisticRegression' in source:
                    info['model_type'] = 'LogisticRegression'
                elif 'XGBoost' in source or 'xgb' in source:
                    info['model_type'] = 'XGBoost'
                elif 'Sequential' in source or 'Model(' in source:
                    info['model_type'] = 'Neural Network (Keras)'
        
        info['libraries'] = list(info['libraries'])
        
        print("\n📊 Notebook Analysis:")
        print(f"   Model Type: {info['model_type'] or 'Unknown'}")
        print(f"   Libraries: {', '.join(info['libraries']) or 'None detected'}")
        
        return info
        
    except Exception as e:
        print(f"❌ Error analyzing notebook: {str(e)}")
        return None

# Example usage:
# convert_notebook_to_script('fraud_detection.ipynb', 'colab_model.py')
# extract_model_info('fraud_detection.ipynb')
