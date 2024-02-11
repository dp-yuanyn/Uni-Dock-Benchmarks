from pathlib import Path
from rdkit.Chem import AllChem as Chem
from rdkit.Chem import rdMolAlign


def calc_rmsd(
    ref_ligand: Path, 
    target_ligand: Path,
):
    ref_mol = Chem.SDMolSupplier(str(ref_ligand), removeHs=True)[0]
    target_mol = Chem.SDMolSupplier(str(target_ligand), removeHs=True)
    return [rdMolAlign.CalcRMS(ref_mol, tmol) for tmol in target_mol]