import folder_paths
from pathlib import Path

COMFY_PATH = Path(__file__).parent.parent.parent

folder_paths.add_model_folder_path("animatediff_models", str(COMFY_PATH / "models" / "animatediff_models"))
folder_paths.add_model_folder_path("animatediff_models", str(COMFY_PATH / "custom_nodes" / "ComfyUI-AnimateDiff-Evolved" / "models" ))
folder_paths.add_model_folder_path("animatediff_motion_lora", str(COMFY_PATH / "models" / "animatediff_motion_lora"))
folder_paths.add_model_folder_path("animatediff_motion_lora", str(COMFY_PATH / "custom_nodes" / "ComfyUI-AnimateDiff-Evolved" / "motion_lora"))


class ArcheryInputBool:
    CATEGORY = "archery-inc"
    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("BOOLEAN",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"value": ("BOOLEAN", {"default": False})}}

    def run(self, value):
        return (value,)


class ArcheryInputFloat:
    CATEGORY = "archery-inc"
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("FLOAT",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"value": ("FLOAT", {"default": 0, "min": -999999999999999999999999, "max": 999999999999999999999999, "step": 0.001 }) }}

    def run(self, value):
        return (value,)


class ArcheryInputInt:
    CATEGORY = "archery-inc"
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("INT",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"value": ("INT", {"default": 0, "min": -999999999999999999999999, "max": 999999999999999999999999}) }}

    def run(self, value):
        return (value,)


class ArcheryInputAnimateDiffModelSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (folder_paths.get_filename_list("animatediff_models"),)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (folder_paths.get_filename_list("animatediff_models"), ),}}

    def run(self, value):
        return (value,)


WEIGHTS = ["linear", "ease in", "ease out", 'ease in-out', 'reverse in-out', 'weak input', 'weak output', 'weak middle', 'strong middle', 'style transfer', 'composition', 'strong style transfer']

class ArcheryInputIpAdapterWeightTypeSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (WEIGHTS,)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (WEIGHTS, ),}}

    def run(self, value):
        return (value,)


class ArcheryInputControlNetSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (folder_paths.get_filename_list("controlnet"),)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (folder_paths.get_filename_list("controlnet"), ),}}

    def run(self, value):
        return (value,)

def vae_list():
    vaes = folder_paths.get_filename_list("vae")
    approx_vaes = folder_paths.get_filename_list("vae_approx")
    sdxl_taesd_enc = False
    sdxl_taesd_dec = False
    sd1_taesd_enc = False
    sd1_taesd_dec = False

    for v in approx_vaes:
        if v.startswith("taesd_decoder."):
            sd1_taesd_dec = True
        elif v.startswith("taesd_encoder."):
            sd1_taesd_enc = True
        elif v.startswith("taesdxl_decoder."):
            sdxl_taesd_dec = True
        elif v.startswith("taesdxl_encoder."):
            sdxl_taesd_enc = True
    if sd1_taesd_dec and sd1_taesd_enc:
        vaes.append("taesd")
    if sdxl_taesd_dec and sdxl_taesd_enc:
        vaes.append("taesdxl")
    return vaes


class ArcheryInputVaeSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (vae_list(),)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (vae_list(), ),}}

    def run(self, value):
        return (value,)

