local str = "asset-4565464565345435-name.mp4"
local name = string.match(str, "-(%w+).mp4")
print(name)