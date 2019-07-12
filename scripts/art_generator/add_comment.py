import png
import sys

TEXT_CHUNK_FLAG = b'tEXt'
#'Comment\x00[type:angry;x:-13;y:-135;z-order:0;pivot_x:0.5015;pivot_y:0.4998;]'


def generate_chunk_tuple(type_flag, content):
    return tuple([type_flag, content])


def generate_text_chunk_tuple(str_info):
    type_flag = TEXT_CHUNK_FLAG
    comment_ba=bytearray(bytes("Comment").encode("utf-8"))
    comment_ba.append(b'\x00')
    comment_ba.extend(bytes(str_info).encode("utf-8"))
    
    return generate_chunk_tuple(type_flag, bytes(comment_ba))

def insert_text_chunk(target, text, index=1):
    if index < 0:
        raise Exception('The index value {} less than 0!'.format(index))

    reader = png.Reader(filename=target)
    chunks = reader.chunks()
    chunk_list = list(chunks)
    
    #add non comment chunks to new list, basically removes all existing comments
    new_chunk_list=[]
    for chunk in chunk_list:
        if 'tEXt' not in chunk[0]:
            new_chunk_list.append(chunk)
            
    #add the new comment with postions
    chunk_item = generate_text_chunk_tuple(text)
    new_chunk_list.insert(index, chunk_item)

    with open(target, 'wb') as dst_file:
        png.write_chunks(dst_file, new_chunk_list)


def _insert_text_chunk_to_png_test(src, message):
    #src = r'E:\temp\png\register_05.png'
    insert_text_chunk(src, message)


if __name__ == '__main__':
    _insert_text_chunk_to_png_test(sys.argv[1], sys.argv[2])