AIO_PREPROCESSORS = ["none", "LineArtPreprocessor", "AnyLineArtPreprocessor_aux", "LineArtPreprocessor", "AnimeLineArtPreprocessor", "LineartStandardPreprocessor", "PiDiNetPreprocessor", "CannyEdgePreprocessor", 
                     "AnimeFace_SemSegPreprocessor", "ColorPreprocessor", "DensePosePreprocessor", "DepthAnythingPreprocessor", "Zoe_DepthAnythingPreprocessor", "DiffusionEdge_Preprocessor", "DSINE-NormalMapPreprocessor", 
                     "DWPreprocessor", "AnimalPosePreprocessor", "HEDPreprocessor", "FakeScribblePreprocessor", "InpaintPreprocessor", "LeReS-DepthMapPreprocessor", "Manga2Anime_LineArt_Preprocessor", 
                     "MediaPipe-FaceMeshPreprocessor",  "MeshGraphormer-DepthMapPreprocessor", "MeshGraphormer+ImpactDetector-DepthMapPreprocessor", "Metric3D-DepthMapPreprocessor", "Metric3D-NormalMapPreprocessor",
                     "MiDaS-NormalMapPreprocessor", "MiDaS-DepthMapPreprocessor", "M-LSDPreprocessor", "BAE-NormalMapPreprocessor", "OneFormer-COCO-SemSegPreprocessor", "OneFormer-ADE20K-SemSegPreprocessor",
                     "OpenposePreprocessor", "SavePoseKpsAsJsonFile", "FacialPartColoringFromPoseKps", "UpperBodyTrackingFromPoseKps", "ImageLuminanceDetector", "ImageIntensityDetector", "ScribblePreprocessor", 
                     "Scribble_XDoG_Preprocessor", "Scribble_PiDiNet_Preprocessor", "SAMPreprocessor", "ShufflePreprocessor", "TEED_Preprocessor", "TilePreprocessor", "TTPlanet_TileGF_Preprocessor", 
                     "TTPlanet_TileSimple_Preprocessor", "UniFormer-SemSegPreprocessor", "SemSegPreprocessor", "MaskOptFlow", "Unimatch_OptFlowPreprocessor", "Zoe-DepthMapPreprocessor"]

class ArcheryAIOAuxPreprocessorSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (AIO_PREPROCESSORS,)
    RETURN_NAMES = ("preprocessor",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"preprocessor": (AIO_PREPROCESSORS, ),}}

    def run(self, preprocessor):
        return (preprocessor,)


class ArcheryInputUpscalerSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (folder_paths.get_filename_list("upscale_models"),)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (folder_paths.get_filename_list("upscale_models"), ),}}

    def run(self, value):
        return (value,)


class ArcheryInputAnimateDiffMotionLoraSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (folder_paths.get_filename_list("animatediff_motion_lora"),)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (folder_paths.get_filename_list("animatediff_motion_lora"), ),}}

    def run(self, value):
        return (value,)


class ArcheryInputCheckpointSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (folder_paths.get_filename_list("checkpoints"),)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (folder_paths.get_filename_list("checkpoints"), ),}}

    def run(self, value):
        return (value,)


ip_adapter_options = ['LIGHT - SD1.5 only (low strength)', 'STANDARD (medium strength)', 'VIT-G (medium strength)', 'PLUS (high strength)', 'PLUS FACE (portraits)', 'FULL FACE - SD1.5 only (portraits stronger)']

class ArcheryInputIpAdapterSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (ip_adapter_options,)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (ip_adapter_options, ),}}

    def run(self, value):
        return (value,)

WEIGHT_TYPES = ["linear", "ease in", "ease out", 'ease in-out', 'reverse in-out', 'weak input', 'weak output', 'weak middle', 'strong middle', 'style transfer', 'composition', 'strong style transfer']

class ArcheryInputIpAdapterWeightSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (WEIGHT_TYPES,)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (WEIGHT_TYPES, ),}}

    def run(self, value):
        return (value,)


class ArcheryInputLoraSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (folder_paths.get_filename_list("loras"),)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (folder_paths.get_filename_list("loras"), ),}}

    def run(self, value):
        return (value,)
    
class ArcheryInputUpscalerSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (folder_paths.get_filename_list("upscale_models"),)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (folder_paths.get_filename_list("upscale_models"), ),}}

    def run(self, value):
        return (value,)


NOISE_TYPES = ["default", "constant", "empty", "repeated_context", "FreeNoise"]

class ArcheryInputNoiseTypeSelector:
    CATEGORY = 'archery-inc'
    RETURN_TYPES = (NOISE_TYPES,)
    RETURN_NAMES = ("value",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (NOISE_TYPES, ),}}

    def run(self, value):
        return (value,)
    

class ArcheryInputString:
    CATEGORY = "archery-inc"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"value": ("STRING", { "default": "" }) }}

    def run(self, value):
        return (value,)


class ArcheryInputStringMultiline:
    CATEGORY = "archery-inc"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"value": ("STRING", { "default": "", "multiline": True }) }}

    def run(self, value):
        return (value,)
