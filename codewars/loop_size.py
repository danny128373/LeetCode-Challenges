def loop_size(node):
    size = 1
    onestep = node
    twostep = node.next
    while(onestep != twostep):
        twostep = twostep.next.next
        onestep = onestep.next
    # we are inside the loop
    #onestep == twostep
    onestep = node.next
    size += 1
    while(onestep != twostep):
        size += 1
        onestep = onestep.next
    return size
