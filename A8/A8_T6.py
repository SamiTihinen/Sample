import os
import sys
from typing import Optional, List, Dict

class SVGElement:
    """Yksinkertainen luokka kuvaamaan piirrettyä SVG-elementtiä."""
    def __init__(self, type_name: str, params: Dict):
        self.type_name = type_name
        self.params = params

class Dwg:
    """Simuloitu svgwrite.Drawing-objekti piirustusten keräämiseen."""
    def __init__(self):
        self.elements: List[SVGElement] = []
        
    def rect(self, insert: Tuple[float, float], size: Tuple[float, float], fill: str, stroke: str) -> None:
        """Lisää suorakulmion (neliön) piirustukseen."""
        self.elements.append(SVGElement("rect", {
            "insert": insert, "size": size, "fill": fill, "stroke": stroke
        }))

    def circle(self, center: Tuple[float, float], r: float, fill: str, stroke: str) -> None:
        """Lisää ympyrän piirustukseen."""
        self.elements.append(SVGElement("circle", {
            "center": center, "r": r, "fill": fill, "stroke": stroke
        }))

    def save(self, filename: str, pretty: bool = False, indent: int = 2) -> bool:
        """Simuloi tallennusta pyydetyssä SVG-muodossa."""
        if not self.elements:
            return False
        svg_content = '<?xml version="1.0" encoding="utf-8" ?>\n'
        if pretty:
            svg_content += '<svg>\n'
            
            indent_str = ' ' * indent
            for element in self.elements:
                params_str = ' '.join(f'{k}="{v}"' for k, v in element.params.items())
                svg_content += f'{indent_str}<{element.type_name} {params_str} />\n'
                
            svg_content += '</svg>\n'
        else:
            svg_content += '<svg>'
            for element in self.elements:
                 params_str = ' '.join(f'{k}="{v}"' for k, v in element.params.items())
                 svg_content += f'<{element.type_name} {params_str} />'
            svg_content += '</svg>'
            
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            return True
        except IOError:
            print(f"Error: Could not save file {filename}.")
            return False

MENU_OPTIONS = {
    1: "Draw square",
    2: "Draw circle",
    3: "Save svg",
    0: "Exit"
}

def _display_menu() -> None:
    """Näyttää valikkovaihtoehdot."""
    print("Options:")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}.--.{value}")

def _get_float_input(prompt: str) -> Optional[float]:
    """Kysyy liukulukua ja käsittelee virheet."""
    try:
        return float(input(prompt))
    except ValueError:
        return None

def _get_str_input(prompt: str) -> str:
    """Kysyy merkkijonoa."""
    return input(prompt)

def draw_square(dwg: Dwg) -> None:
    """Kysyy neliön parametrit ja piirtää sen."""
    print("Insert.square")
    
    left_edge_pos = _get_float_input("--.Left.edge.position:")
    top_edge_pos = _get_float_input("--.Top.edge.position:")
    side_length = _get_float_input("--.Side.length:")
    fill_color = _get_str_input("--.Fill.color:")
    stroke_color = _get_str_input("--.Stroke.color:")
    
    if None in [left_edge_pos, top_edge_pos, side_length]:
        print("Input.error!.Square.not.drawn.")
        return

    dwg.rect(
        insert=(left_edge_pos, top_edge_pos), 
        size=(side_length, side_length),
        fill=fill_color, 
        stroke=stroke_color
    )
    print("Square.drawn!")


def draw_circle(dwg: Dwg) -> None:
    """Kysyy ympyrän parametrit ja piirtää sen."""
    print("Insert.circle")
    
    center_x = _get_float_input("--.Center.X.coord:")
    center_y = _get_float_input("--.Center.Y.coord:")
    radius = _get_float_input("--.Radius:")
    fill_color = _get_str_input("--.Fill.color:")
    stroke_color = _get_str_input("--.Stroke.color:")
    
    if None in [center_x, center_y, radius]:
        print("Input.error!.Circle.not.drawn.")
        return
    dwg.circle(
        center=(center_x, center_y), 
        r=radius, 
        fill=fill_color, 
        stroke=stroke_color
    )
    print("Circle.drawn!")


def save_svg(dwg: Dwg) -> None:
    """Tallentaa piirustukset tiedostoon ja kysyy lupaa ylikirjoitukseen."""
    
    if not dwg.elements:
        print("Error: No elements to save.")
        return
        
    filename = _get_str_input("Insert.filename:")
    print(f"Saving.file.to: \"{filename}\"")
    proceed = _get_str_input("Proceed.(y/n)?:").lower().strip()
    
    if proceed == 'y':
        if dwg.save(filename, pretty=True, indent=2):
            print("Vector.saved.successfully!")
        else:
            print("Vector.save.failed.")
    else:
        print("Saving.aborted.")

def main():
    print("Program.starting.")
    
    dwg = Dwg()
    
    while True:
        _display_menu()
        
        try:
            choice = int(input("Your.choice:"))
        except ValueError:
            continue
        
        if choice == 1:
            draw_square(dwg)
        elif choice == 2:
            draw_circle(dwg)
        elif choice == 3:
            save_svg(dwg)
        elif choice == 0:
            print("Exiting.program.")
            break
        else:
            continue

    print("Program.ending.")
if __name__ == "__main__":
    main()