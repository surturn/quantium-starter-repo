from app import app

# A helper function to find components in your layout
def component_exists(layout, target_id):
    # 1. Check if the current component is the one we want
    if hasattr(layout, 'id') and layout.id == target_id:
        return True
    
    # 2. If not, check if it has children (components inside it)
    if hasattr(layout, 'children'):
        children = layout.children
        # Ensure children is a list so we can loop through it
        if not isinstance(children, list):
            children = [children]
        
        # 3. Recursively check all children
        for child in children:
            if component_exists(child, target_id):
                return True
                
    # 4. If we looked everywhere and didn't find it
    return False

# --- THE TESTS ---

def test_header_exists():
    assert component_exists(app.layout, "header") is True, "The Header (id='header') was not found."

def test_region_picker_exists():
    assert component_exists(app.layout, "region-selector") is True, "The Region Picker (id='region-selector') was not found."

def test_visualization_exists():
    assert component_exists(app.layout, "sales-graph") is True, "The Graph (id='sales-graph') was not found."