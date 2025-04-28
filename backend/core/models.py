from dataclasses import dataclass, field
from typing import List, Optional
import json
from typing import Dict
# Class to use with classical parser
@dataclass
class ParsedCV:
    nome: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    lingue: List[str] = field(default_factory=list)
    skill: List[str] = field(default_factory=list)
    esperienze: List[str] = field(default_factory=list)
    istruzione: List[str] = field(default_factory=list)
    altro: List[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "nome_completo": self.nome,
            "email": self.email,
            "telefono": self.telefono,
            "lingue": self.lingue,
            "skill": self.skill,
            "esperienze_lavorative": self.esperienze,
            "istruzione": self.istruzione,
            "altro": self.altro,
        }

    def to_json(self, indent: int = 2):
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    def __str__(self):
        return self.to_json()
    
#Class to use with huggingface model
@dataclass
class LanguageDetails:
    level: Optional[str] = ""
    understanding: Optional[str] = ""
    speaking: Optional[str] = ""
    writing: Optional[str] = ""
    listening: Optional[str] = ""
    reading: Optional[str] = ""
    spokenProduction: Optional[str] = ""
    spokenInteraction: Optional[str] = ""

@dataclass
class Skills:
    hardSkills: Optional[List[str]] = field(default_factory=list)
    softSkills: Optional[Dict[str, str]] = field(default_factory=dict)

@dataclass
class WorkExperience:
    company: Optional[str] = ""
    position: Optional[str] = ""
    period: Optional[str] = ""
    description: Optional[str] = ""

@dataclass
class Education:
    university: Optional[str] = ""
    fieldOfStudy: Optional[str] = ""
    period: Optional[str] = ""
    grade: Optional[str] = ""
    level: Optional[str] = ""
    thesis: Optional[str] = ""
    description: Optional[str] = ""
    acquiredSkills: Optional[str] = ""

@dataclass
class CV:
    name: Optional[str] = ""
    email: Optional[str] = ""
    phone: Optional[str] = ""
    address: Optional[str] = ""
    languages: Optional[Dict[str, LanguageDetails]] = field(default_factory=dict)
    skills: Optional[Skills] = field(default_factory=Skills)
    workExperience: Optional[List[WorkExperience]] = field(default_factory=list)
    education: Optional[List[Education]] = field(default_factory=list)

