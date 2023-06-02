from flask import Flask, request

app = Flask(__name__)

nfts = []

def comprar_nft():
    data = request.get_json()
    comprador = data['comprador']
    nft_id = data['nft_id']
    oferta = data['oferta']
    nft = {'comprador': comprador, 'nft_id': nft_id, 'oferta': oferta}
    nfts.append(nft)
    return 'Oferta de compra recibida.'

def vender_nft():
    data = request.get_json()
    vendedor = data['vendedor']
    nft_id = data['nft_id']
    demanda = data['demanda']
    nft = {'vendedor': vendedor, 'nft_id': nft_id, 'demanda': demanda}
    nfts.append(nft)
    return 'Oferta de venta recibida.'

app.add_url_rule('/comprar', 'comprar_nft', comprar_nft, methods=['POST'])
app.add_url_rule('/vender', 'vender_nft', vender_nft, methods=['POST'])

app.run()