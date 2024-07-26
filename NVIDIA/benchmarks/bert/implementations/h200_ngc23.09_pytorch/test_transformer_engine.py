# Test with singularity image:
# singularity exec --nv --bind $PWD:/mnt /path_to_image/pytorch_bert.sif python /mnt/test_transformer_engine.py

import transformer_engine.pytorch as te

def test_transformer_engine():
    try:
        # Create a simple Linear layer from Transformer Engine
        layer = te.Linear(512, 512)
        print("Transformer Engine Linear layer created successfully.")
    except Exception as e:
        print("Error testing Transformer Engine:", e)

test_transformer_engine()
