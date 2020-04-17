
def translate(path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    txt_name=path[:-4]
    f = open(txt_name+".txt", 'w')
    for text in texts:
    
        #print('\n{}'.format(text.description))
        print(text)
        #f.write(txt_name)
        f.write('\n"{}"'.format(text.description))
    
    #vertices = (['({},{})'.format(vertex.x, vertex.y)
    #            for vertex in text.bounding_poly.vertices])

    #print('bounds: {}'.format(','.join(vertices)))
    f.close()