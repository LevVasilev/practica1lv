def main(x):
    x = x.replace('<block>', '')\
        .replace('begin', '')\
        .replace('end', '')\
        .replace('</block>', '')\
        .replace('#', '')\
        .replace('local', '')\
        .replace('(', '')\
        .replace(')', '')\
        .replace('\n', '')\
        .replace(' ', '')\
        .replace('\'', '')
    x_parts = x.split('.')
    x_parts.pop(-1)
    x_parts1 = [i.split('=:') for i in x_parts]
    result = {}
    for i in x_parts1:
        value = i[0].split('@')
        value.pop(0)
        result[i[1]] = value
    return result


# Testing
print(main('begin<block>local#(@\'arana_760\' @\'rile_61\' @\'bezale_889\' ) =:\nmais.</block><block> local#( @\'leonis\' @\'mave_105\') =:onedra. </block>\n<block>local #( @\'aarge_727\' @\'bearen_242\' ) =:inesat. </block> end'))
