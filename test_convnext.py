import torchvision
model = torchvision.models.convnext_base(pretrained=True)
print(model)
# for name, para in model.named_parameters():
#     print(name, para.shape)

layers = list(model.features.children())
print(len(layers))
print(layers[-1])